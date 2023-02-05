import discord
import os
from dotenv import load_dotenv
from commands.help import help
from commands.show import send_profile_by_id

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

        # 引数を分析するシステムはもう少し改良の余地あり
        subcommands = content.strip().split()[1:]

        if len(subcommands) == 0:
            await describe(message)
            return

        if subcommands[0] == "help":
            await help(message)
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
                    await send_profile_by_id(message, user_id)
                    return
            except Exception as e:
                await message.channel.send(e)
            return


async def describe(message):
    description = (
        "Hello, World!\n"
        "`prof help`でコマンドの使い方を表示します。"
    )
    await message.channel.send(description)


load_dotenv()

TOKEN = os.getenv('TOKEN')

client.run(TOKEN)
