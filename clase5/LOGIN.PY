from flask import Blueprint, request, jsonify

login = Blueprint('login', __name__)

@login.route('/login', methods=['POST'])
def llamarservicioset():
    user =request.json.get('user')
    password = request.json.get('password')
    
    codeRes, menRes, accion = inicializacionVariables(user, password)
    
    salida = {
        "code": codeRes,
        "message": menRes,
        "action": accion
    }
    return jsonify(salida)

def inicializacionVariables(user, password):
    # Dummy implementation, replace with your actual logic
    if user == "admin" and password == "admin":
        return 200, "Login successful", "grant_access"
    else:
        return 401, "Invalid credentials", "deny_access"
