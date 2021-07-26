from flask import Flask, render_template,request
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/about")
def about():
    return render_template("about.html")


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

if __name__ == "__main__":
    app.run(debug=True)

#render_template將會找尋html檔案傳送給使用者