import requests
import json

username = "gandrewnishe"
password = "6399098"

base_url = 'http://127.0.0.1:8000/api/'

#r = requests.get(f"{base_url}book/")
#books = r.json()
#print(books)
#with open("api.json", "w", encoding="UTF-8") as file_out:
#    json.dump(books, file_out, indent=2)


r = requests.post(f"{base_url}order_api/21/3/add_order", auth=(username, password), data={"requires_delivery": "False"})
if r.status_code == 200:
    print(f"Заказ сформирован успешно")