# 関数たち
## 複数行受け取って返すだけの関数
def multiline_input(decoration:str = "", before_input: str = ""):
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
    
        
