import os
from matplotlib import table
from psycopg2 import connect
from dotenv import load_dotenv

from contextlib import contextmanager

class OneHabitDatabase:

    def __init__(self):
        load_dotenv()

    @contextmanager
    def connect(self):
        self._connect()
        cursor = self.connection.cursor()
        try:
            yield cursor
        finally:
            self.connection.close()
    
    def _connect(self):
        self.connection = connect(
            host = os.getenv("HOST_IP"),
            database = os.getenv("DATABASE_NAME"),
            user = os.getenv("DATABASE_USERNAME"),
            password = os.getenv("DATABASE_PASSWORD"))

        self.connection.autocommit = True

    def create_tables(self):
        ## HACK

        schema_filepath = "./src/data/schema.sql"
        with open(schema_filepath, "r") as schema:
            create_tables_sql = schema.read()
        
        with self.connect() as cursor:
            cursor.execute(create_tables_sql)

    # region push

    def push(self, table_name:str, data:dict):

        columns_str = ", ".join(data.keys())
        values_str = ", ".join(["%s"] * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"

        with self.connect() as cursor:
            cursor.execute(query, values)

    @classmethod
    def add_new_user(cls, data:dict):
        cls.push(table_name="users", data=data)
    
    @classmethod
    def add_new_goal(cls, data:dict):
        cls.push(table_name="goals", data=data)
    
    @classmethod
    def add_new_goal_version(cls):
        raise NotImplementedError
    
    @classmethod
    def add_response(cls, response_data:dict):
        raise NotImplementedError

    #endregion
    #region pull

    def pull(self, table_name:str, columns:list=None, 
             condition:str=None, condition_args:tuple=None,
             sorted_condition:str=None, one_record:bool=False):
        
        cols = '*' if columns is None else ', '.join(columns)
        query = f"select {cols} from {table_name}"
        if condition is not None:
            query += f" where {condition}"

        if sorted_condition is not None:
            query += f"order by {sorted_condition}"

        with self.connect() as cursor:
            cursor.execute(query)

            if one_record:
                return dict(zip(columns, cursor.fetchone()))
            return [dict(zip(columns, x)) for x in cursor.fetchall()]
    
    @classmethod
    def get_user(cls, username:str):
        condition = "username = %s"
        return cls.pull(
            table_name="users",
            condition=condition,
            condition_args=(username,),
            one_record=True)
    
    @classmethod
    def get_goals(cls, user_id:str):
        condition = "user_id = %s and archived = false"
        return cls.pull(
            table_name="goals",
            condition=condition,
            condition_args=(user_id,),
            sorted_condition="user_id, goal_id, goal_version asc")
    
    @classmethod
    def get_password_hash(cls, username:str):
        condition = "username = %s"
        return cls.pull(
            table_name="users",
            columns="password_hash",
            condition=condition,
            condition_args=(username,),
            one_record=True)
        
    #endregion
    #region update

    def update(self, table_name: str, data:dict, condition:str, condition_args:tuple):

        set_clause = ", ".join([f"{column} = %s" for column in data.keys()])
        query = f"update {table_name} set {set_clause} where {condition}"

        with self.connect() as cursor:
            cursor.execute(query, (*data.values(), *condition_args))

    @classmethod
    def update_response(cls, response_id):
        raise NotImplementedError

    #endregion