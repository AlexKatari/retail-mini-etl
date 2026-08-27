import pandas as pd

from src.etl import transform_sales


def test_transform_sales_adds_total() -> None:
    data = pd.DataFrame({"quantity": [2], "unit_price": [4.50]})

    result = transform_sales(data)

    assert result["total"].tolist() == [9.0]