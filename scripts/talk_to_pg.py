from utils import add_parent_path
add_parent_path()

from onehabit import OneHabitDatabase

def create_tables():
    schema_filepath = "../src/data/schema.sql"
    with open(schema_filepath, "r") as schema:
        create_tables_sql = schema.read()
    
    ohdb = OneHabitDatabase()
    with ohdb.connect() as cursor:
        cursor.execute(create_tables_sql)

def display_schema():
    query = """
    select table_name, column_name, data_type
    from information_schema.columns
    where table_schema = 'dev'
    order by table_name desc, column_name desc;
    """

    ohdb = OneHabitDatabase()
    with ohdb.connect() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
        for result in results:
            print(result)

if __name__ == "__main__":
    # query = """
    # ALTER TABLE dev.responses 
        # ADD COLUMN type text CHECK(type IN ('habit', 'observation'));
    # """

    display_schema()

    # ohdb = OneHabitDatabase()
    # with ohdb.connect() as cursor:
        # cursor.execute(query)
        # results = cursor.fetchall()
        # for result in results:
        #     print(result)