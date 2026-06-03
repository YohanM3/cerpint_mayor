import customtkinter as ctk
from src.utils.settings import COLOR_BLANCO, FUENTE_TITULO, FUENTE_NORMAL


class InventoryView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color=COLOR_BLANCO)
        self.title_label_inventory = ctk.CTkLabel(
            self, text="Panel de inventario", font=FUENTE_TITULO
        )
        self.title_label_inventory.pack(pady=50)
