import requests
import json


def get_profile_by_id(id: str) -> str:
    url = f"https://api.pjsekai.moe/api/user/{id}/profile"
    result = ""
    try:
        response = requests.get(url, timeout=2.0)
        data = json.loads(response.text)
        game_data = data['user']['userGamedata']
        result = (
            f"{game_data['name']} のプロフィール\n"
            f"ランク：{game_data['rank']}"
        )
    except Exception as e:
        result = f"{id = } は存在しないユーザーの可能性があります。"
    return result
