from pathlib import Path

import pandas as pd


DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "processed"
    / "toast_financials_2023_2025_processed.csv"
)


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    baseline = df.loc[df["year"] == 2025].iloc[0]

    # Reported inputs
    revenue_m = baseline["total_revenue"]
    total_opex_m = baseline["total_operating_expenses"]
    operating_income_m = baseline["operating_income"]

    # Calculated baseline
    opex_pct_revenue = (
        total_opex_m
        / revenue_m
        * 100
    )

    operating_margin_pct = (
        operating_income_m
        / revenue_m
        * 100
    )

    print("2025 OPERATING LEVERAGE BASELINE")
    print(f"Revenue: ${revenue_m:.0f}M")
    print(f"Total Operating Expenses: ${total_opex_m:.0f}M")
    print(f"OpEx as % of Revenue: {opex_pct_revenue:.2f}%")
    print(f"Operating Income: ${operating_income_m:.0f}M")
    print(f"Operating Margin: {operating_margin_pct:.2f}%")

    # Assumptions — percentage-point improvement in OpEx efficiency
    scenarios = {
        "Low": 0.5,
        "Base": 1.0,
        "High": 1.5,
    }

    results = []

    for scenario, efficiency_improvement_pp in scenarios.items():
        operating_income_improvement_m = (
            revenue_m
            * efficiency_improvement_pp
            / 100
        )

        resulting_operating_income_m = (
            operating_income_m
            + operating_income_improvement_m
        )

        resulting_operating_margin_pct = (
            resulting_operating_income_m
            / revenue_m
            * 100
        )

        resulting_opex_pct_revenue = (
            opex_pct_revenue
            - efficiency_improvement_pp
        )

        results.append(
            {
                "scenario": scenario,
                "opex_efficiency_improvement_pp": efficiency_improvement_pp,
                "operating_income_improvement_m": operating_income_improvement_m,
                "resulting_opex_pct_revenue": resulting_opex_pct_revenue,
                "resulting_operating_income_m": resulting_operating_income_m,
                "resulting_operating_margin_pct": resulting_operating_margin_pct,
            }
        )

    results_df = pd.DataFrame(results)

    print("\nOPERATING LEVERAGE SENSITIVITY")
    print(results_df.to_string(index=False))

    output_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "processed"
        / "operating_leverage_sensitivity.csv"
    )

    results_df.to_csv(output_path, index=False)

    print(f"\nSensitivity model saved to: {output_path}")


if __name__ == "__main__":
    main()
