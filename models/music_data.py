from music import Music
from user import User

class MusicData:
    def __init__(self, music_id, user_id) -> None:
        self.music = Music.from_id(music_id)
        self.user = User.from_id(user_id)
    