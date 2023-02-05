## Get Started
### クローン
```
git clone https://github.com/kanyamo/first_bot.git
cd first_bot
```
### 環境変数ファイルを作成する
```
echo "TOKEN = "your_token"" > .env
```
### 仮想環境を作る
```
python -m venv .venv
```
### 仮想環境を起動
``` 
# for Windows
.venv/Scripts/Activate.ps1

# for Mac, Linux
. .venv/bin/activate
```
### インストール
```
pip install -r requirements.txt
```
### 実行
```
python main.py
```