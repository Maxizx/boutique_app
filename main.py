import tkinter
import customtkinter
from add_product import productos
from GUI import App

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.variable = "sin valor"
        self.title("app")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.formulario_de_carga)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def formulario_de_carga(self):
        #cargar foto
        #fecha
        ventana2 = tkinter.Toplevel()
        ventana2.title("Segunda ventana")
        ventana2.geometry("350x500")
        
        self.tipo = self.tipos_de_vestidos(ventana2,row=0, column=0,padx=20, pady=20,sticky="ew",columnspan=3,texto="Tipo")
        self.descripcion = self.campo_formulario(ventana2,texto="Descripcion",row=1,column=0,columnspan=3,sticky="ew")
        self.precio_alquiler = self.campo_formulario(ventana2,texto="Precio de Alquiler",row=2,column=0,columnspan=3,sticky="ew")
        self.precio_venta = self.campo_formulario(ventana2,texto="Precio de Venta",row=3,column=0,columnspan=3,sticky="ew")
        self.tallas_ = self.tallas(ventana2,row=4, column=0,padx=20, pady=20,sticky="ew",columnspan=3,texto="Tallas")

        self.btn = customtkinter.CTkButton(ventana2, text="Cargar", command= self.cargar)
        self.btn.grid(row=5, pady=20, columnspan=3, sticky="nsew")

    def cargar(self):
        print(f"{self.tipo.get()} + {self.descripcion.get()} + {self.precio_alquiler.get()} + {self.precio_venta.get()} + {self.tallas_.get()}")
        self.bd_prodcutos = productos(True,fecha_de_devolucion=0,imagen="nada",tipos_de_vestidos=self.tipo.get(),descripcion=self.descripcion.get(),talla=self.tallas_.get(),precio_de_venta=int(self.precio_venta.get()),precio_del_alquiler=int(self.precio_alquiler.get()))
        self.bd_prodcutos.agregar_productos()

    def campo_formulario(self,ventana,row:int,column:int,columnspan:int,padx=20,pady=20,sticky = "ew",texto = ""):
        self.nameLabel = customtkinter.CTkLabel(ventana,text=texto)
        self.nameLabel.grid(row=row, column=column,padx=padx, pady=pady,sticky=sticky)
        self.nameEntry = customtkinter.CTkEntry(ventana,placeholder_text=texto)
        self.nameEntry.grid(row=row, column=1+column,columnspan=columnspan, padx=padx,pady=pady, sticky="nsew")
        return self.nameEntry


    def tipos_de_vestidos(self,ventana,row:int,column:int,columnspan:int,padx=20,pady=20,sticky = "ew",texto = ""):
        self.nameLabel = customtkinter.CTkLabel(ventana,text=texto)
        self.nameLabel.grid(row=row, column=column,padx=padx, pady=pady,sticky=sticky)
        self.nameCombo = customtkinter.CTkComboBox(ventana,values=["15 años","damas","novia"])
        self.nameCombo.grid(row=row, column=1+column,columnspan=columnspan, padx=padx,pady=pady)
        return self.nameCombo
        


    def tallas(self,ventana,row:int,column:int,columnspan:int,padx=20,pady=20,sticky = "ew",texto = ""):
        self.nameLabel = customtkinter.CTkLabel(ventana,text=texto)
        self.nameLabel.grid(row=row, column=column,padx=padx, pady=pady,sticky=sticky)
        self.nameCombo = customtkinter.CTkComboBox(ventana,values=["S","M","L","X","XL","XXL"])
        self.nameCombo.grid(row=row, column=1+column,columnspan=columnspan, padx=padx,pady=pady)
        return self.nameCombo


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
