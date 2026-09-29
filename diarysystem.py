# diary_module.pyをインポート
from diary_module import diary, diarymanager
# my_toolbox.pyをインポート
from my_toolbox import multiline_input

# 変数を定義
title = '' ## 日記のタイトル用
body = '' ## 日記の本文用
dict_diaries = {} ## jsonから読み出した日記データ用

# diarymanagerのクラスを用いて日記をロード
diarydatas = diarymanager.load()

print('[タイトルを入力してください]')
title = input('> ')

# 複数行受け取れるinputで内容を受け取る
body = multiline_input('> ', '[内容を入力してください(空白改行で終了)]')

# 上で受け取ったtitleとbodyでdiaryクラスのオブジェクトを作成
newdiary = diary.Make(title,body)

# 受け取った日記データの中に新しく日記を追記
diarydatas.add(newdiary)

# 保存
diarydatas.save()