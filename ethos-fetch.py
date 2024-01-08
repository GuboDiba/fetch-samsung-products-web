
import requests

#function for fetching Samsung from api endpoint
def fetch_samsung():
   try:
       response = requests.get("https://dummyjson.com/products", timeout=5)
       response.raise_for_status()

   except requests.exceptions.Timeout:
       print("The request timed out.Please check your internet connection or try again later")
       return None

   except requests.exceptions.HTTPError as errorHTTP:
       print ("Error: Unable to retrieve data due to a server issue. Please try again later.")
       return None

   except requests.exceptions.ConnectionError as errorConnection:
       print ("Error: Unable to establish a connection. Please check your internet connection.")
       return None

   except requests.exceptions.RequestException as error:
       print ("Error: Something went wrong during the request. Please try again later.")
       return None

   else:
       data = response.json()
       return data

#counting number
def count_samsung_products(data):
   samsung_products = [product for product in data['products'] if product['brand'] == 'Samsung']
   return len(samsung_products)

data = fetch_samsung()
if data is not None:
   num_samsung_products = count_samsung_products(data)
   print(f"Number of Samsung products: {num_samsung_products}")
else:
   print("Failed to fetch samsung.")