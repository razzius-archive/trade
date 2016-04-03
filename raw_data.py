from datetime import date
import random
import os
import sys

import parsedatetime
# import requests


SF_CITY_ID = 5391959

# http://api.openweathermap.org/data/2.5/box/city?bbox=12,32,15,37,10&cluster=yes&appid=

WUNDERGROUND_API_KEY = os.environ['WUNDERGROUND_API_KEY']



def _get_aapl_close_price(date_range):
    """Uses ystockquote API to get quotes...
    """
    pass

def _get_random_ratio(date_range):
    """Random numbers between 0 and 1."""
    n_days = (date_range[1] - date_range[0]).days
    return [random.random() for _ in range(n_days)]


def _get_sf_high_temperature(date_range):
    """Inputs:
    date(2015, 1, 1)

    outputs:
    [
        33,
        45,
        59
        ...
    ]
    """

def main(date_range, indicators):
    """
    inputs: date range (february 10, 2016 -> february 20, 2016) (default to last 10 days)
            list of indicators (close price, sf temperature)

    outputs:
    [
        2016-2-10: {
            aapl_close_price: 101
        }
        2016-2-11: {
            aapl_close_price: 102
        }
    ]
    """
    indicators_map = {
        'sf_high_temperature': _get_sf_high_temperature,
        'random': _get_random_ratio,
        'aapl_close_price': _get_aapl_close_price
    }

    indicator_values = {
        indicator: indicators_map[indicator](date_range)
        for indicator in indicators
    }

    return indicator_values


if __name__ == '__main__':
    date_text = ' '.join(sys.argv[1:])

    calendar = parsedatetime.Calendar()

    start_date = calendar.parseDT(date_text).date()

    date_range = (start_date, date.today())
    # indicators = ['sf_high_temperature']
    indicators = ['random']

    indicator_values = main(date_range, indicators)
    print(indicator_values)
