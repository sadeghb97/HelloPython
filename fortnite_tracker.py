import json
import requests

LAST_PLATFORM = None
LAST_EPIC_NICKNAME = None

def getBattleRoyalStats(platform = None, epic_nickname = None, callback = None) :
    global LAST_PLATFORM, LAST_EPIC_NICKNAME

    if platform == None or epic_nickname == None :
        platform = input("Enter Platform (pc, psn, xbl): ")
        if (platform not in ["pc", "psn", "xbl"]): platform = "pc"
        print("Platform: " + platform)
        epic_nickname = input("Enter epic nickname: ")

    LAST_PLATFORM = platform
    LAST_EPIC_NICKNAME = epic_nickname

    api_token = '04a3ac0c-1952-43c2-a8d7-de1f4cfedfaa'
    api_url = f"https://api.fortnitetracker.com/v1/profile/{LAST_PLATFORM}/{LAST_EPIC_NICKNAME}"
    headers = {'Content-Type': 'application/json',
               'TRN-Api-Key': api_token}
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        result = json.loads(response.content.decode('utf-8'))
        print("OK")
        print(epic_nickname + ": ", end = "")
        if "lifeTimeStats" in result :
            print(json.dumps(result['lifeTimeStats'], indent=2))
        else : print(json.dumps(result, indent=2))
    else : print("Failed!")

    if(callback != None) : callback()


