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

# Define distinct attributes 
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

sausage = common_data.copy()
sausage["userData"]["sessionId"] = "7a20ee46-9f2a-4d58-bd81-a8f5c9c4fb0c"

lamb_veal = common_data.copy()
lamb_veal["userData"]["sessionId"] = "7a20ee46-9f2a-4d58-bd81-a8f5c9c4fb0c"

kebabs_marinatedMeat = common_data.copy()
kebabs_marinatedMeat["userData"]["sessionId"] = "7a20ee46-9f2a-4d58-bd81-a8f5c9c4fb0c"

beef = common_data.copy()
beef["userData"]["sessionId"] = "7a20ee46-9f2a-4d58-bd81-a8f5c9c4fb0c"

chicken_turkey = common_data.copy()
chicken_turkey["userData"]["sessionId"] = "7a20ee46-9f2a-4d58-bd81-a8f5c9c4fb0c"

pork_ham = common_data.copy()
pork_ham["userData"]["sessionId"] = "7a20ee46-9f2a-4d58-bd81-a8f5c9c4fb0c"

bacon = common_data.copy()
bacon["userData"]["sessionId"] = "7a20ee46-9f2a-4d58-bd81-a8f5c9c4fb0c"

hotdogs = common_data.copy()
hotdogs["userData"]["sessionId"] = "bec28050-b5fa-4e01-b836-93fc4af4b3d3"

HalalMeat = common_data.copy()
HalalMeat["userData"]["sessionId"] = "7a20ee46-9f2a-4d58-bd81-a8f5c9c4fb0c"

egg_and_substitutes = common_data.copy()
egg_and_substitutes["userData"]["sessionId"] = "8124d3aa-df92-4abd-8a0d-983570ec1400"

nonDairy_milk_alternatives = common_data.copy()
nonDairy_milk_alternatives["userData"]["sessionId"] = "8124d3aa-df92-4abd-8a0d-983570ec1400"

cannedFood = common_data.copy()
cannedFood["userData"]["sessionId"] = "8124d3aa-df92-4abd-8a0d-983570ec1400"

oils_vinegar = common_data.copy()
oils_vinegar["userData"]["sessionId"] = "8124d3aa-df92-4abd-8a0d-983570ec1400"

pasta_sauce = common_data.copy()
pasta_sauce["userData"]["sessionId"] = "0d575695-ba4c-41a0-b144-6f00a9459b79"

plantBasedMeat = common_data.copy()
plantBasedMeat["userData"]["sessionId"] = "7a20ee46-9f2a-4d58-bd81-a8f5c9c4fb0c"

rice = common_data.copy()
rice["userData"]["sessionId"] = "bfacc561-aeb2-44b1-bfed-217c6cd3c2be"

FrozenFruit  = common_data.copy()
FrozenFruit ["userData"]["sessionId"] = "0d575695-ba4c-41a0-b144-6f00a9459b79"

FrozenVegetables = common_data.copy()
FrozenVegetables["userData"]["sessionId"] =   "57f71a20-d492-48f4-9abb-85ec0ffb065b"

FrozenMeat_Seafood  = common_data.copy()
FrozenMeat_Seafood ["userData"]["sessionId"] = "bfacc561-aeb2-44b1-bfed-217c6cd3c2be"

coffee  = common_data.copy()
coffee ["userData"]["sessionId"] = "bfacc561-aeb2-44b1-bfed-217c6cd3c2be"

tea_hotDrinks  = common_data.copy()
tea_hotDrinks ["userData"]["sessionId"] = "bfacc561-aeb2-44b1-bfed-217c6cd3c2be"

shrimp  = common_data.copy()
shrimp ["userData"]["sessionId"] = "bfacc561-aeb2-44b1-bfed-217c6cd3c2be"

fish  = common_data.copy()
fish ["userData"]["sessionId"] = "bfacc561-aeb2-44b1-bfed-217c6cd3c2be"

salmon  = common_data.copy()
salmon ["userData"]["sessionId"] = "bfacc561-aeb2-44b1-bfed-217c6cd3c2be"

bread = common_data.copy()
bread ["userData"]["sessionId"] = "998e81b4-218e-4e07-a4c1-0542a2f84438"

bakingEssentials = common_data.copy()
bakingEssentials["userData"]["sessionId"] = "998e81b4-218e-4e07-a4c1-0542a2f84438"

spices_seasoning = common_data.copy()
spices_seasoning["userData"]["sessionId"] = "05a65107-140c-40b8-8dd8-1444d516c0f4"

juice = common_data.copy()
juice["userData"]["sessionId"] = "05a65107-140c-40b8-8dd8-1444d516c0f4"





def superstore_fetch_product_info(data, page_title, category):
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
                            "Category": category,
                            "Store": "Superstore"  # Add the label here
                        })
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
    
    return product_info

# Categories and their corresponding data
superstore_categories = {
    "fruit": ('listingPage/28194', fruit_data),
    "vegetable": ('listingPage/28195', vegetable_data),
    "butter and spreads": ('listingPage/28220', butter_spreads),
    "milk and cream": ('listingPage/28224', milk_cream),
    "cheese": ('listingPage/28225', cheese),
    "yogurt": ('listingPage/28227', yogurt),
    "sausage": ('listingPage/28170', sausage),
    "lamb_veal": ('listingPage/28171', lamb_veal),
    "kebabs_marinatedMeat": ('listingPage/28173', kebabs_marinatedMeat),
    "beef": ('listingPage/28174', beef),
    "chicken_turkey": ('listingPage/28214', chicken_turkey),
    "pork_ham": ('listingPage/28215', pork_ham),
    "bacon": ('listingPage/59252', bacon),
    "hotdogs": ('listingPage/59253', hotdogs),
    "HalalMeat": ('listingPage/59257', HalalMeat),
    "egg_and_substitutes": ('listingPage/28222', egg_and_substitutes),
    "nonDairy_milk_alternatives": ('listingPage/58904', nonDairy_milk_alternatives),
    "cannedFood": ('listingPage/28187', cannedFood),
    "oils_vinegar": ('listingPage/28244', oils_vinegar),
    "pasta_sauce": ('listingPage/28247', pasta_sauce),
    "rice": ('listingPage/28248', rice),
    "FrozenFruit": ('listingPage/28162', FrozenFruit),
    "FrozenMeat_Seafood": ('listingPage/57003', FrozenMeat_Seafood),
    "coffee": ('listingPage/28228', coffee),
    "tea_hotDrinks": ('listingPage/28234', tea_hotDrinks),
    "shrimp": ('listingPage/28218', shrimp),
    "fish": ('listingPage/28218', fish),
    "salmon": ('listingPage/28217', salmon),
    "plantBasedMeat": ('listingPage/59318', plantBasedMeat),
    "bread":('listingPage/28251',bread),
    "bakingEssentials":('listingPage/28186',bakingEssentials),
    "spices_seasoning":('listingPage/28188',spices_seasoning),
    "juice":('listingPage/28230',juice),
    "FrozenVegetables":('listingPage/29873',FrozenVegetables)
}


# Define categories and their corresponding page ranges
superstore_category_pages = {
    "fruit": (1,3),
    "vegetable": (1,6),
    "butter and spreads": (1,2),
    "milk and cream": (1,4),
    "cheese": (1,6),
    "yogurt": (1,6),
    "sausage": (1,3),
    "lamb_veal": (1,1),
    "kebabs_marinatedMeat": (1,1),
    "beef": (1,3),
    "chicken_turkey": (1,4),
    "pork_ham": (1,2),
    "bacon": (1,1),
    "hotdogs": (1,1),
    "HalalMeat": (1,2),
    "egg_and_substitutes": (1,1),
    "nonDairy_milk_alternatives": (1,2),
    "cannedFood": (1,18),
    "oils_vinegar": (1,5),
    "pasta_sauce": (1,14),
    "rice": (1,5),
    "FrozenFruit": (1,2),
    "FrozenMeat_Seafood": (1,7),
    "coffee": (1,8),
    "tea_hotDrinks": (1,7),
    "shrimp": (1,2),
    "fish": (1,2),
    "salmon": (1,1),
    "plantBasedMeat": (1,1),
    "bread":(1,3),
    "bakingEssentials":(1,17),
    "spices_seasoning":(1,11),
    "juice":(1,9),
    "FrozenVegetables":(1,3),

}
