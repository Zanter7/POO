import sqlite3

database = sqlite3.connect("prueba/delta.db") # comillas para seleccionar directorio

try:
    #crear tabla de datos con nombre articulos, atributos: codigo, descripcion, precio

    database.execute("""create table articulos ( 
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    
    print("se creo la tabla articulos") #confirmacion en terminal
except sqlite3.OperationalError:
    print("La tabla articulos ya existe") #excepcion ante el error
