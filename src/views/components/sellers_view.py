
import customtkinter as ctk
from src.utils.settings import FUENTE_TITULO, FUENTE_NORMAL, COLOR_SECUNDARIO


class SellersView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color="White")
        self.title_label_sellers = ctk.CTkLabel(
            self, text="Panel de vendedores", font=FUENTE_TITULO
        )
        self.title_label_sellers.pack(pady=50)
