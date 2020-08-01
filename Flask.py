from flask import Flask, render_template
from flask import make_response
from flask import request, jsonify
from Control import test01 as T


app = Flask(__name__)
PORT = 5000
DEBUG = False


@app.route("/")
def raiz():
    return render_template('index2.html',nombre=T.nombre)
    # return 'Kevin developer sitio enviroment'


if __name__ == '__main__':
    app.run(debug=True)
