import sqlite3

import pandas as pd


DATABASE_PATH = "banking.db"


connection = sqlite3.connect(DATABASE_PATH)


with open("sql/analysis.sql", "r") as file:
    sql_script = file.read()


# Split individual SQL statements
queries = [
    query.strip()
    for query in sql_script.split(";")
    if query.strip()
]


for number, query in enumerate(queries, start=1):

    print("\n" + "=" * 70)
    print(f"QUERY {number}")
    print("=" * 70)

    try:
        result = pd.read_sql_query(
            query,
            connection,
        )

        print(result.to_string(index=False))

    except Exception as error:
        print(f"Error: {error}")


connection.close()