import pandas as pd
import eel
import sys
import datetime

def kimetsu_search(word,csv_name):
    # 検索対象取得
    df=pd.read_csv("./{}".format(csv_name))
    source=list(df["name"])

    if word in source:
        print('{}が見つかりました'.format(word))
        eel.view_log_js("『{}』が見つかりました".format(word))
    else:
        print('{}は見つかりませんでした'.format(word))
        #リストになかった場合に、キャラクターを(source)追加出来るようにする
        eel.view_log_js("『{}』は見つかりませんでした".format(word))
        add = input('キャラクターを新規に登録しますか？　登録する→0　登録しない→1>>>')
        if add == '0':
            source.append(word)
            print('キャラクターを追加しました')
            eel.view_log_js("『{}』を追加しました".format(word))
        else:
            print('追加しませんでした')
            eel.view_log_js("『{}』を追加しませんでした".format(word))

    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./{}".format(csv_name),encoding="utf_8-sig")
    print(source)