class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def introduce(self):
        print(self.name)

    @classmethod
    def from_json(json):
        # jsonデータからインスタンスを生成するコードをここに記述する
        return User(id=0, name="name")

    @classmethod
    def from_id(id):
        # idデータをローカルに参照し、あればそれを、なければ新たに作成しインスタンスを返す
        return User(id=id, name="name")
