# 関数たち
## 複数行受け取って返すだけの関数
def multiline_input(decoration:str = '', before_input: str = ''):
    ## 変数を定義
    input_str = ""
    multi_str = []
    output_str = ""

    ## 文字を入力させる前に一行分何かを表示する機能
    ## 何も入力されなかったらprintを実行せずすっ飛ばす
    if before_input:
        print(before_input)

    ## while Trueでinputをひたすら繰り返し、multi_strのlistに格納する
    ## この時のinputの装飾に↑のdecorationがつかわれる
    while True:
        input_str = input(decoration)
        if input_str:
            multi_str.append(input_str)
        else:
            break

    ## 改行でつなげて一つのstrにする
    output_str = '\n'.join(multi_str)

    return output_str
    
def menumaker(what_will: str, menu_list: list[str], decoration:str = '', exit_option:bool = False, exit_opt_text:str = '[終了]', start_over: str = '[もう一度選んでください]'):
    print(what_will)
    menu_line = enumerate(menu_list, 1)
    for i, j in menu_line:
        print(f'{i}) {j}')
    
    if exit_option:
        print(f'{len(menu_list)+1}) {exit_opt_text}')

    while True:
        try:
            choosen = int(input(decoration))
        except ValueError:
            print('[数字以外が入力されました]')
            print(start_over)
            continue
        if 0 < choosen <= len(menu_list):
            break
        elif choosen == len(menu_list)+1 and exit_option:
            choosen = 'end'
            break
        else:
            print('[メニュー範囲外です]')
            print(start_over)
    return choosen

def flag_maker(text: str, decoration: str = '', errormsg: str = '[yesかnoを識別できる文字を入力して下さい]'):
    print(text, end="")
    while True:
        yesno = input(decoration).lower()
        if yesno in ['y', 'yes']:
            return True  
        elif yesno in ['n', 'no']:
            return False
        else:
            print(errormsg, end='')