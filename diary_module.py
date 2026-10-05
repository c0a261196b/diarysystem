# 色々とインポート
import json
from datetime import datetime
from pathlib import Path

# diaryクラスを定義
class diary:
    ## 構造を定義
    def __init__(self, title: str, body: str, tags: list, date: str, time: str):
        self.title = title # タイトル
        self.body = body # 日記の内容
        self.tags = tags # 日記のタグ
        self.date = date # 日記を書いた日付(年も含む)
        self.time = time # 日記を書いた時間(時分秒)

    ## 辞書のキーを何もせずとも呼び出せるようにする
    ## 形式は「"YYYY/MM/DD_HH:mm:ss"」
    @property
    def dictkey(self):
        return f'{self.date}_{self.time}'
    

    ## print()などに直接投げた際の挙動を定義
    def __str__(self):
        title = self.title
        body = self.body
        tags = self.tags
        date = self.date
        time = self.time

        ## tagsをjoin()とrstrip()で加工
        tag = ", ".join(tags).rstrip()

        ## for文で改行混じりのbodyを加工
        body_texts = body.split('\n')
        bodydata = ''

        for j in range(len(body_texts)):
            if j != (len(body_texts) -1):
                bodydata += f'|{body_texts[j]}  [↓]\n'
            else:
                bodydata += f'|{body_texts[j]}'
            
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
        return cls.Make(**diary)

# ファイルを読み込むいろいろ
class diarymanager():
    ## 構造を設定
    def __init__(self, path: str | Path = "", diarydata: dict = {}):
        self.path = Path(path)
        self.diary_datas = diarydata
        self.diary_keys = list(diarydata.keys()) ## 辞書のキーをインデックスしておく
        self.diary_titles = []
        for i in self.diary_keys:
            self.diary_titles.append(self.diary_datas[i]['title'])


    ## 読み込んだ日記データのdictに新しい日記を追記する処理
    def add(self, data: diary):
        newdiary_entry = data.to_dict()
        newdiary_dictkey = data.dictkey

        self.diary_datas[newdiary_dictkey] = newdiary_entry
        self.diary_keys.append(newdiary_dictkey)
        self.diary_titles.append(data.title)

    def save(self):
        filepath = self.path
        diaries_data = self.diary_datas

        try:
            with filepath.open('w') as f:
                json.dump(diaries_data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            raise Exception(e)


    ## インデックス番号だけからdiaryクラスを作成する処理
    def show_diary(self, index):
        ### 自身からdiaryのキーと辞書を引っ張ってくる
        diary_keys = self.diary_keys
        diary_dicts = self.diary_datas

        return diary.from_dict(diary_dicts[diary_keys[index]])


    ## クラスメソッドたち
    ### 明確にクラスを作るためのもの
    @classmethod
    def load(cls, path: str = "./diaries", year: str = "0", month: str = "0"):
        this_year = datetime.now().strftime('%Y')
        this_month = datetime.now().strftime('%m')
        dirpath = Path(path)
        diarydata = {}

        ### yearの中身の長さが4以外 = 年度として使うには不適切ならとりあえず今年のを入れる
        if len(year) != 4:
            year = this_year

        ### monthに対しては1~12の範囲に収まっててほしいので [↓]
        ### それ以外の範囲をいれたら容赦なく矯正しつつ、1~9は0埋めする
        try:
            month_int = int(month)
            if 1 <= month_int <= 12:
                month = month.zfill(2)
            else:
                month = this_month

        ### 適当な文字とかを入れられたらこっちも矯正
        except ValueError:
            month = this_month

        ### デフォルトの保存パスにmonthの文字列をつなげて「dirpath / month」という構造を作る
        dirpath /= year

        ### ファイルの存在チェック(なかったら作成)
        ### 二行目はpathlibの/結合を使って読み込みたいファイル名も含めたPathを作っている
        dirpath.mkdir(parents=True, exist_ok=True)
        filepath = dirpath / f'{year}_{month}_diaries.json'

        ### ファイルがなかったら新規作成しつつ、その中に空のjsonを書き込む
        if not filepath.exists():
            with filepath.open('w') as f:
                json.dump({}, f)

        ### json.load()を用いて辞書型でdiariesの内容を取り出す
        try:
            with filepath.open() as f:
                diarydata = json.load(f)
        except json.JSONDecodeError as e:
            ### classとして扱う都合上読み込みエラーが起きた段階で止めないと [↓]
            ### (まだ残っている情報を)ほかのメソッドで壊しかねないので止める
            print('[読み込みエラーが発生しました]')
            raise Exception(e)
        except Exception as e:
            print('[未知のエラーが発生しました]')
            raise Exception(e)

        return cls(filepath, diarydata)




### 以下はデバッグ用のテストコード
if __name__ == '__main__':
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

    diaries_test = diarymanager.load()
    print(diaries_test)
    print(diaries_test.path)
    print(diaries_test.diary_datas)
    print(diaries_test.diary_keys)
    print(diaries_test.diary_titles)
    