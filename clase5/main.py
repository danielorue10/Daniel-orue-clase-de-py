from flask import Flask
from login_bp import login_bp  # Importa el blueprint del archivo login_bp.py

app = Flask(__name__)
app.register_blueprint(login_bp)

@app.route('/', methods=['GET'])
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
