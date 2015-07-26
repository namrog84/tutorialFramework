from flask import Flask
from flask import render_template
from flask import Markup
app = Flask(__name__)

test = ""

@app.route("/")
def hello():
    
    #return "Hello World!<br>" + test
    return render_template('index.html', inject = test)

if __name__ == "__main__":
    f = open('test.txt', 'r')
    test = f.read()
    test = Markup("<br>".join(test.split()))
    app.run(host='0.0.0.0', port=8080, debug=False)
