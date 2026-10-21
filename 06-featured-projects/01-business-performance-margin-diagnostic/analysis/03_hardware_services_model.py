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
    revenue_m = baseline["hardware_services_revenue"]
    cost_m = baseline["hardware_services_cost"]

    # Calculated baseline
    gross_profit_m = revenue_m - cost_m
    gross_margin_pct = gross_profit_m / revenue_m * 100
    gross_loss_m = abs(gross_profit_m)

    print("2025 HARDWARE & SERVICES BASELINE")
    print(f"Revenue: ${revenue_m:.0f}M")
    print(f"Cost: ${cost_m:.0f}M")
    print(f"Gross Profit: ${gross_profit_m:.0f}M")
    print(f"Gross Margin: {gross_margin_pct:.2f}%")
    print(f"Gross Loss Pool: ${gross_loss_m:.0f}M")

    # Assumptions — sensitivity cases, not company guidance
    scenarios = {
        "Low": 0.10,
        "Base": 0.20,
        "High": 0.30,
    }

    results = []

    for scenario, loss_reduction_pct in scenarios.items():
        gross_profit_improvement_m = (
            gross_loss_m * loss_reduction_pct
        )

        resulting_gross_profit_m = (
            gross_profit_m + gross_profit_improvement_m
        )

        resulting_gross_margin_pct = (
            resulting_gross_profit_m
            / revenue_m
            * 100
        )

        results.append(
            {
                "scenario": scenario,
                "gross_loss_reduction_pct": loss_reduction_pct * 100,
                "gross_profit_improvement_m": gross_profit_improvement_m,
                "resulting_gross_profit_m": resulting_gross_profit_m,
                "resulting_gross_margin_pct": resulting_gross_margin_pct,
            }
        )

    results_df = pd.DataFrame(results)

    print("\nHARDWARE & SERVICES LOSS-REDUCTION SENSITIVITY")
    print(results_df.to_string(index=False))

    output_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "processed"
        / "hardware_services_sensitivity.csv"
    )


    # Implementation-cost assumptions for payback sensitivity
    implementation_cost_cases_m = [10, 20, 30]

    payback_results = []

    for _, row in results_df.iterrows():
        for implementation_cost_m in implementation_cost_cases_m:
            payback_months = (
                implementation_cost_m
                / row["gross_profit_improvement_m"]
                * 12
            )

            payback_results.append(
                {
                    "scenario": row["scenario"],
                    "gross_loss_reduction_pct": row["gross_loss_reduction_pct"],
                    "gross_profit_improvement_m": row["gross_profit_improvement_m"],
                    "implementation_cost_m": implementation_cost_m,
                    "payback_months": payback_months,
                }
            )

    payback_df = pd.DataFrame(payback_results)

    print("\nHARDWARE & SERVICES PAYBACK SENSITIVITY")
    print(payback_df.to_string(index=False))

    results_df.to_csv(output_path, index=False)

    print(f"\nSensitivity model saved to: {output_path}")


if __name__ == "__main__":
    main()
