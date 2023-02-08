import json


class MusicDifficulty:
    def __init__(self, id, music_id) -> None:
        self.id = id
        self.music_id = music_id

    @classmethod
    def from_music_id(self, music_id):
        with open("repositories/musicDifficulties.json", "r") as json_open:
            json_load = json.load(json_open)
            music_difficulty_json_list = list(
                filter(lambda music_difficulty: music_difficulty["musicId"] == music_id, json_load))
            return [
                MusicDifficulty.from_json(
                    music_difficulty_json
                )

                for music_difficulty_json in music_difficulty_json_list
            ]

    @classmethod
    def from_json(self, json_data):
        return MusicDifficulty(id=json_data["id"], music_id=json_data["musicId"])
