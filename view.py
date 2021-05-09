import eel
import search
import desktop

app_name="html"
end_point="index.html"
size=(800,800)

@ eel.expose
def main(csv_name,buy_item_code,buy_item_count,change_money):
    search.main(csv_name,buy_item_code,buy_item_count,change_money)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)