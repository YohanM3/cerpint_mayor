import tkinter as tk
from tkinter import messagebox

from src.utils.settings import COLOR_FONDO, COLOR_TEXTO, FUENTE_TITULO, FUENTE_NORMAL, COLOR_PRIMARIO, COLOR_SECUNDARIO
class LoginView:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Cerpint Mayor - Acceso")
        self.root.geometry("400x500")
        self.root.configure(bg=COLOR_FONDO)
        self.root.resizable(False,False)

        self.crear_widgets()

    def crear_widgets(self):
        self.label_titulo = tk.Label(
            self.root,
            text="CERPINT MAYOR",
            font=FUENTE_TITULO,
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO,
        )
        self.label_titulo.pack(pady=20)

        # INPUT DE USUARIO Y SU LABEL

        self.label_user=tk.Label(
            self.root,
            text="Usuario",
            font=FUENTE_NORMAL,
            fg=COLOR_TEXTO
        )
        self.label_user.pack(pady=5)
        self.entry_cedula=tk.Entry(
            self.root,
            font=FUENTE_NORMAL,
            justify="left",
            fg=COLOR_TEXTO,
            bg="white",
            bd=8,
            relief="flat",
            highlightthickness=1,            
        )
        self.entry_cedula.config(highlightbackground="#CCCCCC", highlightcolor="#28a745")
        self.entry_cedula.pack(pady=10, padx=50, fill="x")

        # INPUT DE PASSWORD Y SU LABEL

        self.label_password = tk.Label(
            self.root, text="Clave de acceso",
            font=FUENTE_NORMAL,
            fg=COLOR_TEXTO
        )
        self.label_password.pack(pady=5)
        self.entry_password = tk.Entry(
            self.root,
            font=FUENTE_NORMAL,
            justify="left",
            fg=COLOR_TEXTO,
            bg="white",
            show="●",
            bd=8,
            relief="flat",
            highlightthickness=1,
        )
        self.entry_password.config(highlightbackground="#CCCCCC", highlightcolor="#28a745")
        self.entry_password.pack(pady=10, padx=50, fill="x")

        # label de olvido contraseña
        self.label_forget_password = tk.Label(
            self.root,
            text="¿Olvidaste tu contraseña?",
            font=FUENTE_NORMAL,
            fg=COLOR_PRIMARIO,
        )
        self.label_forget_password.pack(pady=5)

        # Boton de acceso de login
        self.login_button = tk.Button(
            self.root,
            text="Ingresar",
            font=FUENTE_NORMAL,
            bg=COLOR_SECUNDARIO,
            fg="white",
            activebackground="#218838",
            activeforeground="white",
            bd=0,
            cursor="hand2"
        )
        self.login_button.pack(pady=30, padx=50, fill="x", ipady=10)

        # Footer login

        self.version_label = tk.Label(
            self.root, 
            text="v1.0.0 ∴ 2026",
            font=FUENTE_NORMAL,
            bg=COLOR_FONDO,
            fg=COLOR_TEXTO
        )
        self.version_label.pack(side="bottom", pady=10)
        self.entry_cedula.focus_set()

if __name__=="__main__":
  app = LoginView()
  app.root.mainloop()
