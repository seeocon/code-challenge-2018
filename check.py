# Desk Nibbles’ Code Challenge.
"""
Solve this: 
Use the following fake snacker list:

https://s3.amazonaws.com/misc-file-snack/MOCK_SNACKER_DATA.json

Find all emails of snackers with a 'fave_snack'of a product we stock:

Our product list can be found here (assume all products here are in stock):
https://ca.desknibbles.com/products.json?limit=250

a) List the real stocked snacks you found under the snacker's 'fave_snack'?
b) What're the emails of the snackers who listed those as a 'fave_snack'?
c) If all those snackers we're to pay for their 'fave_snack'what's the total price?
"""

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
