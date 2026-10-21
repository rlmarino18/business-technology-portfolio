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
    subscription_revenue_m = baseline["subscription_revenue"]
    subscription_gross_margin_pct = baseline["subscription_gross_margin_pct"]
    locations = 164_000

    # Calculated baseline
    subscription_revenue_per_location = (
        subscription_revenue_m * 1_000_000 / locations
    )

    print("2025 SUBSCRIPTION BASELINE")
    print(f"Subscription Revenue: ${subscription_revenue_m:.0f}M")
    print(f"Locations: {locations:,}")
    print(
        f"Subscription Revenue per Location: "
        f"${subscription_revenue_per_location:,.0f}"
    )
    print(
        f"Subscription Gross Margin: "
        f"{subscription_gross_margin_pct:.2f}%"
    )

    # Assumptions — sensitivity cases, not company guidance
    scenarios = {
        "Low": 0.02,
        "Base": 0.05,
        "High": 0.08,
    }

    results = []

    for scenario, uplift_pct in scenarios.items():
        incremental_revenue_m = (
            subscription_revenue_m * uplift_pct
        )

        incremental_gross_profit_m = (
            incremental_revenue_m
            * subscription_gross_margin_pct
            / 100
        )

        results.append(
            {
                "scenario": scenario,
                "revenue_per_location_uplift_pct": uplift_pct * 100,
                "incremental_subscription_revenue_m": incremental_revenue_m,
                "incremental_gross_profit_m": incremental_gross_profit_m,
            }
        )

    results_df = pd.DataFrame(results)

    print("\nSUBSCRIPTION ADOPTION SENSITIVITY")
    print(results_df.to_string(index=False))

    output_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "processed"
        / "subscription_adoption_sensitivity.csv"
    )


    # Implementation-cost assumptions for payback sensitivity
    implementation_cost_cases_m = [10, 20, 30]

    payback_results = []

    for _, row in results_df.iterrows():
        for implementation_cost_m in implementation_cost_cases_m:
            payback_months = (
                implementation_cost_m
                / row["incremental_gross_profit_m"]
                * 12
            )

            payback_results.append(
                {
                    "scenario": row["scenario"],
                    "uplift_pct": row["revenue_per_location_uplift_pct"],
                    "incremental_gross_profit_m": row["incremental_gross_profit_m"],
                    "implementation_cost_m": implementation_cost_m,
                    "payback_months": payback_months,
                }
            )

    payback_df = pd.DataFrame(payback_results)

    print("\nSUBSCRIPTION ADOPTION PAYBACK SENSITIVITY")
    print(payback_df.to_string(index=False))

    results_df.to_csv(output_path, index=False)

    print(f"\nSensitivity model saved to: {output_path}")


if __name__ == "__main__":
    main()
