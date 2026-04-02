import tkinter as tk
from PIL import Image, ImageTk
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
        self.root = root
        self.root.title("Cerpint Mayor - Panel de Control")
        # Obtener el ancho y alto de la pantalla disponible
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        # Ajustar la geometría restando unos píxeles para la barra de tareas
        self.root.geometry(f"{width}x{height-80}+0+0")
        # self.root.state('zoomed')
        self.root.resizable(False,False)
        self.root.configure(bg=COLOR_FONDO)
        self.create_layout()
    def create_layout(self):
        self.sidebar =tk.Frame(
            self.root,
            bg=COLOR_SLIDE,
            width=120
        )
        self.sidebar.pack(side='left', fill='y')
        self.sidebar.pack_propagate(False)

        # Contenedor principal
        self.content_area=tk.Frame(
            self.root,
            bg=COLOR_FONDO
        )
        self.content_area.pack(side="right", expand=True, fill="both")

        # Imagen de incio de Cerpint-Mayor
        

        # Botones de Sidebar
        # Botón de crear ventas
        self.btn_sale = tk.Button(
            self.sidebar,
            text="Venta",
            font=FUENTE_NORMAL,
            bg=COLOR_SECUNDARIO,
            fg="white",
            bd=3,
            relief="flat",
            overrelief="flat",
            activebackground="#1e7e34",
            activeforeground="white",
            cursor="hand2",
            anchor="center"
            
        )
        self.btn_sale.pack(side="top", fill="both", expand=True)

        # Boton de productos
        self.btn_products = tk.Button(
            self.sidebar,
            text="Productos",
            font=FUENTE_NORMAL,
            bg="DarkOrange1",
            fg="white",
            bd=3,
            relief="flat",
            overrelief="flat",
            activebackground="DarkOrange4",
            activeforeground="white",
            cursor="hand2",
            anchor="center"
        
        )
        self.btn_products.pack(side="top", fill="both", expand=True)

        # Boton de cliente
        self.btn_customer = tk.Button(
            self.sidebar,
            text="Cliente",
            font=FUENTE_NORMAL,
            bg=COLOR_PRIMARIO,
            fg="white",
            bd=3,
            relief="flat",
            overrelief="flat",
            activebackground="#281e7e",
            activeforeground="white",
            cursor="hand2",
            anchor="center"
            
        )
        self.btn_customer.pack(side="top", fill="both", expand=True)

        # Boton de asesor de venta
        self.btn_sales_advisors = tk.Button(
            self.sidebar,
            text="Vendedor",
            font=FUENTE_NORMAL,
            bg=COLOR_PRIMARIO,
            fg="white",
            bd=3,
            relief="flat",
            overrelief="flat",
            activebackground="#281e7e",
            activeforeground="white",
            cursor="hand2",
            anchor="center"
            
        )
        self.btn_sales_advisors.pack(side="top", fill="both", expand=True)

        # Boton de consultas
        self.btn_consult = tk.Button(
            self.sidebar,
            text="Consultas",
            font=FUENTE_NORMAL,
            bg="gold3",
            fg="white",
            bd=3,
            relief="flat",
            overrelief="flat",
            activebackground="gold4",
            activeforeground="white",
            cursor="hand2",
            anchor="center"
            
        )
        self.btn_consult.pack(side="top", fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = MainDashboard(root)
    root.mainloop()
