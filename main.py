import tkinter
import customtkinter
from add_product import productos

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("app")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.formulario_de_carga)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")




    def formulario_de_carga(self):
        #cargar foto
        #fecha
        ventana2 = tkinter.Toplevel()
        ventana2.title("Segunda ventana")
        ventana2.geometry("350x500")

        
        self.valor = self.tipos_de_vestidos(ventana2,row=0, column=0,padx=20, pady=20,sticky="ew",columnspan=3,texto="Tipo")
        self.valor1 = self.campo_formulario(ventana2,texto="Descripcion",row=1,column=0,columnspan=3,sticky="ew")
        self.valor2 = self.campo_formulario(ventana2,texto="Precio de Alquiler",row=2,column=0,columnspan=3,sticky="ew")
        self.valor3 = self.campo_formulario(ventana2,texto="Precio de Venta",row=3,column=0,columnspan=3,sticky="ew")
        self.valor4 = self.tallas(ventana2,row=4, column=0,padx=20, pady=20,sticky="ew",columnspan=3,texto="Tallas")

        self.btn = customtkinter.CTkButton(ventana2, text="Cargar", command= self.cargar)
        self.btn.grid(row=5, pady=20, columnspan=3, sticky="nsew")



    def cargar(self):
        print(f"{self.valor} + {self.valor1} + {self.valor2} + {self.valor3} + {self.valor4}")


    def campo_formulario(self,ventana,row:int,column:int,columnspan:int,padx=20,pady=20,sticky = "ew",texto = ""):
        self.nameLabel = customtkinter.CTkLabel(ventana,text=texto)
        self.nameLabel.grid(row=row, column=column,padx=padx, pady=pady,sticky=sticky)
        self.nameEntry = customtkinter.CTkEntry(ventana,placeholder_text=texto)
        self.nameEntry.grid(row=row, column=1+column,columnspan=columnspan, padx=padx,pady=pady, sticky=sticky)
        return self.nameEntry.get()

    def tipos_de_vestidos(self,ventana,row:int,column:int,columnspan:int,padx=20,pady=20,sticky = "ew",texto = ""):
        self.nameLabel = customtkinter.CTkLabel(ventana,text=texto)
        self.nameLabel.grid(row=row, column=column,padx=padx, pady=pady,sticky=sticky)
        self.nameCombo = customtkinter.CTkComboBox(ventana,values=["15 años","damas","novia"]).grid(row=row, column=1+column,columnspan=columnspan, padx=padx,pady=pady, sticky=sticky)
        


    def tallas(self,ventana,row:int,column:int,columnspan:int,padx=20,pady=20,sticky = "ew",texto = ""):
        self.nameLabel = customtkinter.CTkLabel(ventana,text=texto)
        self.nameLabel.grid(row=row, column=column,padx=padx, pady=pady,sticky=sticky)
        self.nameCombo = customtkinter.CTkComboBox(ventana,values=["S","M","L","X","XL","XXL"]).grid(row=row, column=1+column,columnspan=columnspan, padx=padx,pady=pady, sticky=sticky)


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
