import discord
import os
from dotenv import load_dotenv
from commands.help import help
from commands.show import get_profile_by_id

# for test
# from models.music import Music

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

guild = discord.Object(id=int(os.getenv("GUILD_ID")))


@tree.command(
    name="profile",  # 入力するコマンド名
    description="プロフィールを表示します。",  # コマンドの説明
)
@discord.app_commands.describe(
    id="プロフィールを表示したいユーザーのidです。",  # コマンドの引数の説明
)
@discord.app_commands.guilds(guild)
async def profile(ctx: discord.Interaction, id: str) -> None:
    res = get_profile_by_id(id)
    await ctx.response.send_message(res)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await tree.sync(guild=guild)
    print('Done!')


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
                    await message.channel.send(get_profile_by_id(user_id))
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

# for test
# music = Music.from_id(1)
# print(music.difficulties)

TOKEN = os.getenv('TOKEN')

client.run(TOKEN)
