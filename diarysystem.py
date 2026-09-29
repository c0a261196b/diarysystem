# diary_module.pyをインポート
from diary_module import diary, diarymanager
# その他のモジュールをインポート
import json
from pathlib import Path
from datetime import datetime

# 変数を定義
title = '' ## 日記のタイトル用
body = '' ## 日記の本文用
dict_diaries = {} ## jsonから読み出した日記データ用

diarydatas = diarymanager.load()


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

# 受け取った日記データの中に新しく日記を追記
diarydatas.add(newdiary)

# 保存
diarydatas.save()