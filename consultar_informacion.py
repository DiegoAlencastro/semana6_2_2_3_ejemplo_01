"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección pais de bddDAlencastro

db = client.bddDAlencastro
coleccion = db.pais

print("Datos de coleccion pais  ")
datos = coleccion.find()
for registro in datos:
    print(registro)
