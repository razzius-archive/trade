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

1. Retrieve all data for the time range.

```python
def get_data(symbol, data_names, start_date, end_date=None) -> DataFrame:
    """inputs 'aapl', ['close'], 2015-01-01

    returns DataFrame([
      {'close': 1},
      {'close': 2},
    ], index=[2015-01-01, 2015-01-02])

    Can call external APIs, read from database, calculate random numbers...
    if I pass in ['sf_temp']
        -> somehow get the SF temp data
    """
    output = DataFrame()

    for data_name in data_names:
        if data_name == 'sf_temp':
            output['sf_temp'] = request_weatherbug_weather_data('sf')
        elif data_name == 'boston_temp':
            output['boston_temp'] = request_weatherbug_weather_data('boston')

    return output
```

Calculate all indicators for each time step.

```python
def calculate_indicators(input_df, indicator_names) -> DataFrame:
    """inputs *df*, ['Basic MACD (26-day 12-day, 9-day)', 'Moving average of high price', 'SF temp / boston temp']
                    -> close price 						-> high price			-> sf temperature, boston temp
 -> data_names becomes ['close', 'high', 'sf_temp', 'boston_temp']

    1. (26-day exponential moving average)| (9-day exponential moving average)

    returns DataFrame
    """
```

Evaluate the strategy for each time step.

```python
def evaluate_strategy(indicators_df, strategy) -> Series:
    """
                TimeSeries
    2012-x-1	{'action': 'sell 10 apple stock'}
    2012-x-2	{'action': 'buy 10 apple stock'}
    2012-x-3	{'action': 'sell 10 apple stock'}
    """
    return strategy.execution_function(indicators_df)

```



```python
class Strategy():
    """Define a strategy that can be tested in an experiment"""
    def __init__(self, name, indicators, execution_function):
        self.name = name
        self.indicators = indicators
        self.execution_function = execution_function

    def resolve_data_dependencies(self):
        """Return a list of all the raw data names needed for this strategy to be tested."""
        return ???

def resolve_data_dependencies(indicators : List)

def strategy_function(indicators_df) -> Series:
    for ind_value, index in indicators_df:
        if ind_value[0] > ind_value[1]:
            return {'action': 'BUY'}

        if ind_value[0] > ind_value[1]:
            if indicators_df.iloc[index - 1, 0] > ind_value[0]:
                return {'action': 'sell'}


my_strategy = ([-indicators-], -function-)
my_strategy = Strategy(['26-day exp moving average'], strategy_function)

def run_experiment(stock, strategy, time_range):

    data_df = get_data('AAPL', strategy.resolve_data_dependencies())
    indicator_df = calculate_indicators(data_df, [strategy.indicators])
    action_series = evaluate_strategy(indicator_df, strategy)

    return action_series

actions_1 = run_experiment('AAPL', my_strategy, 'last 2 weeks')
```

Outputs: time series of actions, final result

# Razzi example strategy

Uses the temperature in SF versus Boston. If it's hotter in SF, sell. Otherwise buy.

Indicators:
    sf temp / boston temp
Data dependencies:
    ['sf_temp', 'iowa_temp']


strategy
    -> indicators
        -> data dependencies


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
