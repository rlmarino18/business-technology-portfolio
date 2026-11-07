from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    # Baseline reported revenue used to estimate the financial effect
    # of improved corporate operating leverage.
    revenue_m = 1169.3

    # These scenarios represent potential operating-efficiency outcomes
    # enabled by better systems, processes, management capacity,
    # analytics, training, and infrastructure.
    #
    # They are not forecasts and should not be interpreted as direct
    # returns from infrastructure spending.
    scenarios = {
        "Low": 0.25,
        "Base": 0.50,
        "High": 0.75,
    }

    results = []

    for scenario, efficiency_improvement_pp in scenarios.items():
        incremental_operating_income_m = (
            revenue_m
            * efficiency_improvement_pp
            / 100
        )

        results.append(
            {
                "scenario": scenario,
                "efficiency_improvement_pp": efficiency_improvement_pp,
                "baseline_revenue_m": revenue_m,
                "illustrative_operating_income_m":
                    incremental_operating_income_m,
            }
        )

    results_df = pd.DataFrame(results)

    print("\nINFRASTRUCTURE SCALABILITY SENSITIVITY")
    print(results_df.to_string(index=False))

    print(
        "\nINTERPRETATION"
    )

    print(
        "This sensitivity illustrates one measurable financial outcome "
        "of scalable infrastructure: improved corporate operating leverage."
    )

    print(
        "It does not estimate the total value or ROI of infrastructure "
        "investment because implementation costs and indirect benefits "
        "such as opening capacity, training quality, supply-chain "
        "resilience, and operating consistency are not publicly observable."
    )

    output_path = (
        PROJECT_ROOT
        / "data"
        / "processed"
        / "infrastructure_scalability_sensitivity.csv"
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