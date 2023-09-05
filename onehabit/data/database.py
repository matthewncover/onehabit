import os
from psycopg2 import connect
from dotenv import load_dotenv

from contextlib import contextmanager

class OneHabitDatabase:

    ##HACK
    SCHEMA = "dev"

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

    def get_colnames(self, cursor):
        return [desc[0] for desc in cursor.description]

    def zip_results(self, cursor):
        columns = self.get_colnames(cursor)
        return [dict(zip(columns, x)) for x in cursor.fetchall()]

    # region push

    def push(self, table_name:str, data:dict):

        columns_str = ", ".join(data.keys())
        values_str = ", ".join(["%s"] * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {self.SCHEMA}.{table_name} ({columns_str}) VALUES ({values_str})"

        with self.connect() as cursor:
            cursor.execute(query, values)

    def add_new_user(self, data:dict):
        self.push(table_name="users", data=data)
    
    def add_new_habit(self, data:dict):
        self.push(table_name="habits", data=data)
    
    def add_new_habit_version(self, data:dict):
        self.push(table_name="habits", data=data)

    def add_response(self, data:dict):
        self.push(table_name="responses", data=data)

    def add_observation(self, data:dict):
        self.push(table_name="observations", data=data)

    #endregion
    #region pull

    def pull(self, table_name:str, columns:list=None, 
             condition:str=None, condition_args:tuple=None,
             sorted_condition:str=None, one_record:bool=False):
        
        cols = '*' if columns is None else ', '.join(columns)
        query = f"select {cols} from {self.SCHEMA}.{table_name}"
        if condition is not None:
            query += f" where {condition}"

        if sorted_condition is not None:
            query += f"order by {sorted_condition}"

        with self.connect() as cursor:
            if condition_args is not None:
                cursor.execute(query, condition_args)
            else:
                cursor.execute(query)

            if one_record:
                if columns is not None:
                    return cursor.fetchone()[0] if len(columns) == 1 else dict(zip(columns, cursor.fetchone()))
                else:
                    return dict(zip(self.get_colnames(cursor), cursor.fetchone()))
                
            return self.zip_results(cursor)
    
    def get_user(self, username:str):
        condition = "username = %s"
        return self.pull(
            table_name="users",
            condition=condition,
            condition_args=(username,),
            one_record=True)
    
    def get_habits(self, user_id:str):
        ## TODO
        ## not validated

        query = """
        select  id, version, metadata, user_id, created_date, active, archived
        from    (select *, row_number() over (partition by id order by version desc) as rn
                from habits
                where user_id = %s and archived = false) as sub
        where rn = 1
        """

        with self.connect() as cursor:
            cursor.execute(query, (user_id,))
            return self.zip_results(cursor)

    def get_password_hash(self, username:str):
        condition = "username = %s"
        return self.pull(
            table_name="users",
            columns=["password_hash"],
            condition=condition,
            condition_args=(username,),
            one_record=True).tobytes()
        
    #endregion
    #region update

    def update(self, table_name: str, data:dict, condition:str, condition_args:tuple):
        set_clause = ", ".join([f"{column} = %s" for column in data.keys()])
        query = f"update {self.SCHEMA}.{table_name} set {set_clause} where {condition}"

        with self.connect() as cursor:
            cursor.execute(query, (*data.values(), *condition_args))

    def update_response(self, response_id, data):
        condition = "id = %s"
        return self.update(
            table_name = "responses",
            data = data,
            condition = condition,
            condition_args=(response_id,))

    #endregion