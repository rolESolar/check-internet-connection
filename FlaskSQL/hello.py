# Python Flask Tutorial

from flask import Flask, url_for, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', fantasie = "Tutorials", param = 50)

@app.route("/login", methods=['POST', 'GET'])
def login():
    if request.method =='POST':
        name = request.form['name']
    else:
        name = request.args.get('name')    
    return "<h1>Hello " + name + "</h1>"

if __name__ == '__main__':
    app.run(port=1337, debug=True)