from flask import Flask,request, jsonify
from cliente import buscar_clientes

app = Flask(__name__)

@app.route('/cliente', methods=['POST'])
def obtener_clientes():
        data= request.get_json()
        if not data or "ci" not in data:
              return jsonify ({
        "codRes" : "ERROR",
	"menrRes" : "Error cliente",
      "ci" : data.get("ci", "NO enviado" )
               }), 400
        
        ci = data["ci"]
        cliente = buscar_clientes(ci)

        if cliente:
              return jsonify({
                    "accion": "succes",
                    "codRes": "SIN ERROR",
                    "menRes": "OK",
                    "ci": cliente ["ci"],
                    "nombre": cliente ["nombre"],
                    "apellido": cliente ["apellidos"],
                    })
        else: 
              return jsonify ({"accion":"cliente no esta en el sistema"})
        

    #return "Hello World! desde la unida xD"

if __name__ == '__main__':
    app.run(host='localhost', port=5003,debug= True )
