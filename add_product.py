from data_base import db_productos

class productos:
    def __init__(self,alquilado:bool ,fecha_de_devolucion:str ,imagen:str ,tipos_de_vestidos:str ,descripcion:str ,talla:str ,precio_del_alquiler:int,precio_de_venta:int) -> None:
        self.en_alquiler = alquilado
        self.foto  =  imagen
        self.tipos =  tipos_de_vestidos
        self.fecha =  fecha_de_devolucion
        self.descripcion =  descripcion
        self.talla  =  talla
        self.alquiler_precio = precio_del_alquiler
        self.venta_precio = precio_de_venta
        self.base_de_datos = db_productos()

    def agregar_productos(self):
        self.base_de_datos.agregar_datos(alquilado = self.en_alquiler,foto = self.foto ,tipo = self.tipos,fecha = self.fecha,descripcion = self.descripcion,talla = self.talla ,alquiler = self.alquiler_precio,venta = self.venta_precio)

    def cambiar_alquiler(self, esta_alquilado:bool):
        self.en_alquiler = esta_alquilado


