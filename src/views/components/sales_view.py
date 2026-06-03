import customtkinter as ctk
from src.utils.settings import COLOR_BLANCO, FUENTE_TITULO


class SalesView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=COLOR_BLANCO)

        title = ctk.CTkLabel(
            self,
            text="Panel de ventas",
            font=FUENTE_TITULO,
            anchor="center",
        )
        title.pack(fill="both", expand=True, pady=(80, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Aquí irá el flujo de ventas y las notas de entrega.",
            font=(FUENTE_TITULO[0], 14),
            text_color="#7A7A7A",
        )
        subtitle.pack(pady=(0, 10))

        info = ctk.CTkLabel(
            self,
            text="Por ahora este panel es un placeholder mientras inventario se maneja en el módulo de inventario.",
            font=FUENTE_TITULO,
            text_color="#7A7A7A",
            wraplength=520,
            justify="center",
        )
        info.pack(padx=40)
