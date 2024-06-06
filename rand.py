import requests
import json

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

data = '{"cart":{"cartId":"fe3216ff-ab17-47c3-98b1-ed2242591c9a"},"fulfillmentInfo":{"storeId":"1518","pickupType":"STORE","offerType":"OG","date":"05062024","timeSlot":null},"listingInfo":{"filters":{},"sort":{},"pagination":{"from":1},"includeFiltersInResponse":true},"banner":"superstore","userData":{"domainUserId":"4b129ecf-7f11-42ef-86ec-540244009529","sessionId":"bec28050-b5fa-4e01-b836-93fc4af4b3d3"}}'

response = requests.post('https://api.pcexpress.ca/pcx-bff/api/v2/listingPage/28194', headers=headers, data=data)

# Parse the JSON content
response_data = json.loads(response.content)

# Extract and print the title, price, and package size

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    response_data = response.json()
    
    # Pretty print the JSON data
    #print(json.dumps(response_data))
    # Iterate over components and print product tiles
    count = 0
    components = response_data.get('layout', {}).get('sections', {}).get('productListingSection', {}).get('components', [])
    for component in components:
        component_data = component.get('data', {}).get('productGrid', {}).get('productTiles', [])
        if component_data:
            for key in component_data:
                title = key.get('title')
                packageSizing = key.get('packageSizing')
                price = key.get('pricing', {}).get('price')

                if title and packageSizing and price:
                    count+=1
                    print(f"Title: {title}")
                    print(f"Price: ${price}")
                    print(f"packageSizing: {packageSizing}")
                    print("\n")
                    

                    

else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)
