from flask import Flask,request
import json
from bs4 import BeautifulSoup
import requests
############################################################
app = Flask(__name__)
###########################หน้าแรก################################
@app.route('/')
def index():
    return "Hi Welcome to python page"
#################################หน้าราคาหุ้น###############################
@app.route('/getquote', methods=['GET'])
def getquote():
    symbol_param = request.args.get("symbol")
    url = "https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol="+symbol_param+"&ssoPageId=9&selectPage=1"
    res = requests.get(url)
    res.encoding = "tis-620"
    soup = BeautifulSoup(res.text, 'html.parser')
    #####หาชื่อหุ้นและเวลาอัพเดท#######
    data_span = soup.find_all('span')
    span_list = []
    for data_spans in data_span:
        obj_span = data_spans.string
        span_list.append(obj_span)
    last_update = span_list[22]
    symbol = span_list[24]

    ######หาราคาล่าสุดและการเปลี่ยนแปลง#####
    data_h1 = soup.find_all('h1')
    h1_list = []
    for data_h1s in data_h1:
        obj_h1 = data_h1s.text
        h1_list.append(obj_h1)
    last_price = h1_list[1].strip()
    price_chg = h1_list[2].strip()
    percent_chg = h1_list[3].strip()

    stock_return = {"symbol": symbol, "lastupdate": last_update, "lastprice": last_price, "pricechange": price_chg,
                    "percentchange": percent_chg}

    return json.dumps(stock_return)

if __name__ == '__main__':
    app.run()