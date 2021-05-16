import eel
import search
from search import Order #Orderクラスをまとめて持ってくる
import desktop

app_name="html"
end_point="index.html"
size=(800,800)

order:Order #グローバル領域で変数を定義

# 関数名はmian_xのような名前はわかりずらいので非推奨。inpur_orderなどの処理と対応した命名がおすすめ

@ eel.expose
def main_1(csv_name):#メニューの登録処理
    global order# グローバル変数を使用するための宣言、これがないとローカル変数として扱われエラーになる
    ITEM_MASTER_CSV_PATH= './' + csv_name
    # CSVからマスタへ登録
    item_master = search.add_item_master_by_csv(ITEM_MASTER_CSV_PATH) 
    order = Order(item_master)# Orderクラスのインスタンスの作成

@ eel.expose
def main_2(buy_item_code,buy_item_count):#商品番号&個数入力する処理
    global order
    order.input_order(buy_item_code,buy_item_count)

@ eel.expose
def main_3():#購入する商品番号&個数表示する処理
    global order
    order.view_order() 

@ eel.expose
def main_4(change_money):#支払金額入力~お釣り受け取りまでの処理
    global order
    order.input_change_money(change_money)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)