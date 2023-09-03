import os
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

    def zip_results(self, cursor):
        columns = [desc[0] for desc in cursor.description]
        return [dict(zip(columns, x)) for x in cursor.fetchall()]

    # region push

    def push(self, table_name:str, data:dict):

        columns_str = ", ".join(data.keys())
        values_str = ", ".join(["%s"] * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"

        with self.connect() as cursor:
            cursor.execute(query, values)

    def add_new_user(self, data:dict):
        self.push(table_name="users", data=data)
    
    def add_new_goal(self, data:dict):
        self.push(table_name="goals", data=data)
    
    def add_new_goal_version(self, data:dict):
        self.push(table_name="goals", data=data)

    def add_response(self, data:dict):
        self.push(table_name="response", data=data)

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
            if condition_args is not None:
                cursor.execute(query, condition_args)
            else:
                cursor.execute(query)

            if one_record:
                if len(columns) == 1:
                    return cursor.fetchone()[0]
                else:
                    return dict(zip(columns, cursor.fetchone()))
            return self.zip_results(cursor)
    
    def get_user(self, username:str):
        condition = "username = %s"
        return self.pull(
            table_name="users",
            condition=condition,
            condition_args=(username,),
            one_record=True)
    
    def get_goals(self, user_id:str):
        query = """
        select  goal_id, goal_version, user_id, created_date, active, archived
        from    (select *, row_number() over (partition by goal_id order by goal_version desc) as rn
                from goals
                where user_id = %s and archived = false) as sub
        where rn = 1
        """

        with self.connect() as cursor:
            cursor.execute(query, (user_id,))
            return self.zip_results(cursor)

        # condition = "user_id = %s and archived = false"
        # return cls.pull(
        #     table_name="goals",
        #     condition=condition,
        #     condition_args=(user_id,),
        #     sorted_condition="user_id, goal_id, goal_version asc")
    
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
        query = f"update {table_name} set {set_clause} where {condition}"

        with self.connect() as cursor:
            cursor.execute(query, (*data.values(), *condition_args))

    def update_response(self, response_id):
        raise NotImplementedError

    #endregion