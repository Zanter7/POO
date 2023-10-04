import sqlite3
import random

# conexion a la base de datos
database = sqlite3.connect("prueba/delta.db")


#ejecuta comando insert a la DB articulos en los campos descripcion y precio, con ? indica la posicion donde se inserta
# inserta una tupla a la posicion


def letrazar():
    abecedario =['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
    'v', 'w', 'x', 'y', 'z']

    nivel = random.randint(3,10)

    nombre = ""

    for i in range(nivel):
        nombre+= abecedario[random.randint(0,len(abecedario))-1]
        
    return nombre


for i in range(20):
    database.execute("insert into articulos(descripcion,precio) values (?,?)", (letrazar(), random.randint(0,500)))



database.commit() # guarda cambios
database.close() # cierra conexion
