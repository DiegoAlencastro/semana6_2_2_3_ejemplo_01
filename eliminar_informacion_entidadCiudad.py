"""
    Eliminar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.bddDAlencastro
coleccion = db.ciudad

print("Borrar registros de una colección cuando paisPertenencia sea Ecuador")
coleccion.delete_many({'paisPertenencia':'Ecuador'})

print("Se muestra informacion")
datos = coleccion.find()
for registro in datos:
    print(registro)
