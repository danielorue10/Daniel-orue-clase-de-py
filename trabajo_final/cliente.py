#clientes en py

clientes = [ {

"ci" : "6951569",
	"nombre" : "Daniel",
	"apellido": "Orue Barrios",



}  ]

def buscar_clientes (ci):
    for cliente in clientes:
        if cliente [ "ci"] == ci:
            return cliente
        
#return None
