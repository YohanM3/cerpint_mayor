import tkinter as tk
from src.utils.settings import FUENTE_TITULO, FUENTE_NORMAL,COLOR_SECUNDARIO

class InventoryView(tk.Frame):
  def __init__(self, parent):
    super().__init__(parent, bg="white")
    self.create_widgets()