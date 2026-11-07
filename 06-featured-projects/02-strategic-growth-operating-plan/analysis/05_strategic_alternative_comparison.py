from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

EXPANSION_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "accelerated_expansion_sensitivity.csv"
)

PRODUCTIVITY_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "same_store_productivity_sensitivity.csv"
)

INFRASTRUCTURE_PATH = (
    PROJECT_ROOT
    / "data"
    / "processed"
    / "infrastructure_scalability_sensitivity.csv"
)


def main() -> None:
    expansion_df = pd.read_csv(EXPANSION_PATH)
    productivity_df = pd.read_csv(PRODUCTIVITY_PATH)
    infrastructure_df = pd.read_csv(INFRASTRUCTURE_PATH)

    expansion_base = expansion_df[
        expansion_df["scenario"] == "Base"
    ].iloc[0]

    productivity_base = productivity_df[
        productivity_df["scenario"] == "Base"
    ].iloc[0]

    infrastructure_base = infrastructure_df[
        infrastructure_df["scenario"] == "Base"
    ].iloc[0]

    comparison = pd.DataFrame(
        [
            {
                "alternative": "Accelerated Expansion",
                "base_case_assumption": "20 incremental restaurants",
                "incremental_revenue_m":
                    expansion_base["mature_annual_revenue_m"],
                "incremental_profit_m":
                    expansion_base["mature_restaurant_profit_m"],
                "known_initial_investment_m":
                    expansion_base["total_initial_investment_m"],
                "payback_years":
                    expansion_base["mature_payback_years"],
                "primary_value": "Footprint and revenue growth",
                "capital_intensity": "High",
                "execution_risk": "High",
                "time_to_value": "Medium",
            },
            {
                "alternative": "Same-Store Productivity",
                "base_case_assumption": "3% productivity uplift",
                "incremental_revenue_m":
                    productivity_base["incremental_revenue_m"],
                "incremental_profit_m":
                    productivity_base["incremental_restaurant_profit_m"],
                "known_initial_investment_m": None,
                "payback_years": None,
                "primary_value": "Existing-store productivity",
                "capital_intensity": "Unknown",
                "execution_risk": "Medium",
                "time_to_value": "Medium",
            },
            {
                "alternative": "Scalable Infrastructure",
                "base_case_assumption": "0.50 pp efficiency improvement",
                "incremental_revenue_m": None,
                "incremental_profit_m":
                    infrastructure_base["illustrative_operating_income_m"],
                "known_initial_investment_m": None,
                "payback_years": None,
                "primary_value": "Organizational scalability",
                "capital_intensity": "Unknown",
                "execution_risk": "Medium",
                "time_to_value": "Long",
            },
        ]
    )

    print("\nSTRATEGIC ALTERNATIVE BASE-CASE COMPARISON")
    print(comparison.to_string(index=False))

    output_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "strategic_alternative_comparison.csv"
    )

    comparison.to_csv(
        output_path,
        index=False,
    )

    print(
        f"\nComparison saved to: "
        f"{output_path}"
    )


if __name__ == "__main__":
    main()