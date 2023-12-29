import os, datetime as dt
from typing import List, Union, Type
from dotenv import load_dotenv

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import OperationalError

from onehabit.utils import DevUtils

SA_BASE = declarative_base()

# def operational_error_handler(

class OneHabitDatabase:

    def __init__(self):
        load_dotenv()
        self._engine = None
        self._session_maker = None

    @property
    def engine(self):
        if not self._engine:
            self._engine = self._create_engine()
        return self._engine
    
    @property
    def session_maker(self):
        if not self._session_maker:
            self._session_maker = sessionmaker(bind=self.engine)
        return self._session_maker

    def _create_engine(self):
        username    = os.getenv('DATABASE_USERNAME')
        password    = os.getenv('DATABASE_PASSWORD')
        host        = os.getenv('HOST_IP')
        db_name     = os.getenv('DATABASE_NAME')

        return sa.create_engine(f"postgresql+psycopg2://{username}:{password}@{host}/{db_name}")

    def add(self, records: Union[SA_BASE, List[SA_BASE]]) -> List[int]:
        records = DevUtils.assert_as_list(records)

        with self.session_maker() as session:
            session: Session
            session.add_all(records)
            session.commit()

            ids = [record.id for record in records]

        return ids
    
    def update(self, records: Union[SA_BASE, List[SA_BASE]]) -> List[int]:
        records = DevUtils.assert_as_list(records)

        with self.session_maker() as session:
            for record in records:
                record.modified_at = dt.datetime.utcnow()
                session.merge(record)

            session.commit()

            ids = [record.id for record in records]

        return ids

    def pull(self, sa_model: Type[SA_BASE], *filters:list, 
             order_by:str=None, limit:int=None) -> List[SA_BASE]:
        
        with self.session_maker() as session:
            query = session.query(sa_model).filter(*filters)

            if order_by is not None:
                query = query.order_by(order_by)

            if limit is not None:
                query = query.limit(limit)

            records = query.all()

        return records
    
    def delete(self, records: Union[SA_BASE, List[SA_BASE]]) -> None:
        records = DevUtils.assert_as_list(records)

        with self.session_maker() as session:
            for record in records:
                session.delete(record)

            session.commit()
