import pandas as pd
from sqlalchemy import create_engine, text
from openai_query import generate_category_and_tags

# Path to the downloaded CSV file
csv_file_path = r'filtered_merged_clean.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path)

# Database connection settings (replace with your actual details)
db_url = 'postgresql://neondb_owner:Vl7ibMrf1wWX@ep-purple-cell-a561b2u2.us-east-2.aws.neon.tech/neondb?sslmode=require'

# Create a SQL Alchemy engine
engine = create_engine(db_url)

# Define the table name
table_name = 'groceryitems'

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
            "Unit Type" TEXT,
            "Tags" TEXT
        )
    '''))

# Import the updated DataFrame into the database
df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f'Data imported successfully into table {table_name}')

# item is currently hard coded, should be recieved from the frontend 
input_item = "Apples and pears"
gen_category, gen_tags =  generate_category_and_tags(input_item) 

gen_tags_set = set(gen_tags.split(','))

# Filter the DataFrame to only include rows where the 'Category' column matches the generated category
filtered_df = df[df['Category'] == gen_category]

# Define variations of the input item
variations = [
    input_item.lower(), input_item[:-1].lower(), 
    input_item.capitalize(), input_item[:-1].capitalize(),
    input_item.lower() + "'", input_item[:-1].lower() + "'",
    input_item.capitalize() + "'", input_item[:-1].capitalize() + "'",
    input_item.lower() + "'s", input_item[:-1].lower() + "'s",
    input_item.capitalize() + "'s", input_item[:-1].capitalize() + "'s"
]

# Filter to include rows where the Title contains any variation of the input item
#filtered_df = filtered_df[filtered_df['Title'].apply(lambda title: any(var in title for var in variations))]

# Create a list to store items with their common tag counts
items_with_common_tags = []

for index, row in filtered_df.iterrows():
    item_title = row['Title']  
    item_tags = row['Tags']

    # Convert item tags to a set
    item_tags_set = set(item_tags.split(',')) 

    # Compute the number of common tags
    common_tags_count = len(gen_tags_set.intersection(item_tags_set)) 

    # Append to the list
    items_with_common_tags.append((item_title, common_tags_count))

# Sort the items based on the number of common tags in descending order
items_with_common_tags.sort(key=lambda x: x[1], reverse=True)

for item in items_with_common_tags:
    title = item[0]
    print(title)




# # Iterate through the database and update with tags
# for index, row in filtered_df:
#     item_title = row['Title']  # Assuming 'Title' is the column with item names
#     Category,Tags = generate_category_and_tags("bananas")
    
#     # Update the database with the generated tags
#     with engine.connect() as conn:
#         conn.execute(text('''
#             UPDATE "groceryitems"
#             SET "Category" = :tags
#             WHERE "Title" = :title
#         ''').bindparams(tags=Tags, title=item_title))
# print(Tags)
# # print(f'Tags updated successfully in table {table_name}')
