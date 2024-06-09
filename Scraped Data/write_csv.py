import csv
from superstore import *
from nofrills import *

# Fetch data for all categories and pages and write to CSV
all_product_info = []


# Fetch Superstore data
for category, (page_title, data) in superstore_categories.items():
    print(f"Fetching data for {category} from Superstore")
    page_range = superstore_category_pages.get(category, (1, 1))  # Default to (1, 1) if category not found
    for page_num in range(page_range[0], page_range[1]+1):  # Iterate over the range of pages
        print(f"Fetching data for page {page_num}")
        data["listingInfo"]["pagination"]["from"] = page_num  # Update pagination
        product_info = superstore_fetch_product_info(data, page_title, category)
        all_product_info.extend(product_info)

# Fetch No Frills data
for category, (page_title, data) in nofrills_categories.items():
    print(f"Fetching data for {category} from No Frills")
    page_range = nofrills_category_pages.get(category, (1, 1))  # Default to (1, 1) if category not found
    for page_num in range(page_range[0], page_range[1]+1):  # Iterate over the range of pages
        print(f"Fetching data for page {page_num}")
        data["listingInfo"]["pagination"]["from"] = page_num  # Update pagination
        product_info = nofrills_fetch_product_info(data, page_title, category)
        all_product_info.extend(product_info)

# Write to CSV
csv_file = 'product_data.csv'
csv_columns = ["Title", "Price", "Package Sizing", "Category", "Store"]

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for product in all_product_info:
            writer.writerow(product)
    print(f"Data successfully written to {csv_file}")
except IOError:
    print("I/O error while writing to CSV")
