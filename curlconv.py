import requests
import json
import csv

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en',
    'Business-User-Agent': 'PCXWEB',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'DNT': '1',
    'Origin': 'https://www.realcanadiansuperstore.ca',
    'Origin_Session_Header': 'B',
    'Referer': 'https://www.realcanadiansuperstore.ca/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0',
    'is-helios-account': 'false',
    'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'x-apikey': 'C1xujSegT5j3ap3yexJjqhOfELwGKYvz',
    'x-application-type': 'Web',
    'x-channel': 'web',
    'x-loblaw-tenant-id': 'ONLINE_GROCERIES',
    'x-preview': 'false',
}

# Define common attributes
common_data = {
    "cart": {"cartId": "fe3216ff-ab17-47c3-98b1-ed2242591c9a"},
    "fulfillmentInfo": {"storeId": "1518", "pickupType": "STORE", "offerType": "OG", "date": "05062024", "timeSlot": None},
    "listingInfo": {"filters": {}, "sort": {}, "pagination": {"from": 1}, "includeFiltersInResponse": True},
    "banner": "superstore",
    "userData": {"domainUserId": "4b129ecf-7f11-42ef-86ec-540244009529"}
}

# Define distinct attributes for fruit and vegetable data
fruit_data = common_data.copy()
fruit_data["userData"]["sessionId"] = "bec28050-b5fa-4e01-b836-93fc4af4b3d3"

vegetable_data = common_data.copy()
vegetable_data["userData"]["sessionId"] = "7ffeb0bc-cc0c-42ab-a079-5c1b90fd75bc"

butter_spreads = common_data.copy()
butter_spreads["userData"]["sessionId"] = "bec28050-b5fa-4e01-b836-93fc4af4b3d3"

milk_cream = common_data.copy()
milk_cream["userData"]["sessionId"] = "bec28050-b5fa-4e01-b836-93fc4af4b3d3"

cheese = common_data.copy()
cheese["userData"]["sessionId"] = "bec28050-b5fa-4e01-b836-93fc4af4b3d3"

yogurt = common_data.copy()
yogurt["userData"]["sessionId"] = "bec28050-b5fa-4e01-b836-93fc4af4b3d3"

southAsian = common_data.copy()
southAsian["userData"]["sessionId"] = "bec28050-b5fa-4e01-b836-93fc4af4b3d3"

def fetch_product_info(data, page_title, category):
    response = requests.post(f'https://api.pcexpress.ca/pcx-bff/api/v2/{page_title}', headers=headers, json=data)
    product_info = []

    if response.status_code == 200:
        response_data = response.json()
        components = response_data.get('layout', {}).get('sections', {}).get('productListingSection', {}).get('components', [])
        for component in components:
            component_data = component.get('data', {}).get('productGrid', {}).get('productTiles', [])
            if component_data:
                for key in component_data:
                    title = key.get('title')
                    packageSizing = key.get('packageSizing')
                    price = key.get('pricing', {}).get('price')
                    if title and packageSizing and price:
                        product_info.append({
                            "Title": title,
                            "Price": price,
                            "Package Sizing": packageSizing,
                            "Category": category
                        })
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
    
    return product_info

# Categories and their corresponding data
categories = {
    "fruit": ('listingPage/28194', fruit_data),
    "vegetable": ('listingPage/28195', vegetable_data),
    "butter and spreads": ('listingPage/28220', butter_spreads),
    "milk and cream": ('listingPage/28224', milk_cream),
    "cheese": ('listingPage/28225', cheese),
    "yogurt": ('listingPage/28227', yogurt),
    "southAsian": ('listingPage/58045', southAsian)
}

# Fetch data for all categories and write to CSV
all_product_info = []

for category, (page_title, data) in categories.items():
    print(f"Fetching data for {category}")
    product_info = fetch_product_info(data, page_title, category)
    all_product_info.extend(product_info)

# Write to CSV
csv_file = 'product_data.csv'
csv_columns = ["Title", "Price", "Package Sizing", "Category"]

try:
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for product in all_product_info:
            writer.writerow(product)
    print(f"Data successfully written to {csv_file}")
except IOError:
    print("I/O error while writing to CSV")




