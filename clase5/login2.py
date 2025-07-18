def inicializacionVariables(user, password):
    userLocal = "admin"
    passwordLocal = "admin123"
    codRes = 'SIN_ERROR'
    menRes = 'OK'
    
    try:
        print("verificacion de Login")
        if password == passwordLocal and user == userLocal:
            accion = "LOGIN_OK"
        else:
            print("Error de Login")
            codRes = 'ERROR_LOGIN'
            menRes = 'Error de Login'
            accion = "LOGIN_ERROR"
    except Exception as e:
        print(f"Error en la verificación: {e}")
        codRes = 'ERROR_INTERNO'
        menRes = 'Error interno del servidor'
        accion = "LOGIN_ERROR"
    return codRes, menRes, accion
