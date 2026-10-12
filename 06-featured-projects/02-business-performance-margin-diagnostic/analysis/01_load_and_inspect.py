from pathlib import Path

import pandas as pd


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

    output_path = (
        Path(__file__).resolve().parents[1]
        / "data"
        / "processed"
        / "toast_financials_2023_2025_processed.csv"
    )

    df.to_csv(output_path, index=False)

    print(f"\nProcessed dataset saved to: {output_path}")    

if __name__ == "__main__":
    main()
