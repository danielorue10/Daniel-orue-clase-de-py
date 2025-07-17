from flask import Flask, jsonify, request

login = blueprint('login', __name__)

@login.route('/login', methods=['POST'])

def llamarserviciosSet():
    user= request.json.get('user')
    password = request.json.get('password')
    print(user, password)