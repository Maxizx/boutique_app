import customtkinter
import tkinter
from add_product import productos

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("app")

        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        pass


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
