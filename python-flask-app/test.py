from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello, World!</h1>'

@app.route('/haoyun')
def haoyun():
    return "<h1>Hello, Haoyun</h1>"

#使用POST和GET方法，可隨意在/home/目錄下，輸入文字名稱進入不同頁面
@app.route('/home', methods=['POST', 'GET'], defaults={'name' : 'Default'}) 

#輸入的內容將被轉成字串，使用POST和GET方法，且為動態網址
@app.route('/home/<string:name>', methods=['POST', 'GET'])
def home(name):
    return '<h1>Hello {}, you are on the home page!</h1>'.format(name)

#呈現JSON資料
@app.route('/json')
def json():
    return jsonify({'key' : 'value', 'listkey' : [1,2,3]})

#查詢頁query
@app.route('/query')
def query():
    name = request.args.get('name')
    location = request.args.get('location')
    return '<h1>Hi {}. You are from {}. You are on the query page!</h1>'.format(name, location)

#透過表格傳送資料，產生動態結果　
@app.route('/theform')
def theform():
    return '''<form method="POST" action="/process">
                  <input type="text" name="name">
                  <input type="text" name="location">
                  <input type="submit" value="Submit">
              </form>'''
@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    location = request.form['location']
    return '<h1>Hello {}. You are from {}. You have submitted the form successfully!<h1>'.format(name, location)

#傳送JSON資料，使網頁產生變化
@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()
    name = data['name']
    location = data['location']
    randomlist = data['randomlist']
    return jsonify({'result' : 'Success!', 'name' : name, 'location' : location, 'randomkeyinlist' : randomlist[1]})

if __name__ == "__main__":
    app.run(debug=True)

#CMD執行 python main.py
#debug=True時，一修改程式存檔，它就會自動reload
#瀏覽器網址列輸入 localhost:8000(預設port為5000，可調整至其他數字)
#加入thread參數，可以一次處理多個request