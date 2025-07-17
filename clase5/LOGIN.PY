from flask import Flask, jsonify, request, Blueprint

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def llamarservicioSet():
    user = request.json.get('user')
    password = request.json.get('password')
    print(user, password)
