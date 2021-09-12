from flask import Flask, render_template, request
from datetime import datetime
import main
app = Flask(__name__)
 
@app.route('/')
def default():
    return render_template('post.html')

@app.route('/post', methods=['POST'])
def post():
    value = {}
    print(request.form)
    value["pet"] = request.form["pet"]
    value["age"] = (datetime.now() - datetime.strptime(request.form["date"],'%Y-%m-%d') ).days // 30
    value["alg"] = list(map(str, request.form.getlist('alg')))
    value["flavor"] = list(map(str, request.form.getlist('flavor')))
    value["when"] = list(map(str, request.form.getlist('when')))
    general, natural = main.filter_petfood(value)
    val = "일반식"
    for a in general:
        val += "<br>" + a["name"]
    val+= "<br><br> 자연식"
    
    for a in natural:
        val += "<br>" + a["name"]
    return val
if __name__ == '__main__':
    app.run(host="0.0.0.0")


