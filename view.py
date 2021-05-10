import eel
import search
import desktop

app_name="html"
end_point="index.html"
size=(800,800)

@ eel.expose
def main_1(csv_name):
    search.main_1(csv_name)

@ eel.expose
def main_2(buy_item_code,buy_item_count):
    search.main_2(buy_item_code,buy_item_count)

@ eel.expose
def main_3():
    search.main_3()

@ eel.expose
def main_4(pay_money):
    search.main_4(pay_money)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)