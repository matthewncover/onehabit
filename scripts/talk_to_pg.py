import sys, os
parent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(parent_dir, '..'))

from src.data.database import OneHabitDatabase

def create_tables(self):
    ## HACK

    schema_filepath = "../src/data/schema.sql"
    with open(schema_filepath, "r") as schema:
        create_tables_sql = schema.read()
    
    with ohdb.connect() as cursor:
        cursor.execute(create_tables_sql)

if __name__ == "__main__":
    query = "alter table goals add column archived boolean not null default false"

    ohdb = OneHabitDatabase()
    with ohdb.connect() as cursor:
        cursor.execute(query)