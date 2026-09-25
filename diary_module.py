# 色々とインポート
import json
from datetime import datetime
from pathlib import Path

# diaryクラスを定義
class diary:
    ## 構造を定義
    def __init__(self, title: str, body: str, tags: list, date: str, time: str):
        self.title = title
        self.body = body
        self.tags = tags
        self.date = date
        self.time = time

    ## print()などに直接投げた際の挙動を定義
    def __str__(self):
        title = self.title
        body = self.body
        tags = self.tags
        date = self.date
        time = self.time

        ## for文で複数個あるはずのtagsを加工
        tag = ""
        for i in range(len(tags)):
            if i != (len(tags) -1):
                tag += f'{tags[i]}, '
            else:
                tag += f'{tags[i]}'


        ## for文で改行混じりのbodyを加工
        body_texts = body.split('\n')
        bodydata = ''

        for j in range(len(body_texts)):
            if j != (len(body_texts) -1):
                bodydata += f'|{body_texts[j]}  [↓]\n'
            else:
                bodydata += f'|{body_texts[j]}  ]'
            
        return f'[{title} - {date} - {time} | tags:{tag}]\n{bodydata}'

    ## 自分に記録されている日記の内容をdictで返すための関数
    def to_dict(self):
        json_data = {
            'title': self.title,
            'date': self.date,
            'time': self.time,
            'body': self.body,
            'tags': self.tags
        }
        return json_data

    ## クラスメソッドたち
    ### class.Make(~内容~)で明示的に作る
    @classmethod
    def Make(cls, title: str, body: str, tags: list|None = None, date: str|None = None, time: str|None = None):
        
        if tags is None:
            tags = ['未定義']
    
        if date is None:
            date = datetime.now().strftime('%Y/%m/%d')
    
        if time is None:
            time = datetime.now().strftime('%H:%M:%S')

        return cls(title, body, tags, date, time)

    ### 直接辞書を突っ込んでdiaryを作るためのメソッド
    @classmethod
    def from_dict(cls, diary: dict):
        return cls(**diary)


### 以下はデバッグ用のテストコード

testdiary = diary.Make("テスト日記", "テスト用の内容です。\n改行もします。")
print(testdiary.title)
print(testdiary.date)
print(testdiary.time)
print(testdiary.body)
print(testdiary.tags)
print()
print(testdiary.to_dict())
print()
print(testdiary)
print()

testdict = {
    'title': 'テスト日記2',
    'date': '2026/09/99',
    'time': '11:22:40',
    'body': 'テスト用の内容その2です。',
    'tags': ['テスト1', 'test2']
}

testdiary_2 = diary.from_dict(testdict)

print(testdiary_2.title)
print(testdiary_2.date)
print(testdiary_2.time)
print(testdiary_2.body)
print(testdiary_2.tags)
print()
print(testdiary_2.to_dict())
print()
print(testdiary_2)
print()