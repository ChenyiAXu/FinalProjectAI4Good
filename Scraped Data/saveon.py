import requests
import csv


def get_items(categories):
    all_items = []
    for category, data in categories.items():
        pages = data['pages']
        category_id = data['id']
        breadcrumb = data['breadcrumb']
        for page in range(pages[0], pages[1] + 1):
            params = {
                'take': '30',
                'skip': str((page - 1) * 30),
                'page': str(page),
                'f': breadcrumb,
            }
            response = requests.get(
                f'https://storefrontgateway.saveonfoods.com/api/stores/1982/categories/{category_id}/search',
                params=params
            )
            items = response.json().get('items', [])
            for item in items:
                Title = item.get('name', '')
                Price_numeric = item.get('priceNumeric', '')
                PackageSizing = item.get('pricePerUnit', '')
                Category = category
                Store = "Save On Foods"

                all_items.append({'Title': Title, 'Price': Price_numeric, 'Package Sizing': PackageSizing, 'Category': Category, 'Store': Store})
    return all_items

# Define categories and their respective page ranges, IDs, and breadcrumbs
categories = {
    'Fruit': {'pages': (1, 5), 'id': '30682', 'breadcrumb': 'Breadcrumb:grocery/fruits & vegetables/fresh fruit'},
    'Vegetables': {'pages': (1, 10), 'id': '30694', 'breadcrumb': 'Breadcrumb:grocery/fruits & vegetables/fresh vegetables'},
    'Bread': {'pages': (1, 5), 'id': '30850', 'breadcrumb': 'Breadcrumb:grocery/bakery/breads'},
    'Butter_Spreads': {'pages': (1, 2), 'id': '30907', 'breadcrumb': 'Breadcrumb:grocery/dairy & eggs/butter & margarine'},
    'Cheese': {'pages': (1, 10), 'id': '30910', 'breadcrumb': 'Breadcrumb:grocery/dairy & eggs/cheese'},
    'Egg_and_Substitutes': {'pages': (1, 2), 'id': '30919', 'breadcrumb': 'Breadcrumb:grocery/dairy & eggs/eggs & substitutes'},
    'Milk_Cream': {'pages': (1, 2), 'id': '30930', 'breadcrumb': 'Breadcrumb:grocery/dairy & eggs/milk & creams'},
    'Milk_Substitutes': {'pages': (1, 1), 'id': '30939', 'breadcrumb': 'Breadcrumb:grocery/dairy & eggs/milk substitutes'},
    'Yogurt': {'pages': (1, 8), 'id': '30945', 'breadcrumb': 'Breadcrumb:grocery/dairy & eggs/yogurt'},
    'FrozenFruit': {'pages': (1, 2), 'id': '30971', 'breadcrumb': 'Breadcrumb:grocery/frozen/frozen fruit'},
    'FrozenVegetables': {'pages': (1, 2), 'id': '31002', 'breadcrumb': 'Breadcrumb:grocery/frozen/frozen vegetables'},
    'FrozenMeat': {'pages': (1, 3), 'id': '30830', 'breadcrumb': 'Breadcrumb:grocery/meat & seafood/frozen meat'},
    'Bacon': {'pages': (1, 3), 'id': '30817', 'breadcrumb': 'Breadcrumb:grocery/meat & seafood/bacon'},
    'Beef_Veal': {'pages': (1, 3), 'id': '30792', 'breadcrumb': 'Breadcrumb:grocery/meat & seafood/beef & veal'},
    'Chicken_Turkey': {'pages': (1, 3), 'id': '30798', 'breadcrumb': 'Breadcrumb:grocery/meat & seafood/chicken & turkey'},
    'Fish': {'pages': (1, 2), 'id': '30827', 'breadcrumb': 'Breadcrumb:grocery/meat & seafood/fish'},
    'Hotdogs_Sausages': {'pages': (1, 2), 'id': '30818', 'breadcrumb': 'Breadcrumb:grocery/meat & seafood/hot dogs & sausages'},
    'Lamb': {'pages': (1, 1), 'id': '30815', 'breadcrumb': 'Breadcrumb:grocery/meat & seafood/lamb'},
    'Pork_Ham': {'pages': (1, 3), 'id': '30807', 'breadcrumb': 'Breadcrumb:grocery/meat & seafood/pork & ham'},
    'Meat_Alternatives': {'pages': (1, 3), 'id': '30821', 'breadcrumb': 'Breadcrumb:grocery/meat & seafood/meat alternatives'},
    'Shrimp_ShellFish': {'pages': (1, 1), 'id': '30828', 'breadcrumb': 'Breadcrumb:grocery/meat & seafood/shrimp & shell fish'},
    'Oils_Vinegars': {'pages': (1, 5), 'id': '30625', 'breadcrumb': 'Breadcrumb:grocery/pantry/oils & vinegars'},
    'Juice': {'pages': (1, 6), 'id': '30407', 'breadcrumb': 'Breadcrumb:grocery/pantry/beverages/juice'},
    'Coffee': {'pages': (1, 12), 'id': '30386', 'breadcrumb': 'Breadcrumb:grocery/pantry/beverages/coffee'},
    'Tea': {'pages': (1, 7), 'id': '30393', 'breadcrumb': 'Breadcrumb:grocery/pantry/beverages/tea'},
    'Herbs_Spices_Sesaonings': {'pages': (1, 15), 'id': '30635', 'breadcrumb': 'Breadcrumb:grocery/pantry/herbs, spices & seasonings'},
    'CannedFood': {'pages': (1, 23), 'id': '30527', 'breadcrumb': 'Breadcrumb:grocery/pantry/canned & packaged'},
    'Rice': {'pages': (1, 5), 'id': '30672', 'breadcrumb': 'Breadcrumb:grocery/pantry/pasta, sauces & grains/rice'},
    'Pasta_Sauce': {
        'pages': (1, 8), 'id': '30653', 'breadcrumb': 'Breadcrumb:grocery/pantry/pasta, sauces & grains/pasta & noodles',
        'pages': (1, 4), 'id': '30662', 'breadcrumb': 'Breadcrumb:grocery/pantry/pasta, sauces & grains/pasta sauces',
        'pages': (1, 14), 'id': '30668', 'breadcrumb': 'Breadcrumb:grocery/pantry/pasta, sauces & grains/pasta mixes'
    },
    'BakingEssentials': {'pages': (1, 5), 'id': '30373', 'breadcrumb': 'Breadcrumb:grocery/pantry/baking goods'},
}

# Fetch items from the specified categories and page ranges
all_items = get_items(categories)

# # Write items to CSV
# with open('items.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Title', 'Price', 'package sizing', 'Category', 'Store']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
#     writer.writeheader()
#     for item in all_items:
#         writer.writerow(item)

# print("Items have been written to items.csv.")
