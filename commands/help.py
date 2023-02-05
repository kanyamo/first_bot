async def help(message):
    description = (
        "サブコマンド一覧\n"
        "`help`\n"
        "\tコマンドの使い方を表示します。\n"
        "`show`\n"
        "\tユーザーのプロフィールを表示します。第二引数にユーザーidを入力します。"
    )

    await message.channel.send(description)
