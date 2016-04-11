from pandas import DataFrame, Series
from pandas.tseries.index import DatetimeIndex

import astral


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

def descriptor_parameters(descriptor):
    """Returns a dictionary of parameters to be passed to a data calculation function.

    Namely `type` is not a parameter, so remove it. (This could be redesigned)
    """
    return {
        key: value
        for key, value in descriptor.items()
        if key != 'type'
    }

def _high_temperature_data(date_range: DatetimeIndex,
                           city: None) -> Series:
    # todo razzi
    raise NotImplementedError


def _get_close_price(date_range, symbol='') -> Series:
    # todo jon
    raise NotImplementedError


def _moon_phase(date_range: DatetimeIndex) -> Series:
    almanac = astral.Astral()

    return Series([
        almanac.moon_phase(date)
        for date in date_range
    ], index=date_range)

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
        'high_temperature': _high_temperature_data,
        'moon_phase': _moon_phase
    }

    # refactor

    """
    input: {'the_moon_phase': {'type': 'moon_phase'}}

    input.keys() -> ['the_moon_phase']
    input.values() -> [{'type': 'moon_phase'}]

    for val in values:
        identifier = val['type'] -> 'moon_phase'
        fn = data_functions[identifier] -> _moon_phase

        output_data = fn(date_range) -> _moon_phase(date_range)
         -> Series(14, 16, 17)
        return output_data
    """

    return DataFrame({
        identifier: data_functions[descriptor['type']](
            date_range, **descriptor_parameters(descriptor)
        ) for identifier, descriptor in data_descriptors.items()
    }, index=date_range)


def calculate_indicators(input_df, indicator_names) -> DataFrame:
    pass


def evaluate_strategy(indicators_df, strategy) -> Series:
    pass
