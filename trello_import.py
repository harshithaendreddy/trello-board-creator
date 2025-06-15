import requests
import time
import json
import os

# Directly access GitHub Actions secrets via environment variables
API_KEY = os.getenv('TRELLO_API_KEY')
TOKEN = os.getenv('TRELLO_TOKEN')

if not API_KEY or not TOKEN:
    raise Exception("❌ API key or token not found in environment variables.")

# Load board structure from JSON
with open('DeveloperDashboardBoard.json') as f:
    board_data = json.load(f)

# Create the board
board_name = board_data["name"]
create_board_url = "https://api.trello.com/1/boards/"
params = {
    "name": board_name,
    "key": API_KEY,
    "token": TOKEN,
    "defaultLists": "false"
}

response = requests.post(create_board_url, params=params)
if response.status_code != 200:
    raise Exception("❌ Board creation failed:", response.text)

board = response.json()
board_id = board["id"]
print(f"✅ Created Board: {board_name} | ID: {board_id}")

# Create lists and cards
for list_data in board_data["lists"]:
    list_name = list_data["name"]
    create_list_url = f"https://api.trello.com/1/lists"
    list_params = {
        "name": list_name,
        "idBoard": board_id,
        "key": API_KEY,
        "token": TOKEN
    }
    list_response = requests.post(create_list_url, params=list_params)
    if list_response.status_code != 200:
        print(f"❌ Failed to create list {list_name}")
        continue

    list_id = list_response.json()["id"]
    print(f"📂 Created List: {list_name}")

    for card_name in list_data["cards"]:
        create_card_url = "https://api.trello.com/1/cards"
        card_params = {
            "name": card_name,
            "idList": list_id,
            "key": API_KEY,
            "token": TOKEN
        }
        card_response = requests.post(create_card_url, params=card_params)
        if card_response.status_code == 200:
            print(f"📝  Added card: {card_name}")
        else:
            print(f"⚠️  Failed to add card: {card_name}")
        time.sleep(0.2)  # Prevent hitting Trello API rate limits
