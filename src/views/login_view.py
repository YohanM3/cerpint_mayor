import customtkinter as ctk
from tkinter import messagebox
from src.views.dashboard_view import MainDashboard

from src.utils.settings import (
    APP_MODE,
    COLOR_BLANCO,
    COLOR_BORDE,
    COLOR_FONDO,
    COLOR_PRIMARIO,
    COLOR_SECUNDARIO,
    COLOR_TEXTO,
    COLOR_TEXT_MUTED,
    COLOR_TEXT_SECONDARY,
    COLOR_THEME,
    FUENTE_NORMAL,
    FUENTE_TITULO,
)


class LoginView:
    def open_dashboard(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        MainDashboard(self.root)

    def __init__(self):
        ctk.set_appearance_mode(APP_MODE)
        ctk.set_default_color_theme(COLOR_THEME)

        self.root = ctk.CTk()
        self.root.title("Cerpint Mayor - Acceso")
        self.root.geometry("460x560")
        self.root.configure(fg_color=COLOR_FONDO)
        self.root.resizable(False, False)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.crear_widgets()

    def crear_widgets(self):
        self.container = ctk.CTkFrame(
            self.root,
            fg_color=COLOR_BLANCO,
            corner_radius=25,
            border_width=1,
            border_color=COLOR_BORDE,
        )
        self.container.grid(row=0, column=0, padx=24, pady=24, sticky="nsew")

        self.header = ctk.CTkFrame(
            self.container, fg_color=COLOR_FONDO, corner_radius=20
        )
        self.header.pack(fill="x", padx=20, pady=(20, 10))

        self.label_titulo = ctk.CTkLabel(
            self.header,
            text="Cerpint Mayor",
            font=(FUENTE_TITULO[0], 24, "bold"),
            text_color=COLOR_TEXTO,
        )
        self.label_titulo.pack(pady=(12, 0))

        self.label_subtitle = ctk.CTkLabel(
            self.header,
            text="Bienvenido de nuevo",
            font=(FUENTE_NORMAL[0], 14),
            text_color=COLOR_TEXT_SECONDARY,
        )
        self.label_subtitle.pack(pady=(5, 18))

        self.form_frame = ctk.CTkFrame(
            self.container, fg_color=COLOR_FONDO, corner_radius=20
        )
        self.form_frame.pack(fill="both", expand=True, padx=20, pady=(0, 10))

        self.title_label = ctk.CTkLabel(
            self.form_frame,
            text="Inicia sesión",
            font=(FUENTE_TITULO[0], 20, "bold"),
            text_color=COLOR_TEXTO,
            anchor="w",
        )
        self.title_label.pack(fill="x", padx=20, pady=(20, 10))

        self.subtitle_label = ctk.CTkLabel(
            self.form_frame,
            text="Ingresa tus datos para continuar con el panel.",
            font=(FUENTE_NORMAL[0], 12),
            text_color=COLOR_TEXT_MUTED,
            anchor="w",
        )
        self.subtitle_label.pack(fill="x", padx=20, pady=(0, 20))

        self.entry_cedula = ctk.CTkEntry(
            self.form_frame,
            font=FUENTE_NORMAL,
            placeholder_text="Usuario",
            corner_radius=12,
        )
        self.entry_cedula.pack(fill="x", padx=20, pady=(0, 15), ipady=12)

        self.entry_password = ctk.CTkEntry(
            self.form_frame,
            font=FUENTE_NORMAL,
            placeholder_text="Contraseña",
            show="●",
            corner_radius=12,
        )
        self.entry_password.pack(fill="x", padx=20, pady=(0, 10), ipady=12)

        self.forgot_frame = ctk.CTkFrame(
            self.form_frame,
            fg_color=COLOR_FONDO,
            corner_radius=12,
            border_width=1,
            border_color=COLOR_BORDE,
        )
        self.forgot_frame.pack(fill="x", padx=20, pady=(0, 20))

        self.label_forget_password = ctk.CTkLabel(
            self.forgot_frame,
            text="¿Olvidaste tu contraseña?",
            font=FUENTE_NORMAL,
            text_color=COLOR_PRIMARIO,
        )
        self.label_forget_password.pack(padx=15, pady=12)

        self.login_button = ctk.CTkButton(
            self.form_frame,
            text="Ingresar",
            font=FUENTE_NORMAL,
            fg_color=COLOR_SECUNDARIO,
            text_color=COLOR_BLANCO,
            hover_color=COLOR_PRIMARIO,
            corner_radius=16,
            command=self.handle_login,
        )
        self.login_button.pack(fill="x", padx=20, pady=(0, 20), ipady=14)

        self.root.bind("<Return>", lambda event: self.handle_login())

        self.version_label = ctk.CTkLabel(
            self.container,
            text="v1.0.0 ∴ 2026",
            font=FUENTE_NORMAL,
            text_color=COLOR_TEXTO,
        )
        self.version_label.pack(side="bottom", pady=(0, 18))

        self.root.after(10, self.entry_cedula.focus_set)

    def handle_login(self):
        usuario = self.entry_cedula.get().strip()
        clave = self.entry_password.get().strip()

        if not usuario or not clave:
            messagebox.showwarning(
                "Campos incompletos",
                "Debes ingresar usuario y contraseña.",
            )
            return

        if not self.validate_credentials(usuario, clave):
            messagebox.showerror(
                "Acceso denegado",
                "Usuario o contraseña incorrectos.",
            )
            self.entry_password.delete(0, "end")
            return

        self.root.after_idle(self.open_dashboard)

    def validate_credentials(self, usuario, clave):
        # Validación temporal de ejemplo.
        # Cambia esta lógica por la base de datos cuando la tengas lista.
        return usuario == "admin" and clave == "1234"


if __name__ == "__main__":
    app = LoginView()
    app.root.mainloop()
