import discord
import os
from dotenv import load_dotenv
import requests
import json

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    # ボット自身のメッセージに反応しないようにする
    if message.author == client.user:
        return

    content = message.content

    if content.startswith('prof'):

        subcommands = content.strip().split()[1:]

        if len(subcommands) == 0:
            await describe(message)
            return

        if subcommands[0] == "help":
            await show_help(message)
            return

        if subcommands[0] == "show":
            try:
                if len(subcommands) == 1:
                    result = (
                        "第二引数にユーザーidを指定してください。\n"
                        "例： `prof show 286685511145242625`"
                    )
                    await message.channel.send(result)
                    return
                else:
                    user_id = subcommands[1]
                    url = f"https://api.pjsekai.moe/api/user/{user_id}/profile"
                    response = requests.get(url)
                    data = json.loads(response.text)
                    game_data = data['user']['userGamedata']
                    result = (
                        f"{game_data['name']} のプロフィール\n"
                        f"ランク：{game_data['rank']}"
                    )
                    await message.channel.send(result)
            except Exception as e:
                await message.channel.send(e)
            return


async def describe(message):
    description = (
        "Hello, World!\n"
        "`prof help`  コマンドの使い方を表示します。"
    )
    await message.channel.send(description)


async def show_help(message):
    description = (
        "サブコマンド一覧\n"
        "`help`  コマンドの使い方を表示します。\n"
        "`show`  ユーザーのプロフィールを表示します。第二引数にユーザーidを入力します。"
    )

    await message.channel.send(description)

load_dotenv()

TOKEN = os.getenv('TOKEN')

client.run(TOKEN)
