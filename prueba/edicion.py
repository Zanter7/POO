import sqlite3

# conexion a la base de datos
database = sqlite3.connect("prueba/delta.db")


#ejecuta comando insert a la DB articulos en los campos descripcion y precio, con ? indica la posicion donde se inserta
# inserta una tupla a la posicion

database.execute("insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50))
database.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34))
database.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25))


database.commit() # guarda cambios
database.close() # cierra conexion