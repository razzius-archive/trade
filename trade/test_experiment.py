import datetime

import pandas as pd
from pandas.tseries.index import DatetimeIndex

from experiment import get_data, calculate_indicators, evaluate_strategy


APRIL_1_2016_DATERANGE = pd.date_range(start=datetime.date(2016, 4, 1), periods=1)

FIRST_WEEK_IN_APRIL = pd.date_range(start=datetime.date(2016, 4, 1), periods=7)


def test_get_sf_high_temperature():
    """High temperature for SF was 59 degrees Fahrenheit on April 1, 2016."""
    temperature_df = get_data({'sf_temperature': {'type': 'high_temperature'}}, APRIL_1_2016_DATERANGE)

    assert temperature_df.columns == ['sf_temperature']
    assert len(temperature_df.columns) == 1

    assert temperature_df['sf_temperature'].iloc[0] == 59


def test_get_boston_high_temperature():
    """High temperature for Boston was 69 degrees Fahrenheit on April 1, 2016."""
    temperature_df = get_data({'boston_temperature': {'type': 'high_temperature'}}, APRIL_1_2016_DATERANGE)

    assert temperature_df.columns == ['boston_temperature']
    assert len(temperature_df.columns) == 1

    assert temperature_df['boston_temperature'].iloc[0] == 69


def test_get_apple_close_price_data():
    """Apple close price for April 1, 2016 was $109.99."""
    close_price_descriptor = {
        'type': 'close',
        'symbol': 'AAPL',
    }

    close_price_df = get_data({'apple_close': close_price_descriptor}, APRIL_1_2016_DATERANGE)

    value = close_price_df['close'].iloc[0]

    assert value == 109.99


def test_get_amazon_high_price():
    """High price for amazon on 2016-04-01 was ???"""
    close_price_descriptor = {
        'type': 'close',
        'symbol': 'AAPL',
    }

    close_price_df = get_data({'apple_close': close_price_descriptor}, APRIL_1_2016_DATERANGE)
    value = close_price_df['close'].iloc[0]

    # TODO find value


def test_get_multiple_data_sources():
    """Query historical temperatures for different cities."""
    metrics = {
        'sf_temperature': {'type': 'temperature', 'value': 'high_temperature', 'city': 'San Francisco'},
        'boston_temperature': {'type': 'temperature', 'value': 'high_temperature', 'city': 'Boston'}
    }

    df = get_data(metrics, APRIL_1_2016_DATERANGE)

    # TODO find values


def test_get_close_data_for_range():
    """Apple close data for the week of April 1 to April 8."""
    close_price_descriptor = {
        'type': 'close',
        'symbol': 'AAPL',
    }

    close_price_df = get_data({'apple_close': close_price_descriptor}, FIRST_WEEK_IN_APRIL)

    # TODO find values
