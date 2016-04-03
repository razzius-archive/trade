import datetime

from experiment import get_data, calculate_indicators, evaluate_strategy


def test_get_data():
    """Close price should come back as a float."""
    close_price_df = get_data('AAPL', ['close'], datetime.date.today(), datetime.date.today())
    value = close_price_df['close'].iloc[0]
    assert isinstance(value, float)
