import csv
from superstore import superstore_categories, superstore_category_pages, superstore_fetch_product_info
from nofrills import nofrills_categories, nofrills_category_pages, nofrills_fetch_product_info
from saveon import get_items, categories as saveon_categories  # Import the get_items function and categories from your main script

# Fetch items from Save On Foods categories
print('Fetching items from Save On')
saveon_items = get_items(saveon_categories)


# Fetch data for Superstore categories and pages
superstore_all_product_info = []
for category, (page_title, data) in superstore_categories.items():
    print(f"Fetching data for {category} from Superstore")
    page_range = superstore_category_pages.get(category, (1, 1))
    for page_num in range(page_range[0], page_range[1]+1):
        print(f"Fetching data for page {page_num}")
        data["listingInfo"]["pagination"]["from"] = page_num
        product_info = superstore_fetch_product_info(data, page_title, category)
        superstore_all_product_info.extend(product_info)

# Fetch data for No Frills categories and pages
nofrills_all_product_info = []
for category, (page_title, data) in nofrills_categories.items():
    print(f"Fetching data for {category} from No Frills")
    page_range = nofrills_category_pages.get(category, (1, 1))
    for page_num in range(page_range[0], page_range[1]+1):
        print(f"Fetching data for page {page_num}")
        data["listingInfo"]["pagination"]["from"] = page_num
        product_info = nofrills_fetch_product_info(data, page_title, category)
        nofrills_all_product_info.extend(product_info)


# Combine all fetched data
all_product_info = saveon_items + superstore_all_product_info + nofrills_all_product_info

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
