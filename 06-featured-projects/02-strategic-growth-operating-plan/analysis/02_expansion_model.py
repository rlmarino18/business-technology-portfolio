from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    # Baseline assumptions
    auv_m = 3.1
    restaurant_level_margin_pct = 23.4

    capex_per_new_restaurant_m = 2.2
    pre_opening_cost_per_restaurant_m = 0.265

    # Assumption:
    # New restaurants contribute approximately half of mature annual revenue
    # during the first year because openings occur throughout the year.
    year_one_ramp_factor = 0.50

    scenarios = {
        "Low": 10,
        "Base": 20,
        "High": 30,
    }

    results = []

    for scenario, incremental_restaurants in scenarios.items():
        mature_annual_revenue_m = (
            incremental_restaurants
            * auv_m
        )

        year_one_revenue_m = (
            mature_annual_revenue_m
            * year_one_ramp_factor
        )

        year_one_restaurant_profit_m = (
            year_one_revenue_m
            * restaurant_level_margin_pct
            / 100
        )

        mature_restaurant_profit_m = (
            mature_annual_revenue_m
            * restaurant_level_margin_pct
            / 100
        )

        capex_m = (
            incremental_restaurants
            * capex_per_new_restaurant_m
        )

        pre_opening_cost_m = (
            incremental_restaurants
            * pre_opening_cost_per_restaurant_m
        )

        total_initial_investment_m = (
            capex_m
            + pre_opening_cost_m
        )

        mature_payback_years = (
            total_initial_investment_m
            / mature_restaurant_profit_m
        )

        results.append(
            {
                "scenario": scenario,
                "incremental_restaurants": incremental_restaurants,
                "mature_annual_revenue_m": mature_annual_revenue_m,
                "year_one_revenue_m": year_one_revenue_m,
                "year_one_restaurant_profit_m": year_one_restaurant_profit_m,
                "mature_restaurant_profit_m": mature_restaurant_profit_m,
                "capex_m": capex_m,
                "pre_opening_cost_m": pre_opening_cost_m,
                "total_initial_investment_m": total_initial_investment_m,
                "mature_payback_years": mature_payback_years,
            }
        )

    results_df = pd.DataFrame(results)

    print("\nACCELERATED EXPANSION SENSITIVITY")
    print(results_df.to_string(index=False))

    output_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "accelerated_expansion_sensitivity.csv"
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    results_df.to_csv(
        output_path,
        index=False,
    )

    print(
        f"\nSensitivity model saved to: "
        f"{output_path}"
    )


if __name__ == "__main__":
    main()