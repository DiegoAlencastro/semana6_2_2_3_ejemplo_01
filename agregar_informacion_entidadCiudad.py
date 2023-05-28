"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# Base de datos bddDAlencastro y coleccion ciudad

db = client.bddDAlencastro
coleccion = db.ciudad

# proceso que agrega una lista de documentos
listado = [
{"nombre": "Quito", "paisPertenencia" : "Ecuador", "densidadPoblacional":"7469,5"},
{"nombre": "Cuenca", "paisPertenencia" : "Ecuador", "densidadPoblacional":"5832"},
{"nombre": "Bogota", "paisPertenencia" : "Colombia", "densidadPoblacional":"4907,45"},
{"nombre": "Lima", "paisPertenencia" : "Perú", "densidadPoblacional":"3620,94"}
]

coleccion.insert_many(listado)
