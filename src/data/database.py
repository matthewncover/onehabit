import os
from psycopg2 import connect
from dotenv import load_dotenv

from contextlib import contextmanager

class GoalTrackingDatabase:

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
            password = os.getenv("DATABASE_PASSWORD")
        )

    def create_tables(self):
        ## HACK

        schema_filepath = "./src/data/schema.sql"
        with open(schema_filepath, "r") as schema:
            create_tables_sql = schema.read()
        
        with self.connect() as cursor:
            cursor.execute(create_tables_sql)
            self.connection.commit()

    ## TODO
    ## push
    ## _setup_push
    ## function to create new user
    ## function to create new goal
    ## function to create new goal version
    ## function to add daily response
    ##
    ## pull
    ## _setup_pull
    ## function to pull the configs of the newest versions of all active goals
    ## 
    ## update
    ## function to update response for a given day
    ##
    ## other
    ## function for whether a user exists
    

    def push(self, table_name:str, data:dict):

        columns_str = ", ".join(data.keys())
        values_str = ", ".join(["%s"] * len(data))
        values = tuple(data.values())

        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"

        with self.connect() as cursor:
            cursor.execute(query, values)
            self.connection.commit()

    def pull(self, table_name:str, condition:str=None):

        query = f"SELECT * FROM {table_name}"
        if condition is not None:
            query += f" WHERE {condition}"

        with self.connect() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def get_password(self, username:str):
        query = f"select password_hash from users where username = '{username}'"

        with self.connect() as cursor:
            cursor.execute(query)
            return cursor.fetchone()
        
if __name__ == "__main__":
    gtdb = GoalTrackingDatabase()
    gtdb.create_tables()