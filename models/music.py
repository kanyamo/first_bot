import json
from .music_difficulty import MusicDifficulty


class Music:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.difficulties = MusicDifficulty.from_music_id(self.id)

    # idから曲の情報を取得してインスタンスを生成する関数
    @classmethod
    def from_id(self, id):
        # ここでjsonから情報を取得する
        with open('repositories/musics.json', 'r') as json_open:
            json_load = json.load(json_open)
            music_data = list(
                filter(lambda music: music["id"] == id, json_load))
            if music_data:
                music_data = music_data[0]
                return Music(id=id, title=music_data["title"])
        return Music(id=0, title="not found")
