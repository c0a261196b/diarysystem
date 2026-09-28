# diary_module.pyをインポート
from diary_module import diary
# その他のモジュールをインポート
import json
from pathlib import Path
from datetime import datetime

# 変数を定義
title = '' ## 日記のタイトル用
body = '' ## 日記の本文用
dict_diaries = {} ## jsonから読み出した日記データ用

# ファイルパスと日記を保存するjsonファイル名を定義
default_diarypath = Path('./diaries')
diaries_thisyear = default_diarypath / f'{datetime.now().strftime("%Y")}_diaries.json' ## (年度)_diaries.json

# ディレクトリとファイルの存在をチェック(無かったら新規作成)
Path.mkdir(default_diarypath, exist_ok=True)
Path.touch(diaries_thisyear)

# jsonファイルの構造をチェック
try:
    with diaries_thisyear.open() as f:
        dict_diaries = json.load(f)
except json.JSONDecodeError:
    pass ## 上ですでに空の辞書型で初期化しているため何もしなくてもOK


print('[タイトルを入力してください]')
title = input('> ')

# while-Trueで複数行受け取って'\n'.joinでつなげたものをbodyに入れることで複数行入力を実現
bodys = []
print('[内容を入力してください(空白改行で終了)]')
while True:
    bodyline = input('> ')
    if bodyline:
        bodys.append(bodyline)
    else:
        break
body = '\n'.join(bodys)

# 上で受け取ったtitleとbodyでdiaryクラスのオブジェクトを作成
newdiary = diary.Make(title,body)

# 受け取った辞書型の日記データの中に新しく日記を追記
recorded_date = f'{newdiary.date}_{newdiary.time}'
dict_diaries[recorded_date] = newdiary.to_dict()

# 書き込み処理
try:
    with diaries_thisyear.open('w') as f:
        json.dump(dict_diaries, f, ensure_ascii=False, indent=4)
except Exception as e:
    print(e)