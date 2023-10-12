import sqlite3

def conexionDB(): #Establecer conexion con la DB
    try:
        con = sqlite3.connect("Clases/BaseDatos.db")
        return con
    
    except sqlite3.Error:
        print(sqlite3.Error)

def CerrarConexDB(con): #Termina conexion con la DB
    con.close()

def CrearTablaProductos(con):
    cursorOBJ = con.cursor()

    crear = """ CREATE TABLE IF NOT EXISTS producto(
    noIDProducto integer NOT NULL,
    nomProduct text NOT NULL,
    UnidadMedida float NOT NULL,
    fechaVencimiento date NOT NULL,
    precioCompra float NOT NULL,
    precioVenta float NOT NULL,
    PRIMARY KEY(noIDProducto))
    """

    cursorOBJ.execute(crear)

    con.commit()

def CrearProducto(con):
    cursorOBJ = con.cursor()

    insertar = """ INSERT INTO producto VALUES(
    1,
    "Chocorramo",
    80,
    "2023-10-9",
    1500.0,
    4000.0
    )
    """

    cursorOBJ.execute(insertar)

    con.commit()

def main():
    DataBase = conexionDB()
    #CrearTablaProductos(DataBase)
    CrearProducto(DataBase)
    CerrarConexDB(DataBase)

main()
print("qe")
