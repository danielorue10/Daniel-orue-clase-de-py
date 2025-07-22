from flask import Blueprint, request, jsonify
from log import inicializacionVariables

login_bp = Blueprint('login_bp', __name__, url_prefix='/login')

@login_bp.route('/', methods=['POST'])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"code": 400, "message": "JSON inválido"}), 400

    user = data.get('user')
    password = data.get('password')

    if user == "daniel" and password == "123unida":
        return jsonify({"code": 200, "message": "Login OK", "action": "acceso concedido"})
    else:
        return jsonify({"code": 401, "message": "Credenciales inválidas", "action": "denegar_acceso"})
