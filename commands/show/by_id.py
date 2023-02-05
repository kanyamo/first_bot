import requests
import json


async def send_profile_by_id(message, id):
    url = f"https://api.pjsekai.moe/api/user/{id}/profile"
    response = requests.get(url)
    data = json.loads(response.text)
    game_data = data['user']['userGamedata']
    result = (
        f"{game_data['name']} のプロフィール\n"
        f"ランク：{game_data['rank']}"
    )
    await message.channel.send(result)
