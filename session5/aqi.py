from urllib.request import urlopen
import json

url = "https://store.steampowered.com/api/appdetails?appids=730&filters=price_overview&cc=vn"


#1. Open connection
conn = urlopen(url)

#2. Read data
raw_data = conn.read()

#3. Decode data
text = raw_data.decode("utf-8")
data = json.loads(text)

# results = data["results"]
# for i in results:
#     print("City:",i["s"]["n"][0])
#     print("Index:",i["s"]["a"])
#     print("******************************")
print(data)