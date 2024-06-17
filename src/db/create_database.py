import pandas as pd
from sqlalchemy import create_engine, text
import psycopg2

# Path to the downloaded CSV file
csv_file_path = r'/Users/feliciajiang/Documents/AI4Good Lab/FinalProjectAI4Good/Data Processing/Cleaned Data/combined_cleaned.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Database connection settings (replace with your actual details)
db_url = 'postgresql://combineddb_owner:NbVg8dZPUu6e@ep-shiny-poetry-a67zznk9.us-west-2.aws.neon.tech/combineddb'

# Create a SQLAlchemy engine
engine = create_engine(db_url)

# Define the table name
table_name = 'grocery_items'

# Create the table schema in the database
with engine.connect() as conn:
    conn.execute(text(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            Title TEXT,
            Price NUMERIC,
            Category TEXT,
            Store TEXT,
            "Price per Unit" NUMERIC,
            "Per Unit Quantity" NUMERIC,
            "Unit Type" TEXT
        )
    '''))

# Import the DataFrame into the database
df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f'Data imported successfully into table {table_name}')

query = f'SELECT * FROM {table_name} LIMIT 10'
df = pd.read_sql(query, engine)
print(df)
