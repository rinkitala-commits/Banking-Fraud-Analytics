import sqlite3

import pandas as pd


DATABASE_PATH = "banking.db"


connection = sqlite3.connect(DATABASE_PATH)


with open(
    "sql/advanced_analysis.sql",
    "r"
) as file:

    sql_script = file.read()


queries = [
    query.strip()
    for query in sql_script.split(";")
    if query.strip()
]


for number, query in enumerate(
    queries,
    start=1
):

    print("\n" + "=" * 80)
    print(f"ADVANCED QUERY {number}")
    print("=" * 80)

    try:

        result = pd.read_sql_query(
            query,
            connection
        )

        print(
            result.head(20).to_string(
                index=False
            )
        )

    except Exception as error:

        print(f"Error: {error}")


connection.close()
