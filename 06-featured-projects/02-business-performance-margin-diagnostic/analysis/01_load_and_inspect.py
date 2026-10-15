from pathlib import Path

import pandas as pd

import matplotlib.pyplot as plt

DATA_PATH = (
    Path(__file__).resolve().parents[1]
    / "data"
    / "raw"
    / "toast_financials_2023_2025.csv"
)


def main() -> None:
    df = pd.read_csv(DATA_PATH)

    print("\nFIRST 5 ROWS")
    print(df.head())

    print("\nSHAPE")
    print(df.shape)

    print("\nCOLUMNS")
    print(df.columns.tolist())

    print("\nDATA TYPES")
    print(df.dtypes)

    print("\nDATAFRAME INFO")
    df.info()

    df["gross_profit"] = (
        df["total_revenue"] - df["total_cost_of_revenue"]
    )

    df["gross_margin_pct"] = (
        df["gross_profit"] / df["total_revenue"] * 100
    )

    print("\nGROSS PROFIT AND GROSS MARGIN")
    print(
        df[
            [
                "year",
                "total_revenue",
                "total_cost_of_revenue",
                "gross_profit",
                "gross_margin_pct",
            ]
        ]
    )

    df["total_revenue_growth_pct"] = (
        df["total_revenue"].pct_change() * 100
    )

    df["subscription_growth_pct"] = (
        df["subscription_revenue"].pct_change() * 100
    )

    df["fintech_growth_pct"] = (
        df["fintech_revenue"].pct_change() * 100
    )

    print("\nYEAR-OVER-YEAR REVENUE GROWTH")
    print(
        df[
            [
                "year",
                "total_revenue_growth_pct",
                "subscription_growth_pct",
                "fintech_growth_pct",
            ]
        ]
    )

    df["subscription_gross_profit"] = (
        df["subscription_revenue"] - df["subscription_cost"]
    )

    df["subscription_gross_margin_pct"] = (
        df["subscription_gross_profit"]
        / df["subscription_revenue"]
        * 100
    )

    df["fintech_gross_profit"] = (
        df["fintech_revenue"] - df["fintech_cost"]
    )

    df["fintech_gross_margin_pct"] = (
        df["fintech_gross_profit"]
        / df["fintech_revenue"]
        * 100
    )

    print("\nSEGMENT GROSS MARGINS")
    print(
        df[
            [
                "year",
                "subscription_gross_margin_pct",
                "fintech_gross_margin_pct",
            ]
        ]
    )

    df["subscription_revenue_mix_pct"] = (
        df["subscription_revenue"]
        / df["total_revenue"]
        * 100
    )

    df["fintech_revenue_mix_pct"] = (
        df["fintech_revenue"]
        / df["total_revenue"]
        * 100
    )

    df["hardware_services_revenue_mix_pct"] = (
        df["hardware_services_revenue"]
        / df["total_revenue"]
        * 100
    )

    print("\nREVENUE MIX")
    print(
        df[
            [
                "year",
                "subscription_revenue_mix_pct",
                "fintech_revenue_mix_pct",
                "hardware_services_revenue_mix_pct",
            ]
        ]
    )

    df["subscription_mix_change_pp"] = (
        df["subscription_revenue_mix_pct"].diff()
    )

    df["fintech_mix_change_pp"] = (
        df["fintech_revenue_mix_pct"].diff()
    )

    df["hardware_mix_change_pp"] = (
        df["hardware_services_revenue_mix_pct"].diff()
    )

    print("\nYEAR-OVER-YEAR REVENUE MIX CHANGE")
    print(
        df[
            [
                "year",
                "subscription_mix_change_pp",
                "fintech_mix_change_pp",
                "hardware_mix_change_pp",
            ]
        ]
    )

    df["subscription_gross_profit_mix_pct"] = (
        df["subscription_gross_profit"]
        / df["gross_profit"]
        * 100
    )

    df["fintech_gross_profit_mix_pct"] = (
        df["fintech_gross_profit"]
        / df["gross_profit"]
        * 100
    )

    df["hardware_services_gross_profit"] = (
        df["hardware_services_revenue"]
        - df["hardware_services_cost"]
    )

    df["hardware_services_gross_profit_mix_pct"] = (
        df["hardware_services_gross_profit"]
        / df["gross_profit"]
        * 100
    )

    print("\nGROSS PROFIT CONTRIBUTION BY SEGMENT")
    print(
        df[
            [
                "year",
                "subscription_gross_profit_mix_pct",
                "fintech_gross_profit_mix_pct",
                "hardware_services_gross_profit_mix_pct",
            ]
        ]
    )

    df["unallocated_amortization_effect"] = (
        -df["intangible_amortization"]
    )

    df["segment_gross_profit_total"] = (
        df["subscription_gross_profit"]
        + df["fintech_gross_profit"]
        + df["hardware_services_gross_profit"]
        + df["unallocated_amortization_effect"]
    )

    df["gross_profit_reconciliation_difference"] = (
        df["gross_profit"]
        - df["segment_gross_profit_total"]
    )

    print("\nGROSS PROFIT RECONCILIATION")
    print(
        df[
            [
                "year",
                "gross_profit",
                "segment_gross_profit_total",
                "gross_profit_reconciliation_difference",
            ]
        ]
    )

    high_margin_years = df[
        df["gross_margin_pct"] > 24
    ]

    print("\nYEARS WITH GROSS MARGIN ABOVE 24%")
    print(
        high_margin_years[
            [
                "year",
                "total_revenue",
                "gross_profit",
                "gross_margin_pct",
            ]
        ]
    )

    strong_performance_years = df[
        (df["gross_margin_pct"] > 24)
        & (df["total_revenue_growth_pct"] > 20)
    ]

    print("\nYEARS WITH >24% GROSS MARGIN AND >20% REVENUE GROWTH")
    print(
        strong_performance_years[
            [
                "year",
                "total_revenue_growth_pct",
                "gross_margin_pct",
            ]
        ]
    )

    strong_performance_summary = df.loc[
        (df["gross_margin_pct"] > 24)
        & (df["total_revenue_growth_pct"] > 20),
        [
            "year",
            "total_revenue",
            "total_revenue_growth_pct",
            "gross_profit",
            "gross_margin_pct",
        ],
    ]

    print("\nSTRONG PERFORMANCE SUMMARY USING LOC")
    print(strong_performance_summary)

    margin_ranked_years = df.loc[
        :,
        [
            "year",
            "total_revenue_growth_pct",
            "gross_margin_pct",
        ],
    ].sort_values(
        by="gross_margin_pct",
        ascending=False,
    )

    print("\nYEARS RANKED BY GROSS MARGIN")
    print(margin_ranked_years)

    highest_margin_year = df.nlargest(
        1,
        "gross_margin_pct",
    )

    lowest_margin_year = df.nsmallest(
        1,
        "gross_margin_pct",
    )

    print("\nHIGHEST GROSS MARGIN YEAR")
    print(
        highest_margin_year[
            [
                "year",
                "gross_margin_pct",
            ]
        ]
    )

    print("\nLOWEST GROSS MARGIN YEAR")
    print(
        lowest_margin_year[
            [
                "year",
                "gross_margin_pct",
            ]
        ]
    )

    performance_summary = df[
        [
            "total_revenue_growth_pct",
            "gross_margin_pct",
        ]
    ].agg(
        [
            "mean",
            "min",
            "max",
        ]
    )

    print("\nPERFORMANCE SUMMARY")
    print(performance_summary)
    print("\nMISSING VALUES BY COLUMN")
    print(df.isna().sum())

    growth_analysis = df.dropna(
        subset=[
            "total_revenue_growth_pct",
            "subscription_growth_pct",
            "fintech_growth_pct",
        ]
    )

    duplicate_rows = df.duplicated().sum()

    print("\nDUPLICATE ROW COUNT")
    print(duplicate_rows)

    print("\nGROWTH ANALYSIS ROWS")
    print(
        growth_analysis[
            [
                "year",
                "total_revenue_growth_pct",
                "subscription_growth_pct",
                "fintech_growth_pct",
            ]
        ]
    )

    duplicate_years = df.duplicated(
        subset=["year"]
    ).sum()

    print("\nDUPLICATE YEAR COUNT")
    print(duplicate_years)

    descriptive_stats = df[
        [
            "total_revenue",
            "gross_profit",
            "gross_margin_pct",
            "subscription_gross_margin_pct",
            "fintech_gross_margin_pct",
        ]
    ].describe()

    print("\nDESCRIPTIVE STATISTICS")
    print(descriptive_stats)

    plt.figure()

    plt.plot(
        df["year"],
        df["gross_margin_pct"],
        marker="o",
    )

    plt.title("Toast Gross Margin Trend")
    plt.xlabel("Year")
    plt.ylabel("Gross Margin (%)")

    plt.xticks(df["year"])
    plt.tight_layout()

    plt.savefig(
        Path(__file__).resolve().parents[1]
        / "deliverables"
        / "charts"
        / "gross_margin_trend.png",
        dpi=150,
    )

    plt.show()

    plt.figure()

    plt.plot(
        df["year"],
        df["subscription_gross_margin_pct"],
        marker="o",
        label="Subscription",
    )

    plt.plot(
        df["year"],
        df["fintech_gross_margin_pct"],
        marker="o",
        label="Fintech",
    )

    plt.title("Toast Segment Gross Margin Trend")
    plt.xlabel("Year")
    plt.ylabel("Gross Margin (%)")
    plt.xticks(df["year"])
    plt.legend()

    plt.tight_layout()

    plt.savefig(
        Path(__file__).resolve().parents[1]
        / "deliverables"
        / "charts"
        / "segment_gross_margin_trend.png",
        dpi=150,
    )

    plt.show()

    plt.figure()

    plt.plot(
        df["year"],
        df["subscription_revenue_mix_pct"],
        marker="o",
        label="Subscription",
    )

    plt.plot(
        df["year"],
        df["fintech_revenue_mix_pct"],
        marker="o",
        label="Fintech",
    )

    plt.plot(
        df["year"],
        df["hardware_services_revenue_mix_pct"],
        marker="o",
        label="Hardware & Services",
    )

    plt.title("Toast Revenue Mix Trend")
    plt.xlabel("Year")
    plt.ylabel("Revenue Mix (%)")
    plt.xticks(df["year"])
    plt.legend()

    plt.tight_layout()

    plt.savefig(
        Path(__file__).resolve().parents[1]
        / "deliverables"
        / "charts"
        / "revenue_mix_trend.png",
        dpi=150,
    )

    plt.show()

    plt.figure()

    plt.plot(
        df["year"],
        df["subscription_gross_profit_mix_pct"],
        marker="o",
        label="Subscription",
    )

    plt.plot(
        df["year"],
        df["fintech_gross_profit_mix_pct"],
        marker="o",
        label="Fintech",
    )

    plt.plot(
        df["year"],
        df["hardware_services_gross_profit_mix_pct"],
        marker="o",
        label="Hardware & Services",
    )

    plt.title("Toast Gross Profit Contribution by Segment")
    plt.xlabel("Year")
    plt.ylabel("Gross Profit Contribution (%)")
    plt.xticks(df["year"])
    plt.legend()

    plt.tight_layout()

    plt.savefig(
        Path(__file__).resolve().parents[1]
        / "deliverables"
        / "charts"
        / "gross_profit_contribution_by_segment.png",
        dpi=150,
    )

    plt.show()

    plt.figure()

    plt.plot(
        df["year"],
        df["subscription_gross_profit"],
        marker="o",
        label="Subscription",
    )

    plt.plot(
        df["year"],
        df["fintech_gross_profit"],
        marker="o",
        label="Fintech",
    )

    plt.plot(
        df["year"],
        df["hardware_services_gross_profit"],
        marker="o",
        label="Hardware & Services",
    )

    plt.title("Toast Gross Profit by Segment")
    plt.xlabel("Year")
    plt.ylabel("Gross Profit ($M)")
    plt.xticks(df["year"])
    plt.legend()

    plt.tight_layout()
    plt.show()

    segment_gp_change = {
        "Subscription": (
            df.loc[df["year"] == 2025, "subscription_gross_profit"].iloc[0]
            - df.loc[df["year"] == 2023, "subscription_gross_profit"].iloc[0]
        ),
        "Fintech": (
            df.loc[df["year"] == 2025, "fintech_gross_profit"].iloc[0]
            - df.loc[df["year"] == 2023, "fintech_gross_profit"].iloc[0]
        ),
        "Hardware & Services": (
            df.loc[df["year"] == 2025, "hardware_services_gross_profit"].iloc[0]
            - df.loc[df["year"] == 2023, "hardware_services_gross_profit"].iloc[0]
        ),
    }

    print("\n2023 TO 2025 GROSS PROFIT CHANGE BY SEGMENT")
    for segment, change in segment_gp_change.items():
        print(f"{segment}: {change:.0f}")

    total_gp_change = (
        df.loc[df["year"] == 2025, "gross_profit"].iloc[0]
        - df.loc[df["year"] == 2023, "gross_profit"].iloc[0]
    )

    print("\n2023 TO 2025 CONTRIBUTION TO GROSS PROFIT GROWTH")

    for segment, change in segment_gp_change.items():
        contribution_pct = change / total_gp_change * 100
        print(
            f"{segment}: {contribution_pct:.1f}%"
        )

    margin_change_pp = {
        "Overall": (
            df.loc[df["year"] == 2025, "gross_margin_pct"].iloc[0]
            - df.loc[df["year"] == 2023, "gross_margin_pct"].iloc[0]
        ),
        "Subscription": (
            df.loc[df["year"] == 2025, "subscription_gross_margin_pct"].iloc[0]
            - df.loc[df["year"] == 2023, "subscription_gross_margin_pct"].iloc[0]
        ),
        "Fintech": (
            df.loc[df["year"] == 2025, "fintech_gross_margin_pct"].iloc[0]
            - df.loc[df["year"] == 2023, "fintech_gross_margin_pct"].iloc[0]
        ),
    }

    print("\n2023 TO 2025 GROSS MARGIN CHANGE")
    for segment, change in margin_change_pp.items():
        print(f"{segment}: {change:.2f} percentage points")

    revenue_mix_change_pp = {
        "Subscription": (
            df.loc[df["year"] == 2025, "subscription_revenue_mix_pct"].iloc[0]
            - df.loc[df["year"] == 2023, "subscription_revenue_mix_pct"].iloc[0]
        ),
        "Fintech": (
            df.loc[df["year"] == 2025, "fintech_revenue_mix_pct"].iloc[0]
            - df.loc[df["year"] == 2023, "fintech_revenue_mix_pct"].iloc[0]
        ),
        "Hardware & Services": (
            df.loc[df["year"] == 2025, "hardware_services_revenue_mix_pct"].iloc[0]
            - df.loc[df["year"] == 2023, "hardware_services_revenue_mix_pct"].iloc[0]
        ),
    }

    print("\n2023 TO 2025 REVENUE MIX CHANGE")
    for segment, change in revenue_mix_change_pp.items():
        print(f"{segment}: {change:.2f} percentage points")

    plt.figure()

    plt.bar(
        segment_gp_change.keys(),
        segment_gp_change.values(),
    )

    plt.title("2023–2025 Gross Profit Change by Segment")
    plt.xlabel("Segment")
    plt.ylabel("Gross Profit Change ($M)")

    plt.tight_layout()

    plt.savefig(
        Path(__file__).resolve().parents[1]
        / "deliverables"
        / "charts"
        / "gross_profit_change_by_segment.png",
        dpi=150,
    )

    plt.show()

    output_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "processed"
        / "toast_financials_2023_2025_processed.csv"
    )

    df.to_csv(output_path, index=False)

    print(f"\nProcessed dataset saved to: {output_path}")

    segment_columns = [
    "subscription",
    "fintech",
    "hardware_services",
    ]

    for segment in segment_columns:
        df[f"{segment}_revenue_mix"] = (
        df[f"{segment}_revenue"] / df["total_revenue"]
    )
        df[f"{segment}_margin"] = (
        (
            df[f"{segment}_revenue"]
            - df[f"{segment}_cost"]
        )
        / df[f"{segment}_revenue"]
    )

    print("\nMARGIN DECOMPOSITION INPUTS")

    print(
        df[
            [
                "year",
                "subscription_revenue_mix",
                "subscription_margin",
                "fintech_revenue_mix",
                "fintech_margin",
                "hardware_services_revenue_mix",
                "hardware_services_margin",
            ]
        ]
    )

    # Calculate each segment's contribution to consolidated gross margin

    for segment in segment_columns:
        df[f"{segment}_weighted_margin"] = (
            df[f"{segment}_revenue_mix"]
            * df[f"{segment}_margin"]
        )

    df["weighted_segment_margin"] = (
        df["subscription_weighted_margin"]
        + df["fintech_weighted_margin"]
        + df["hardware_services_weighted_margin"]
    )

    print("\nWEIGHTED SEGMENT MARGIN")
    print(
        df[
            [
                "year",
                "subscription_weighted_margin",
                "fintech_weighted_margin",
                "hardware_services_weighted_margin",
                "weighted_segment_margin",
            ]
        ]
    )

    df["amortization_margin_effect"] = (
        df["intangible_amortization"] / df["total_revenue"]
    )

    df["reconstructed_gross_margin"] = (
        df["weighted_segment_margin"]
        - df["amortization_margin_effect"]
    )

    df["reported_gross_margin_decimal"] = (
        df["gross_margin_pct"] / 100
    )

    df["margin_reconciliation_difference"] = (
        df["reconstructed_gross_margin"]
        - df["reported_gross_margin_decimal"]
    )

    print("\nMARGIN RECONCILIATION")
    print(
        df[
            [
                "year",
                "weighted_segment_margin",
                "amortization_margin_effect",
                "reconstructed_gross_margin",
                "reported_gross_margin_decimal",
                "margin_reconciliation_difference",
            ]
        ]
    )

    # Margin decomposition: mix effect

    base_year = 2023
    end_year = 2025

    base_row = df.loc[df["year"] == base_year].iloc[0]
    end_row = df.loc[df["year"] == end_year].iloc[0]

    mix_effects = {}

    for segment in segment_columns:
        mix_change = (
            end_row[f"{segment}_revenue_mix"]
            - base_row[f"{segment}_revenue_mix"]
        )

        base_margin = base_row[f"{segment}_margin"]

        mix_effects[segment] = (
            mix_change * base_margin
        )

    print("\n2023 TO 2025 MIX EFFECT")
    for segment, effect in mix_effects.items():
        print(f"{segment}: {effect * 100:.2f} percentage points")

    total_mix_effect = sum(mix_effects.values())

    print(
        f"Total Mix Effect: {total_mix_effect * 100:.2f} percentage points"
    )

        # Margin decomposition: within-segment effect

    within_segment_effects = {}

    for segment in segment_columns:
        margin_change = (
            end_row[f"{segment}_margin"]
            - base_row[f"{segment}_margin"]
        )

        base_mix = base_row[f"{segment}_revenue_mix"]

        within_segment_effects[segment] = (
            base_mix * margin_change
        )

    print("\n2023 TO 2025 WITHIN-SEGMENT EFFECT")
    for segment, effect in within_segment_effects.items():
        print(f"{segment}: {effect * 100:.2f} percentage points")

    total_within_segment_effect = sum(
        within_segment_effects.values()
    )

    print(
        f"Total Within-Segment Effect: "
        f"{total_within_segment_effect * 100:.2f} percentage points"
    )

    # Margin decomposition: interaction effect

    interaction_effects = {}

    for segment in segment_columns:
        mix_change = (
            end_row[f"{segment}_revenue_mix"]
            - base_row[f"{segment}_revenue_mix"]
        )

        margin_change = (
            end_row[f"{segment}_margin"]
            - base_row[f"{segment}_margin"]
        )

        interaction_effects[segment] = (
            mix_change * margin_change
        )

    print("\n2023 TO 2025 INTERACTION EFFECT")
    for segment, effect in interaction_effects.items():
        print(f"{segment}: {effect * 100:.2f} percentage points")

    total_interaction_effect = sum(
        interaction_effects.values()
    )

    print(
        f"Total Interaction Effect: "
        f"{total_interaction_effect * 100:.2f} percentage points"
    )

    # Margin decomposition: amortization effect

    base_amortization_effect = base_row["amortization_margin_effect"]
    end_amortization_effect = end_row["amortization_margin_effect"]

    amortization_change_effect = (
        base_amortization_effect
        - end_amortization_effect
    )

    print("\n2023 TO 2025 AMORTIZATION EFFECT")
    print(
        f"Amortization Effect: "
        f"{amortization_change_effect * 100:.2f} percentage points"
    )

    # Final margin decomposition summary

    decomposition_summary = pd.DataFrame(
        {
            "effect": [
                "Mix Effect",
                "Within-Segment Effect",
                "Interaction Effect",
                "Amortization Effect",
            ],
            "percentage_points": [
                total_mix_effect * 100,
                total_within_segment_effect * 100,
                total_interaction_effect * 100,
                amortization_change_effect * 100,
            ],
        }
    )

    decomposition_summary.loc[len(decomposition_summary)] = {
        "effect": "Total Explained Margin Change",
        "percentage_points": decomposition_summary[
            "percentage_points"
        ].sum(),
    }

    observed_margin_change = (
        end_row["gross_margin_pct"]
        - base_row["gross_margin_pct"]
    )

    decomposition_summary.loc[len(decomposition_summary)] = {
        "effect": "Observed Gross Margin Change",
        "percentage_points": observed_margin_change,
    }

    print("\n2023 TO 2025 MARGIN DECOMPOSITION SUMMARY")
    print(decomposition_summary)

    # Margin decomposition visualization

    chart_data = decomposition_summary.iloc[:4]

    plt.figure()

    plt.bar(
        chart_data["effect"],
        chart_data["percentage_points"],
    )

    plt.title("Toast 2023–2025 Gross Margin Decomposition")
    plt.xlabel("Driver")
    plt.ylabel("Margin Impact (Percentage Points)")

    plt.xticks(rotation=20)

    plt.tight_layout()

    plt.savefig(
        Path(__file__).resolve().parents[1]
        / "deliverables"
        / "charts"
        / "gross_margin_decomposition.png",
        dpi=150,
    )

    plt.show()

if __name__ == "__main__":
    main()
