"""Transform a small sample of retail sales data."""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "clean_sales.csv"


def build_sample_data() -> pd.DataFrame:
    """Return sample sales data for the example ETL pipeline."""
    return pd.DataFrame(
        {
            "product": ["Notebook", "Pen", "Notebook"],
            "quantity": [2, 5, 1],
            "unit_price": [4.50, 1.25, 4.50],
        }
    )


def transform_sales(data: pd.DataFrame) -> pd.DataFrame:
    """Add a total column to sales data."""
    result = data.copy()
    result["total"] = result["quantity"] * result["unit_price"]
    return result


def main() -> None:
    """Run the sample pipeline and save its processed output."""
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    processed_data = transform_sales(build_sample_data())
    processed_data.to_csv(OUTPUT_PATH, index=False)
    print(f"Wrote {len(processed_data)} rows to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()