from pandas import DataFrame, Series
from pandas.tseries.index import DatetimeIndex


# class DataDescriptor():
#     """A description of a raw data value to be calculated.

#     Encapsulates the identifier as well as any arguments used
#     to parameterize the calculation.
#     """
#     def __init__(self, identifier, **parameters):
#         self.identifier = identifier
#         self.parameters = parameters

class Strategy():
    pass


# classes of metrics
# - depend on symbol or not
# - parameterized or not

# temperature_data = Metric(stock_related=False, parametrized=True)

# ? stock_metric
# ? city is repeated here
# @metric('temperature', required_parameters=['city'])
# def _get_temperature_data(date_range: DateTimeIndex,
#                           city) -> Series:
#     # todo razzi
#     raise NotImplementedError

# temperature_data.execute

def _get_temperature_data(date_range: DatetimeIndex) -> Series:
    # todo razzi
    raise NotImplementedError


def _get_close_price(date_range, symbol='') -> Series:
    # todo jon
    raise NotImplementedError

# for example
# sf_temperature =('temperature', {'city': 'San Francisco'})
# sf_temperature = DataDescriptor('temperature', city='San Francisco')
# get_data('aapl', ['close', sf_temperature])


def get_data(data_descriptors: dict,
             date_range: DatetimeIndex) -> DataFrame:
    """TODO document
    """
    data_functions = {
        'close': _get_close_price,
        'high_temperature': _get_temperature_data
    }

    # TODO pass params
    # refactor

    return DataFrame({
        identifier: data_functions[descriptor['type']](date_range, **descriptor)
        for identifier, descriptor in data_descriptors.values()
    })


def calculate_indicators(input_df, indicator_names) -> DataFrame:
    pass


def evaluate_strategy(indicators_df, strategy) -> Series:
    pass
