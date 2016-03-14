## data
(somewhere we will store the data sources available)

input : last 3 days
output : 3 days of apple close prices


```python
# input = 'previous year'

# note : could be ordereddict
output = OrderedDict([
    ('2015-01-01', {'close_price': 100, 'volume': 1000}),
    ('2015-01-02', {'close_price': 110, 'volume': 1100})
])
```


## indicator line
(need: somewhere we will store the indicators available)

1. close price over volume

```python
input: (raw data), (indicator parameters)
close price / volume

```

2. nine day moving average of close price over volume


3. close price

indicators
(bundles of indicator lines

a. uses #1 and #3
b. uses #2 and #3


strategy
inputs: indicators, inventory

this is an ok strategy
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
