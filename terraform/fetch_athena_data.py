import awswrangler as wr
import pandas as pd

s3_output = "s3://my-unique-bucket-2024-07-15/"
database = "new_database"
table = "superstore_table"


query = f"SELECT * FROM {table};"

df = wr.athena.read_sql_query(
    sql=query,
    database=database,
    s3_output=s3_output
)

df.to_csv("superstore_data.csv", index=False)
