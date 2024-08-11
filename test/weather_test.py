# this is the "test/stocks_test.py" file...

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_example():
    assert 2 + 2 == 4

from pandas import DataFrame
from app.weather import display_forecast

def test_data_fetching():
    df = display_forecast("07302")
    assert isinstance(df, DataFrame)
    assert df.columns.tolist() == ['day', 'date', 'temp', 'forecast', 'icon']
    assert geo.place_name == "Jersey City"