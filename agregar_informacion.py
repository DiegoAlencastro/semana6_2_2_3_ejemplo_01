"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# Base de datos bddDAlencastro y coleccion pais

db = client.bddDAlencastro
coleccion = db.pais

# proceso que agrega una lista de documentos
listado = [
{"nombre": "Ecuador", "continente" : "Suramérica", "poblacion":"18408350"},
{"nombre": "Colombia", "continente" : "Suramérica", "poblacion":"52215503"},
{"nombre": "Perú", "continente" : "Suramérica", "poblacion":"33788589"}
]

coleccion.insert_many(listado)
