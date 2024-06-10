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
    'Origin': 'https://www.nofrills.ca',
    'Origin_Session_Header': 'B',
    'Referer': 'https://www.nofrills.ca/',
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
    "cart": {"cartId": "77acf7ce-c1df-44cc-8beb-786da4fbce55"},
    'fulfillmentInfo': {'storeId': '3403','pickupType': 'STORE','offerType': 'OG', 'date': '08062024','timeSlot': None,},
    "listingInfo": {"filters": {}, "sort": {}, "pagination": {}, "includeFiltersInResponse": True},
    "banner": "nofrills",
    "userData": {"domainUserId": "4d29b63fe-5c3d-4f19-a349-ec5d532d37fb"}
}

# Define distinct attributes 

vegetable_data = common_data.copy()
vegetable_data["userData"]["sessionId"] = "3293ccc5-1501-40c1-a549-179606e8fc78"

fruit_data = common_data.copy()
fruit_data["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

sausage = common_data.copy()
sausage["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

lamb_veal = common_data.copy()
lamb_veal["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

kebabs_marinatedMeat = common_data.copy()
kebabs_marinatedMeat["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

beef = common_data.copy()
beef["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

chicken_turkey = common_data.copy()
chicken_turkey["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

pork_ham = common_data.copy()
pork_ham["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

bacon = common_data.copy()
bacon["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

hotdogs = common_data.copy()
hotdogs["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

HalalMeat = common_data.copy()
HalalMeat["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

plantBasedMeat = common_data.copy()
plantBasedMeat["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

fish = common_data.copy()
fish["userData"]["sessionId"] = '3293ccc5-1501-40c1-a549-179606e8fc78'

salmon = common_data.copy()
salmon["userData"]["sessionId"] =  '3293ccc5-1501-40c1-a549-179606e8fc78'

shrimp = common_data.copy()
shrimp["userData"]["sessionId"] =  '3293ccc5-1501-40c1-a549-179606e8fc78'

bread = common_data.copy()
bread["userData"]["sessionId"] =  '3293ccc5-1501-40c1-a549-179606e8fc78'

coffee = common_data.copy()
coffee["userData"]["sessionId"] =  '3293ccc5-1501-40c1-a549-179606e8fc78'

tea_hotDrinks = common_data.copy()
tea_hotDrinks["userData"]["sessionId"] =  '3293ccc5-1501-40c1-a549-179606e8fc78'

FrozenFruit = common_data.copy()
FrozenFruit["userData"]["sessionId"] =  '3293ccc5-1501-40c1-a549-179606e8fc78'

FrozenVegetables = common_data.copy()
FrozenVegetables["userData"]["sessionId"] =   '3293ccc5-1501-40c1-a549-179606e8fc78'

FrozenMeat_Seafood  = common_data.copy()
FrozenMeat_Seafood ["userData"]["sessionId"] = "d9886879-14a9-420c-a05a-0e9f65dc2b0e"


cheese = common_data.copy()
cheese["userData"]["sessionId"] =  "4ded8592-26d9-4396-b8ed-e61c428d3e1e"

yogurt= common_data.copy()
yogurt["userData"]["sessionId"] =  "4ded8592-26d9-4396-b8ed-e61c428d3e1e"


butter_spreads= common_data.copy()
butter_spreads["userData"]["sessionId"] = "4ded8592-26d9-4396-b8ed-e61c428d3e1e"

egg_and_substitutes= common_data.copy()
egg_and_substitutes["userData"]["sessionId"] = "4ded8592-26d9-4396-b8ed-e61c428d3e1e"

milk_cream= common_data.copy()
milk_cream["userData"]["sessionId"] = "4ded8592-26d9-4396-b8ed-e61c428d3e1e"

bakingEssentials= common_data.copy()
bakingEssentials["userData"]["sessionId"] = "4ded8592-26d9-4396-b8ed-e61c428d3e1e"

pasta_sauce= common_data.copy()
pasta_sauce["userData"]["sessionId"] = "4ded8592-26d9-4396-b8ed-e61c428d3e1e"
  
rice= common_data.copy()
rice["userData"]["sessionId"] = "4ded8592-26d9-4396-b8ed-e61c428d3e1e"

oils_vinegar= common_data.copy()
oils_vinegar["userData"]["sessionId"] = "4ded8592-26d9-4396-b8ed-e61c428d3e1e"

spices_seasoning= common_data.copy()
spices_seasoning["userData"]["sessionId"] = "4ded8592-26d9-4396-b8ed-e61c428d3e1e"

cannedFood= common_data.copy()
cannedFood["userData"]["sessionId"] = "4ded8592-26d9-4396-b8ed-e61c428d3e1e"

juice= common_data.copy()
juice["userData"]["sessionId"] = "4ded8592-26d9-4396-b8ed-e61c428d3e1e"

nonDairy_milk_alternatives= common_data.copy()
nonDairy_milk_alternatives["userData"]["sessionId"] = "4ded8592-26d9-4396-b8ed-e61c428d3e1e"
   
def nofrills_fetch_product_info(data, page_title, category):
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
                            "Store": "No Frills"  # Add the label here
                        })
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)
    
    return product_info

# Categories and their corresponding data
nofrills_categories = {
    "vegetable": ('listingPage/28195', vegetable_data),
    "fruit": ('listingPage/28194', fruit_data),
    "sausage": ('listingPage/28170', sausage),
    "lamb_veal": ('listingPage/28171', lamb_veal),
    "kebabs_marinatedMeat": ('listingPage/28173', kebabs_marinatedMeat),
    "beef": ('listingPage/28174', kebabs_marinatedMeat),
    "chicken_turkey": ('listingPage/28214', chicken_turkey),
    "pork_ham": ('listingPage/28215', pork_ham),
    "bacon": ('listingPage/59252',bacon),
    "hotdogs": ('listingPage/59253',hotdogs),
    "HalalMeat": ('listingPage/59257',HalalMeat),
    "plantBasedMeat": ('listingPage/59318',plantBasedMeat),
    "fish": ('listingPage/28191',fish),
    "salmon": ('listingPage/28217',salmon),
    "shrimp": ('listingPage/28218',shrimp),
    "bread": ('listingPage/28251',bread),
    "coffee": ('listingPage/28228',coffee),
    "tea_hotDrinks": ('listingPage/28234',tea_hotDrinks),
    "FrozenFruit": ('listingPage/29861',FrozenFruit),
    "FrozenVegetables":('listingPage/29873',FrozenVegetables),
    "cheese":('listingPage/28225',cheese),
    "yogurt":('listingPage/28227',yogurt),
    "butter_spreads":('listingPage/28220',butter_spreads),
    "egg_and_substitutes":('listingPage/28222',egg_and_substitutes),
    "milk_cream":('listingPage/28224',milk_cream),
    "bakingEssentials":('listingPage/28186',bakingEssentials),
    "pasta_sauce":('listingPage/28247',pasta_sauce),
    "rice":('listingPage/28248',rice),
    "oils_vinegar":('listingPage/28244',oils_vinegar),
    "spices_seasoning":('listingPage/28188',spices_seasoning),
    "cannedFood":('listingPage/28187',cannedFood),
    "juice":('listingPage/28230',juice),
    "nonDairy_milk_alternatives":('listingPage/58904',nonDairy_milk_alternatives),
    "FrozenMeat_Seafood":('listingPage/57003',FrozenMeat_Seafood),

}


# Define categories and their corresponding page ranges
nofrills_category_pages = {
    "vegetable": (1,6),
    "fruit": (1, 3),
    "sausage": (1, 2),
    "lamb_veal": (1, 1),
    "kebabs_marinatedMeat":(1,1),
    "beef":(1,4),
    "chicken_turkey":(1,4),
    "pork_ham": (1,1),
    "bacon": (1,1),
    "hotdogs":(1,1),
    "HalalMeat":(1,2),
    "plantBasedMeat":(1,1),
    "fish": (1,1),
    "salmon": (1,1),
    "shrimp": (1,1),
    "bread":(1,2),
    "coffee":(1,3),
    "tea_hotDrinks":(1,5),
    "FrozenFruit":(1,2),
    "FrozenVegetables":(1,3),
    "cheese":(1,4),
    "yogurt":(1,6),
    "butter_spreads":(1,2),
    "egg_and_substitutes":(1,1),
    "milk_cream":(1,3),
    "bakingEssentials":(1,9),
    "pasta_sauce":(1,9),
    "rice":(1,4),
    "oils_vinegar":(1,3),
    "spices_seasoning":(1,7),
    "cannedFood":(1,13),
    "juice":(1,7),
    "nonDairy_milk_alternatives":(1,1),
    "FrozenMeat_Seafood":(1,6),

}
