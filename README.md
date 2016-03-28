## data

An indicator that has no data dependencies.
(somewhere we will store the data sources available)

input : close,volume last 3 days
output : 3 days of apple close and volume


```python
# input = 'previous year'

# note : could be ordereddict
output = OrderedDict([
    ('2015-01-01', {'close': 100, 'volume': 1000}),
    ('2015-01-02', {'close': 110, 'volume': 1100})
])
```


## indicator

indicator :: [data_record] -> [value]
(need to store the indicators available)


1. close price over volume

```python
input: (raw data), (indicator parameters)
close price / volume

@indicator_requires('data.close', 'data.volume')
def close_price_over_volume(data):
    return [
        point['close'] / point['volume']
        for point in data
    ]
```

2. n day moving average of close price over volume

```
@indicator_requires('indicator.close_price_over_volume')
def n_day_moving_average_of_close_price_over_volume(n_days, data):
    if len(data) < n_days:
        raise ValueError('Need more data: {} < {}'
                         .format(len(data), n_days)
    averages = []

    for point in data:
        window = _
        average = _
        averages.append(average)

    return averages
```

3. close price

## strategy
inputs: indicators, inventory

this is an ok strategy
(1: indicator 1; 3: indicator 3)
'1 < 3': sell
'1 = 3': hold
'1 > 3': buy

this is a more interesting strategy
If you don't have stock and 1 < 3, hold.
If you don't have stock and 1 > 3, buy.
If you do have stock and 1 < 3, sell.
If you do have stock and 1 > 3, hold.

```python
# inputs
# - indicators
    OrderedDict([
        ('2015-01-01', {'close_price': 100, '9_day_moving_average_of_close_price': 60}),
        ('2015-01-02', {'close_price': 110, '9_day_moving_average_of_close_price': 61}),
    ])

# - inventory
    {
        'aapl': 3
    }

# outputs

[
    ('2015-01-01': [{'action': 'BUY', 'target': 'AAPL': 'quantity': 100}]),
    ('2015-01-02': [{'action': 'BUY', 'target': 'AAPL': 'quantity': 100}]),
    ('2015-01-03': [])
]
```

## portfolio

tracks what our inventory is over time
inputs: inventory, decisions
outputs: stock in our portfolio for each point in time

```
# inputs
decision

"buy 10 apple shares on feb 11
then sit on it forever"

[
    ('2015-01-01': [{'action': 'BUY', 'target': 'AAPL': 'quantity': 10}],
    ('2015-01-02': [],
    ('2015-01-03': [],
    ...

starting inventory

{'AAPL': 0}

# outputs

[
    ('2015-01-01': {'AAPL': 0}),
    ('2015-01-02': {'AAPL': 10}),
    ('2015-01-03': {'AAPL': 10})
]
```


# Interfaces

## run experiment
bot, cli

- stock(s)
- time range
- strategy (defines indicators)
? starting balance
? starting portfolio

Retrieve all data for the time range.

```
def get_data(symbol, sources, start_date, end_date=None) -> DataFrame:
    """inputs 'aapl', ['close'], 2015-01-01

    returns DataFrame([
      {'close': 1},
      {'close': 2},
    ], index=[2015-01-01, 2015-01-02])

    """
```

Calculate all indicators for each time step.

TODO

Evaluate the strategy for each time step.

TODO

Outputs: time series of actions, final result

## start experiment
bot

- stock(s)
- strategy

### step experiments
cron

## stop experiment (experiment_id)
bot

## list experiments
bot, cli

## list experiment (experiment_id)
bot, cli

## show portfolio (experiment_id)
bot, cli

*TODO transition to pandas.DataFrame*
