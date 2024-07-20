import awswrangler as wr
import pandas as pd

# Replace with your actual S3 bucket and database details
s3_output = "s3://my-unique-bucket-2024-07-15/"
database = "new_database"
table = "superstore_table"

# Define the query
#query = f"SELECT * FROM {table};"

# Fetch data from Athena
df = wr.athena.read_sql_query(
    sql=query,
    database=database,
    s3_output=s3_output
)

# Save the data to a CSV file
df.to_csv("superstore_data.csv", index=False)
