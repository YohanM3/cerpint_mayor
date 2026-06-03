import customtkinter as ctk
from src.utils.settings import COLOR_BLANCO, FUENTE_NORMAL, FUENTE_TITULO


class ConsultsView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color=COLOR_BLANCO)
        self.title_label_consults = ctk.CTkLabel(
            self, text="Panel de consultas", font=FUENTE_TITULO
        )
        self.title_label_consults.pack(pady=50)
