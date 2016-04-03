from pandas import DataFrame, Series


class Strategy():
    pass


def get_data(symbol, data_names, start_date, end_date=None) -> DataFrame:
    pass


def calculate_indicators(input_df, indicator_names) -> DataFrame:
    pass


def evaluate_strategy(indicators_df, strategy) -> Series:
    pass
