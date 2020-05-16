import json
import requests

def getBattleRoyalStats(platform, epic_nickname) :
    api_token = '04a3ac0c-1952-43c2-a8d7-de1f4cfedfaa'
    api_url = f"https://api.fortnitetracker.com/v1/profile/{platform}/{epic_nickname}"
    headers = {'Content-Type': 'application/json',
               'TRN-Api-Key': api_token}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        result = json.loads(response.content.decode('utf-8'))
        print("OK")
        print(json.dumps(result, indent=2))
    else : print("Failed!")

platform = input("Enter Platform (pc, psn, xbl): ")
if(platform not in ["pc", "psn", "xbl"]) : platform = "pc"
print("Platform: " + platform)
epic_nickname = input("Enter epic nickname: ")
getBattleRoyalStats(platform, epic_nickname)


