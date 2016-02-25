import datetime
import os
import sys

from sqlalchemy import create_engine

import ystockquote

from schema import exchanges, companies, quotes


def parse_date(s):
    return datetime.datetime.strptime(s, '%Y-%m-%d')


def main(engine, exchange, symbol):
    connection = engine.connect()

    exchange_id, = connection.execute(
        (
            exchanges.insert()
            .returning(exchanges.c.id)
        ),
        {
            'name': exchange
        }
    ).fetchone()

    company_id, = connection.execute(
        (
            companies.insert()
            .returning(companies.c.id)
        ),
        {
            'symbol': symbol,
            'exchange_id': exchange_id
        }
    ).fetchone()

    stock_quotes = ystockquote.get_historical_prices(symbol, '1013-01-03', '2017-01-08')
    quote_entries = [
        {
            'date': parse_date(k),
            'open': v['Close'],
            'close': v['Close'],
            'adjusted_close': v['Adj Close'],
            'high': v['High'],
            'low': v['Low'],
            'volume': v['Volume'],
            'company_id': company_id
        } for k, v in stock_quotes.items()
    ]

    connection.execute(
        quotes.insert(),
        quote_entries
    )


if __name__ == '__main__':
    engine = create_engine(os.environ['DATABASE_URL'])
    exchange = sys.argv[1]
    symbol = sys.argv[2]
    main(engine, exchange, symbol)
