import json
import requests

response_snacker_data = requests.get("https://s3.amazonaws.com/misc-file-snack/MOCK_SNACKER_DATA.json")
response_product_list = requests.get("https://ca.desknibbles.com/products.json?limit=250")
MOCK_SNACKER_DATA = json.loads(response_snacker_data.text)
PRODUCT_DATA = json.loads(response_product_list.text)

total_price = 0.00

for x in MOCK_SNACKER_DATA:
    for y in PRODUCT_DATA['products']:
        if (x['fave_snack'] == y['title']):
            print (x['fave_snack']) # a) fave snacks
            print (x['email']) # b) emails of fave snack
            total_price += float(y['variants'][0]['price']) # c) adding the prices to find the total price


print(total_price) # c) the total number if all of the users with the favorite snacks bought a snack.

# My favourite snack would probably have to be Halva! It's a Russian candy which is basically just Sunflowers and liquid sugar blended into small candies!
