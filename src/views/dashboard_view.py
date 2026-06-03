import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from src.views.components.menu_buttons import MenuButton
from src.controllers.customer_controller import CustomerController
from src.utils.settings import (
    COLOR_FONDO,
    COLOR_TEXTO,
    FUENTE_TITULO,
    FUENTE_NORMAL,
    COLOR_PRIMARIO,
    COLOR_SECUNDARIO,
    COLOR_SLIDE
)

class MainDashboard:

    def __init__(self, root):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.root = root
        self.root.title("Cerpint Mayor - Panel de Control")
        # Obtener el ancho y alto de la pantalla disponible
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        # Ajustar la geometría restando unos píxeles para la barra de tareas
        self.root.geometry(f"{width}x{height-80}+0+0")
        self.root.resizable(False,False)
        self.root.configure(bg=COLOR_FONDO)
        self.create_layout()
        self.customer_ctrl = CustomerController(self.content_area)
    def create_layout(self):
        self.sidebar =tk.Frame(
            self.root,
            bg=COLOR_SLIDE,
            width=200
        )
        self.sidebar.pack(side='left', fill='y')
        self.sidebar.pack_propagate(False)

        # Contenedor principal
        self.content_area=tk.Frame(
            self.root,
            bg=COLOR_FONDO
        )
        self.content_area.pack(side="right", expand=True, fill="both")

        # Imagen de fondo de Bienvenida de Panel
        try:
            self.original_logo=Image.open("assets/logo.png")
            self.resized_logo=self.original_logo.resize((500,400), Image.LANCZOS)
            self.final_logo_img=ImageTk.PhotoImage(self.resized_logo)
            self.lbl_welcome_logo=tk.Label(
                self.content_area,
                image=self.final_logo_img,
                bg=COLOR_FONDO
            )
            self.lbl_welcome_logo.place(relx=0.5, rely=0.5, anchor="center")
        except FileNotFoundError:
            print("Error: no se encontro la imagen del logo")
            self.lbl_fallback=tk.Label(self.content_area, text="Bienvenido a cerpint")
            self.lbl_fallback.place(relx=0.5, rely=0.5, anchor="center")            

        # Botones de Sidebar
        MenuButton(self.sidebar, "📈  VENTA", "#91D06C", self.show_sales)
        MenuButton(self.sidebar, "📦  PRODUCTOS", "#FFA239", self.show_product)
        MenuButton(self.sidebar, "👥  CLIENTE", "#5A9CB5", self.show_customers)
        MenuButton(self.sidebar, "👔  VENDEDOR", "#5A9CB5", self.show_sellers)
        MenuButton(self.sidebar, "🔍  CONSULTAS", "#FFD41D", self.show_consults)

    # Estos los dejas vacíos por ahora para que no den error
    def show_sales(self): self.clear_content()
    def show_product(self):self.clear_content()
    def show_customers(self):self.customer_ctrl.display_view()
    def show_sellers(self): self.clear_content()
    def show_consults(self): self.clear_content()  


if __name__ == "__main__":
    root = tk.Tk()
    app = MainDashboard(root)
    root.mainloop()
