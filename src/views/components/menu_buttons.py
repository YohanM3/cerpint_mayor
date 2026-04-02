import tkinter as tk
from src.utils.settings import FUENTE_NORMAL


class MenuButton(tk.Button):
    def __init__(self, parent, text, color_base, color_active, command=None):
        super().__init__(
            parent,
            text=text,
            command=command,
            font=FUENTE_NORMAL,
            bg=color_base,
            fg="white",
            bd=3,
            relief="flat",
            overrelief="flat",
            activebackground=color_active,
            activeforeground="white",
            cursor="hand2",
            anchor="center",
        )
        
        self.pack(side="top", fill="both", expand=True)
