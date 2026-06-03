import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from src.views.components.menu_buttons import MenuButton
from src.controllers.inventory_controller import InventoryController
from src.controllers.customer_controller import CustomerController
from src.controllers.sales_controller import SalesController
from src.controllers.sellers_controller import SellersController
from src.controllers.consults_controller import ConsultsController
from src.utils.settings import (
    APP_MODE,
    COLOR_BLANCO,
    COLOR_FONDO,
    COLOR_PRIMARIO,
    COLOR_SECUNDARIO,
    COLOR_THEME,
    COLOR_TEXTO,
    COLOR_TEXT_SECONDARY,
    COLOR_BORDE,
    COLOR_SIDEBAR_SEPARATOR,
    COLOR_SLIDE,
    FUENTE_NORMAL,
    FUENTE_TITULO,
    MENU_HOVER_CLIENTS,
    MENU_HOVER_CONSULTS,
    MENU_HOVER_PRODUCTS,
    MENU_HOVER_SALES,
    MENU_HOVER_SELLERS,
)


class MainDashboard:

    def __init__(self, root):
        ctk.set_appearance_mode(APP_MODE)
        ctk.set_default_color_theme(COLOR_THEME)
        self.root = root
        self.root.title("Cerpint Mayor - Panel de Control")
        # Obtener el ancho y alto de la pantalla disponible
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        # Ajustar la geometría restando unos píxeles para la barra de tareas
        self.root.geometry(f"{width}x{height-80}+0+0")
        self.root.resizable(False, False)
        self.root.configure(bg=COLOR_FONDO)
        self.create_layout()
        self.customer_ctrl = CustomerController(self.content_area)
        self.inventory_ctrl = InventoryController(self.content_area)
        self.sales_ctrl = SalesController(self.content_area)
        self.sellers_ctrl = SellersController(self.content_area)
        self.consults_ctrl = ConsultsController(self.content_area)

    def create_layout(self):
        self.sidebar = ctk.CTkFrame(
            self.root,
            fg_color=COLOR_SLIDE,
            width=260,
            corner_radius=30,
        )
        self.sidebar.pack(side="left", fill="y", padx=(15, 0), pady=15)
        self.sidebar.pack_propagate(False)

        self.sidebar_header = ctk.CTkFrame(
            self.sidebar,
            fg_color=COLOR_SLIDE,
            corner_radius=20,
        )
        self.sidebar_header.pack(fill="x", padx=18, pady=(20, 10))

        self.sidebar_title = ctk.CTkLabel(
            self.sidebar_header,
            text="Cerpint Mayor",
            font=(FUENTE_TITULO[0], 18, "bold"),
            text_color=COLOR_TEXTO,
            anchor="w",
        )
        self.sidebar_title.pack(fill="x", padx=12, pady=(18, 18))

        self.sidebar_separator = ctk.CTkFrame(
            self.sidebar,
            fg_color=COLOR_SIDEBAR_SEPARATOR,
            height=1,
        )
        self.sidebar_separator.pack(fill="x", padx=18, pady=(0, 20))

        self.content_area = ctk.CTkFrame(
            self.root,
            fg_color=COLOR_FONDO,
        )
        self.content_area.pack(
            side="right", expand=True, fill="both", padx=(0, 15), pady=15
        )

        self.page_frame = ctk.CTkFrame(
            self.content_area,
            fg_color=COLOR_BLANCO,
            corner_radius=25,
            border_width=1,
            border_color=COLOR_BORDE,
        )
        self.page_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.dashboard_title = ctk.CTkLabel(
            self.page_frame,
            text="Bienvenido al panel",
            font=(FUENTE_TITULO[0], 24, "bold"),
            text_color=COLOR_TEXTO,
            anchor="w",
        )
        self.dashboard_title.pack(fill="x", padx=20, pady=(24, 5))

        self.dashboard_subtitle = ctk.CTkLabel(
            self.page_frame,
            text="Selecciona una sección del menú para comenzar.",
            font=(FUENTE_NORMAL[0], 13),
            text_color=COLOR_TEXT_SECONDARY,
            anchor="w",
        )
        self.dashboard_subtitle.pack(fill="x", padx=20, pady=(0, 18))

        try:
            self.original_logo = Image.open("assets/logo.png")
            self.resized_logo = self.original_logo.resize((420, 330), Image.LANCZOS)
            self.final_logo_img = ImageTk.PhotoImage(self.resized_logo)
            self.lbl_welcome_logo = ctk.CTkLabel(
                self.page_frame,
                image=self.final_logo_img,
                text="",
            )
            self.lbl_welcome_logo.place(relx=0.5, rely=0.55, anchor="center")
        except FileNotFoundError:
            print("Error: no se encontro la imagen del logo")
            self.lbl_fallback = ctk.CTkLabel(
                self.page_frame,
                text="Bienvenido a Cerpint Mayor",
                font=(FUENTE_TITULO[0], 20, "bold"),
                text_color=COLOR_TEXTO,
            )
            self.lbl_fallback.place(relx=0.5, rely=0.5, anchor="center")

        MenuButton(self.sidebar, "📈  VENTA", MENU_HOVER_SALES, self.show_sales)
        MenuButton(
            self.sidebar, "📦  PRODUCTOS", MENU_HOVER_PRODUCTS, self.show_product
        )
        MenuButton(self.sidebar, "👥  CLIENTE", MENU_HOVER_CLIENTS, self.show_customers)
        MenuButton(self.sidebar, "👔  VENDEDOR", MENU_HOVER_SELLERS, self.show_sellers)
        MenuButton(
            self.sidebar, "🔍  CONSULTAS", MENU_HOVER_CONSULTS, self.show_consults
        )

    # Estos los dejas vacíos por ahora para que no den error
    def show_sales(self):
        self.sales_ctrl.display_view()

    def show_product(self):
        self.inventory_ctrl.display_view()

    def show_customers(self):
        self.customer_ctrl.display_view()

    def show_sellers(self):
        self.sellers_ctrl.display_view()

    def show_consults(self):
        self.consults_ctrl.display_view()


if __name__ == "__main__":
    root = tk.Tk()
    app = MainDashboard(root)
    root.mainloop()
