from utils import TestUtils
TestUtils.add_parent_path()

from sqlalchemy import text

from onehabit.data import ohdb

if __name__ == "__main__":
    query = text("""
                 """)

    with ohdb.session_maker() as session:
        session.execute(query)
        session.commit()

    pass