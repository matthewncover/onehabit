import os
from psycopg2 import connect
from dotenv import load_dotenv

class GoalsDataBase:

    def __init__(self):
        pass

    def connect(self, secrets):
        self.conn = connect(
            host = secrets["HOST_IP"],
            database = secrets["DATABASE_NAME"],
            user = secrets["DATABASE_USERNAME"],
            password = secrets["DATABASE_PASSWORD"]
        )

        self.cursor = self.conn.cursor()
        print(f"connected to {os.getenv('DATABASE_NAME')}")

    def push(self, table_name:str, data:dict):

        columns_str = ", ".join(data.keys())
        values_str = ", ".join(["%s"] * len(data))

        query = f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"

        try:
            self.cursor.execute(query, tuple(data.values()))
            self.conn.commit()
            print(f"Records inserted successfully into {table_name} table")

        except Exception as error:
            self.conn.rollback()
            print(f"Failed to insert into database. {error}")

    def pull(self, table_name:str, condition:str=None):

        query = f"SELECT * FROM {table_name}"
        if condition is not None:
            query += f" WHERE {condition}"

        try:
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            for row in rows:
                print(row)

        except Exception as error:
            print(f"Failed to retrieve from database. {error}")
    


