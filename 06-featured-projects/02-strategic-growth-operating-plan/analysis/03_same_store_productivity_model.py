from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    # Baseline operating assumptions
    restaurant_count = 500
    auv_m = 3.1
    restaurant_level_margin_pct = 23.4

    # Same-store productivity scenarios
    scenarios = {
        "Low": 0.01,
        "Base": 0.03,
        "High": 0.05,
    }

    baseline_system_sales_m = (
        restaurant_count
        * auv_m
    )

    results = []

    for scenario, productivity_uplift in scenarios.items():
        incremental_revenue_m = (
            baseline_system_sales_m
            * productivity_uplift
        )

        incremental_restaurant_profit_m = (
            incremental_revenue_m
            * restaurant_level_margin_pct
            / 100
        )

        incremental_revenue_per_restaurant_m = (
            auv_m
            * productivity_uplift
        )

        results.append(
            {
                "scenario": scenario,
                "productivity_uplift_pct": productivity_uplift * 100,
                "baseline_system_sales_m": baseline_system_sales_m,
                "incremental_revenue_m": incremental_revenue_m,
                "incremental_revenue_per_restaurant_m":
                    incremental_revenue_per_restaurant_m,
                "incremental_restaurant_profit_m":
                    incremental_restaurant_profit_m,
            }
        )

    results_df = pd.DataFrame(results)

    print("\nSAME-STORE PRODUCTIVITY SENSITIVITY")
    print(results_df.to_string(index=False))

    output_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "same_store_productivity_sensitivity.csv"
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