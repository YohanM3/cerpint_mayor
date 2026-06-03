import tkinter as tk
import customtkinter as ctk
from src.utils.settings import FUENTE_TITULO, FUENTE_NORMAL,COLOR_SECUNDARIO


class InventoryView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color="White")
        self.title_label_inventory = ctk.CTkLabel(
            self, text="Panel de inventario", font=FUENTE_TITULO
        )
        self.title_label_inventory.pack(pady=50)



