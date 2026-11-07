import pandas as pd


def calculate_score(
    scores: dict[str, int],
    weights: dict[str, float],
) -> float:
    return sum(
        scores[criterion] * weight
        for criterion, weight in weights.items()
    )


def main() -> None:
    alternatives = {
        "Accelerated Expansion": {
            "economic_impact": 5,
            "capital_efficiency": 2,
            "execution_feasibility": 3,
            "time_to_value": 3,
            "strategic_fit": 5,
            "scalability": 4,
            "evidence_strength": 4,
        },
        "Same-Store Productivity": {
            "economic_impact": 4,
            "capital_efficiency": 4,
            "execution_feasibility": 4,
            "time_to_value": 4,
            "strategic_fit": 5,
            "scalability": 5,
            "evidence_strength": 3,
        },
        "Scalable Infrastructure": {
            "economic_impact": 3,
            "capital_efficiency": 3,
            "execution_feasibility": 3,
            "time_to_value": 2,
            "strategic_fit": 5,
            "scalability": 5,
            "evidence_strength": 3,
        },
    }

    weighting_scenarios = {
        "Balanced": {
            "economic_impact": 0.25,
            "capital_efficiency": 0.20,
            "execution_feasibility": 0.15,
            "time_to_value": 0.10,
            "strategic_fit": 0.15,
            "scalability": 0.10,
            "evidence_strength": 0.05,
        },
        "Growth-First": {
            "economic_impact": 0.35,
            "capital_efficiency": 0.10,
            "execution_feasibility": 0.10,
            "time_to_value": 0.05,
            "strategic_fit": 0.20,
            "scalability": 0.15,
            "evidence_strength": 0.05,
        },
        "Efficiency-First": {
            "economic_impact": 0.20,
            "capital_efficiency": 0.25,
            "execution_feasibility": 0.20,
            "time_to_value": 0.15,
            "strategic_fit": 0.10,
            "scalability": 0.05,
            "evidence_strength": 0.05,
        },
    }

    results = []

    for scenario_name, weights in weighting_scenarios.items():
        for alternative, scores in alternatives.items():
            weighted_score = calculate_score(
                scores=scores,
                weights=weights,
            )

            results.append(
                {
                    "scenario": scenario_name,
                    "alternative": alternative,
                    "weighted_score": weighted_score,
                }
            )

    results_df = pd.DataFrame(results)

    results_df["priority_rank"] = (
        results_df
        .groupby("scenario")["weighted_score"]
        .rank(
            method="first",
            ascending=False,
        )
        .astype(int)
    )

    results_df = results_df.sort_values(
        by=["scenario", "priority_rank"]
    )

    print("\nPRIORITIZATION SENSITIVITY ANALYSIS")
    print(
        results_df[
            [
                "scenario",
                "priority_rank",
                "alternative",
                "weighted_score",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()