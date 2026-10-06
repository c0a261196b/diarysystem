# diary_module.pyをインポート
from diary_module import diary, diarymanager
# my_toolbox.pyをインポート
from my_toolbox import multiline_input, menumaker, flag_maker

# 変数を定義
title = '' ## 日記のタイトル用
body = '' ## 日記の本文用
dict_diaries = {} ## jsonから読み出した日記データ用

# diarymanagerのクラスを用いて日記をロード
diarydatas = diarymanager.load()

# メニュー一覧用のlistを作成
menu_list = [
    '[日記の記録]',
    '[日記の閲覧]',
    '[日記の削除]',
]

while True:
    # メニューを表示
    choosen = menumaker('[実行する機能を選択してください]', menu_list, "> ", exit_option=True)

    match choosen:

        # 選ぶと終了
        case 'end':
            print('[終了します]')
            break

        # 記録機能
        case 1:
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

        # 閲覧機能
        case 2:
            # メニュー用の一覧を作成
            diary_menus = [f'[{a} - {b}]' for a, b in zip(diarydatas.diary_titles, diarydatas.diary_keys)]
            while True:           
                # メニューを表示 
                diary_select = menumaker('[閲覧する日記のタイトルを選択してください]', diary_menus, "> ", exit_option=True, exit_opt_text='[戻る]')

                # メニューで「戻る」が選ばれたらこのループをbreakして戻る
                if diary_select == 'end':
                    break

                # インデックスから日記を探して出力
                print(diarydatas.show_diary(diary_select-1))

                # 続けて閲覧するかを聞く
                continueflag = flag_maker('[続けて閲覧しますか?(y/n)]', '> ')
                if not continueflag:
                    break
        
        # 削除機能
        case 3:
            while True:
                # メニュー用の一覧を作成
                diary_menus = [f'[{a} - {b}]' for a, b in zip(diarydatas.diary_titles, diarydatas.diary_keys)]
            
                # 削除用のフラグ変数を初期化
                rm_flag = False
                rm_flag_2 = False

                # メニューを表示 
                diary_select = menumaker('[削除する日記のタイトルを選択してください]', diary_menus, "> ", exit_option=True, exit_opt_text='[戻る]')

                # メニューで「戻る」が選ばれたらこのループをbreakして戻る
                if diary_select == 'end':
                    break

                # インデックスから日記を探して出力
                print(diarydatas.show_diary(diary_select-1))
                rm_flag = flag_maker('[この日記を削除しますか?(y/n)]', '> ')
                if rm_flag:
                    rm_flag_2 = flag_maker('[本当ですね?(この選択で削除が確定します)(y/n)]', '> ')
                    
                if rm_flag and rm_flag_2:
                    diarydatas.remove(diary_select-1)
                    diarydatas.save()
                    print('[削除しました]')
                else:
                    print('[削除がキャンセルされました]')

                # 続けて削除するかを聞く
                continueflag = flag_maker('[ほかに削除する日記はありますか?(y/n)]', '> ')
                if not continueflag:
                    break

        case _:
            pass