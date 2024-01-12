import sqlite3
import random

class db_productos:
    def __init__(self) -> None:
        self.nombre_del_archivo = "productos.db"

    def crear_tabla(self):
        with sqlite3.connect(self.nombre_del_archivo) as conexion:
                conexion.execute("create table if not exists products (Alquilado BOOLEAN ,fecha TEXT,foto TEXT,tipo TEXT,descripcion TEXT,talla TEXT,alquiler INTEGER,venta INTEGER);")

    def agregar_datos(self,fecha ,foto ,tipo ,descripcion ,talla ,alquiler ,venta,alquilado = False ):
        with sqlite3.connect(self.nombre_del_archivo) as conexion:
            conexion.execute("insert into products(Alquilado ,fecha ,foto ,tipo ,descripcion ,talla ,alquiler ,venta) values (?,?,?,?,?,?,?,?)", (alquilado ,fecha ,foto ,tipo ,descripcion ,talla ,alquiler ,venta))
            conexion.commit()#

    def recibir_datos(self):
        with sqlite3.connect(self.nombre_del_archivo) as conexion:
            cursor = conexion.execute("SELECT player, score FROM products ORDER BY score DESC LIMIT 5;")
            lista = []
            for fila in cursor:
                lista.append(fila)
            return lista

foto_ = ["vestido","traje"]
tipos_= ["de 15 años","damas","novia"]
fecha_= ["13/4/98","2/7/25","3/5/30"]
descripcion_= ["es rojo con brillo","es verde con brillo","es azul con brillo"]
talla_ = ["S","M","XXL"]
alquiler_precio = random.randint(100,450)
venta_precio = random.randint(100,450)

foto = random.choice(foto_)
tipos = random.choice(tipos_)
fecha = random.choice(fecha_)
descripcion = random.choice(descripcion_)
talla = random.choice(talla_)


tabla = db_productos()
tabla.crear_tabla()

tabla.agregar_datos(foto=foto,fecha=fecha,tipo=tipos,descripcion=descripcion,talla=talla,alquiler=alquiler_precio,venta=venta_precio)