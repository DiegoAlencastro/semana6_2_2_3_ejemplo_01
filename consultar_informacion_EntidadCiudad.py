"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección ciudad de bddDAlencastro

db = client.bddDAlencastro
coleccion = db.ciudad

print("Datos de coleccion ciudad")
datos = coleccion.find()
for registro in datos:
    print(registro)

