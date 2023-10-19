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

def CrearProducto2(con):
    cursorOBJ = con.cursor()
    noIDprod = input("ingrese el codigo del producto: ")
    noIDprod = noIDprod.rjust(10)
    insertar = "INSERT INTO producto VALUES("+noIDprod+',"Chocorramo",80,"2023-10-9",1500.0,4000.0)'
    cursorOBJ.execute(insertar)

    con.commit()

def leerproducto():
    print("ingrese la siguiente informacion de producto")
    noIDProducto = input("id producto: ")
    noIDProducto = noIDProducto.rjust(10)
    nomProduct = input("nombre producto: ")
    UnidadMedida = input("Unidad de medidad: ") 
    fechaVencimiento = input("fecha vencimiento: ")
    precioCompra = input("precio compra: ")
    precioVenta = input("precio Venta: ")

    producto = (noIDProducto,nomProduct,UnidadMedida,fechaVencimiento,precioCompra,precioVenta)

    return producto


def CrearProducto3(con):
    cursorOBJ = con.cursor()
    insertar = "INSERT INTO producto VALUES(?,?,?,?,?,?)"
    cursorOBJ.execute(insertar, leerproducto()) # ingreso la cadena insertar y sus argumentos llamando la funcion leerproducto

    con.commit()

def actuProducNombre(con):
    cursorOBJ = con.cursor()
    nombre = input("ingrese el nuevo nombre: ")
   # actualizar = f'UPDATE producto SET nomProduct="{nombre}" WHERE noIDProducto = 1'
    actualizar = f'UPDATE producto SET nomProduct="{nombre}" WHERE noIDProducto IN (1,2)'
    cursorOBJ.execute(actualizar)

    con.commit()

def ConsultarProd(con):
    cursorOBJ = con.cursor()

    IDproducto = input("ingrese identificador producto: ")
    
    consulta = f'SELECT noIDProducto, nomProduct FROM producto WHERE noIDProducto = {IDproducto} '

    cursorOBJ.execute(consulta)

    filas = cursorOBJ.fetchall()
    
    for row in filas:
        idprod = row[0]
        nmprod = row[1]

        print("El numero de producto es : ", idprod)
        print("El nombre de producto es ", nmprod)
        #print(row)
    

def ConsultarProd2(con):
    cursorOBJ = con.cursor()

    IDproducto = input("ingrese identificador producto: ")
    
    consulta = f'SELECT COUNT(*) noIDProducto, nomProduct FROM producto WHERE noIDProducto = {IDproducto} '

    cursorOBJ.execute(consulta)

    filas = cursorOBJ.fetchall()
    
    for row in filas:
        contador = row[0]    
    
    print(contador)

def ConsultarProd3(con):
    cursorOBJ = con.cursor()
    
    consulta = 'SELECT SUM(precioVenta) FROM producto'

    cursorOBJ.execute(consulta)

    filas = cursorOBJ.fetchall()
    
    print(filas)

def  borrarProducto(con):
    cursorOBJ = con.cursor()

    IDProductoBorr = input("ingrese id producto a borrar: ")
    
    borrar = f'DELETE FROM producto WHERE noIDProducto ={IDProductoBorr}'

    cursorOBJ.execute(borrar)
    con.commit()

def  borrarTablaProd(con):
    cursorOBJ = con.cursor()

    borrar = 'DROP TABLE producto'

    cursorOBJ.execute(borrar)
    con.commit()


def main():
    DataBase = conexionDB()
    #CrearTablaProductos(DataBase)
    #CrearProducto3(DataBase)
    #actuProducNombre(DataBase)
    borrarTablaProd(DataBase)
    CerrarConexDB(DataBase)
    

main()
