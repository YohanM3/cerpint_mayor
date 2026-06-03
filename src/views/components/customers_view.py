
import customtkinter as ctk
from src.utils.settings import FUENTE_NORMAL, FUENTE_TITULO

class CustomerView(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(parent, fg_color="White")
        self.title_label_customer=ctk.CTkLabel(
          self,
          text="Panel del cliente",
          font=FUENTE_TITULO
        )
        self.title_label_customer.pack(pady=50)
        
    

