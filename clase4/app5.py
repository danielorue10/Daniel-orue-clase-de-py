#-*-coding:utf-8-*-
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def Unida():
    return 'Bienvenidos desde la clase de python'
if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
