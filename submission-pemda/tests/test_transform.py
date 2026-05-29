from utils.transform import transform_data
import pandas as pd

def test_transform_data_success():
    raw_data = [
        {'Title': 'T-shirt', 'Price': '$10.00', 'Rating': '4.5 / 5', 'Colors': '3 Colors', 'Size': 'Size: M', 'Gender': 'Gender: Men'},
        {'Title': 'Unknown Product', 'Price': 'Price Unavailable', 'Rating': 'Invalid Rating / 5', 'Colors': 'None', 'Size': 'None', 'Gender': 'None'}
    ]
    df = transform_data(raw_data)
    assert df is not None
    assert len(df) == 1
    assert df.iloc[0]['Price'] == 160000.0

def test_transform_data_error():
    df = transform_data(None)
    assert df is None
