import os

from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    MetaData,
    Numeric,
    String,
    Table,
    create_engine
)


metadata = MetaData()


exchanges = Table('exchanges', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('name', String, unique=True, nullable=False))

companies = Table('companies', metadata,
                  Column('id', Integer, primary_key=True),
                  Column('symbol', String, nullable=False),
                  Column('exchange_id', Integer, ForeignKey('exchanges.id'), nullable=False))

quotes = Table('quotes', metadata,
               Column('date', Date, nullable=False),
               Column('open', Numeric(9, 2), nullable=False),
               Column('close', Numeric(9, 2), nullable=False),
               Column('adjusted_close', Numeric(9, 2), nullable=False),
               Column('high', Numeric(9, 2), nullable=False),
               Column('low', Numeric(9, 2), nullable=False),
               Column('company_id', Integer, ForeignKey('companies.id'), nullable=False),
               )

if __name__ == '__main__':
    engine = create_engine(os.environ['DATABASE_URL'])
    metadata.create_all(engine)
