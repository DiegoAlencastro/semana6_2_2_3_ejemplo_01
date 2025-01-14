"""
    Eliminar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.bddDAlencastro
coleccion = db.pais

print("Borrar registros de una colección cuando continente sea Suramérica")
coleccion.delete_many({'continente':'Suramérica'})

print("Se muestra informacion")
datos = coleccion.find()
for registro in datos:
    print(registro)
