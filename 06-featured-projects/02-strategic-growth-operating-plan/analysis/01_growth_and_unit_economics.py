from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]

ANNUAL_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "cava_annual_2023_2025.csv"
)

QUARTERLY_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "cava_quarterly_2026.csv"
)

COST_DATA_PATH = (
    PROJECT_ROOT
    / "data"
    / "raw"
    / "cava_cost_structure_2023_2025.csv"
)


def main() -> None:
    annual_df = pd.read_csv(ANNUAL_DATA_PATH)
    quarterly_df = pd.read_csv(QUARTERLY_DATA_PATH)
    cost_df = pd.read_csv(COST_DATA_PATH)

    # Annual growth calculations
    annual_df["revenue_growth_pct"] = (
        annual_df["revenue_m"]
        .pct_change()
        * 100
    )

    annual_df["restaurant_count_growth_pct"] = (
        annual_df["ending_restaurants"]
        .pct_change()
        * 100
    )

    annual_df["restaurant_margin_change_pp"] = (
        annual_df["restaurant_level_margin_pct"]
        .diff()
    )

    print("\nANNUAL GROWTH & UNIT ECONOMICS")
    print(
        annual_df[
            [
                "year",
                "revenue_m",
                "revenue_growth_pct",
                "ending_restaurants",
                "restaurant_count_growth_pct",
                "net_new_restaurants",
                "same_restaurant_sales_growth_pct",
                "auv_m",
                "restaurant_level_margin_pct",
                "restaurant_margin_change_pp",
            ]
        ].to_string(index=False)
    )

    print("\n2026 QUARTERLY OPERATING TREND")
    print(
        quarterly_df[
            [
                "quarter",
                "revenue_m",
                "ending_restaurants",
                "net_new_restaurants",
                "same_restaurant_sales_growth_pct",
                "traffic_growth_pct",
                "auv_m",
                "restaurant_level_margin_pct",
            ]
        ].to_string(index=False)
    )

    print("\n2023 TO 2025 CHANGE")

    revenue_2023 = annual_df.loc[
        annual_df["year"] == 2023,
        "revenue_m",
    ].iloc[0]

    revenue_2025 = annual_df.loc[
        annual_df["year"] == 2025,
        "revenue_m",
    ].iloc[0]

    restaurants_2023 = annual_df.loc[
        annual_df["year"] == 2023,
        "ending_restaurants",
    ].iloc[0]

    restaurants_2025 = annual_df.loc[
        annual_df["year"] == 2025,
        "ending_restaurants",
    ].iloc[0]

    same_store_2023 = annual_df.loc[
        annual_df["year"] == 2023,
        "same_restaurant_sales_growth_pct",
    ].iloc[0]

    same_store_2025 = annual_df.loc[
        annual_df["year"] == 2025,
        "same_restaurant_sales_growth_pct",
    ].iloc[0]

    margin_2023 = annual_df.loc[
        annual_df["year"] == 2023,
        "restaurant_level_margin_pct",
    ].iloc[0]

    margin_2025 = annual_df.loc[
        annual_df["year"] == 2025,
        "restaurant_level_margin_pct",
    ].iloc[0]

    print(
        f"Revenue: ${revenue_2023:.1f}M "
        f"to ${revenue_2025:.1f}M"
    )

    print(
        f"Restaurants: {restaurants_2023} "
        f"to {restaurants_2025}"
    )

    print(
        f"Same-Restaurant Sales Growth: "
        f"{same_store_2023:.1f}% "
        f"to {same_store_2025:.1f}%"
    )

    print(
        f"Restaurant-Level Margin: "
        f"{margin_2023:.1f}% "
        f"to {margin_2025:.1f}%"
    )

    # Merge annual operating data with cost structure data
    combined_df = annual_df.merge(
        cost_df,
        on="year",
        how="left",
    )

    # Corporate operating leverage
    combined_df["g_and_a_pct_revenue"] = (
        combined_df["g_and_a_m"]
        / combined_df["revenue_m"]
        * 100
    )

    combined_df["operating_margin_pct"] = (
        combined_df["operating_income_m"]
        / combined_df["revenue_m"]
        * 100
    )

    # Growth-cost efficiency
    combined_df["pre_opening_cost_per_new_restaurant_m"] = (
        combined_df["pre_opening_costs_m"]
        / combined_df["net_new_restaurants"]
    )

    combined_df["capex_per_new_restaurant_m"] = (
        combined_df["capex_m"]
        / combined_df["net_new_restaurants"]
    )

    print("\nGROWTH COST & OPERATING LEVERAGE")
    print(
        combined_df[
            [
                "year",
                "g_and_a_m",
                "g_and_a_pct_revenue",
                "pre_opening_costs_m",
                "pre_opening_cost_per_new_restaurant_m",
                "capex_m",
                "capex_per_new_restaurant_m",
                "operating_income_m",
                "operating_margin_pct",
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":
    main()