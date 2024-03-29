import requests
import json

username = "Mac"
password = "Htdvu6gd58!"

base_url = 'https://bookingcom.pythonanywhere.com/api/'

#r = requests.get(f"{base_url}book/?page_size=40")
#books = r.json()
#print(books)
#with open("api.json", "w", encoding="UTF-8") as file_out:
#    json.dump(books, file_out, indent=2)


r = requests.post(f"{base_url}order_add/21/", auth=(username, password), data={"requires_delivery": "False", "quantity":1})
if r.status_code == 200:
    print(f"Заказ сформирован успешно")