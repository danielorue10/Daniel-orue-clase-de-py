#!/usr/bin/env python3
from flask import Flask
from login import login 
  

app = Flask(__name__)

##servicios rest

app.register_blueprint(login)

@app.route('/', methods=['GET'])
def helloo():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host= '0.0.0.0', port=5000, debug=True,use_reloader=True)