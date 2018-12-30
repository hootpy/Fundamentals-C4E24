from urllib.request import urlopen
import json

while True:
    id_game= str(input("Enter game id:"))
    if id_game.lower() == "exit":
        break
    elif id_game.isdigit() == False:
        print("Enter game id!")
    else:
        url = f"https://store.steampowered.com/api/appdetails?appids={id_game}&cc=vn"

        #1. Open connection
        conn = urlopen(url)

        #2. Read data
        raw_data = conn.read()

        #3. Decode data
        text = raw_data.decode("utf-8")
        data = json.loads(text)

        if data[id_game]["success"]:
            sub_info = data[id_game]["data"]["package_groups"][0]["subs"]
            for i in sub_info:
                game_name = i["option_text"]
                price = (int(i["price_in_cents_with_discount"])/100) * 0.78
                print(game_name)
                print("Gia ban", price)
                print("**********************")
        else:
            print("Sai ma game")
