import customtkinter as ctk
import tkinter as tk
from typing import Callable, Optional

from src.utils.ui_helpers import debounce


class SearchInput(ctk.CTkFrame):
    """
    Componente reutilizable de búsqueda.

    Proporciona un `CTkEntry` con un `StringVar` y soporte para
    debounce (evitar disparar búsquedas en cada pulsación).

    Uso:
        si = SearchInput(parent, placeholder="Buscar...", delay_ms=250)
        si.pack(...)
        si.on_change(lambda: manejar_busqueda(si.get()))
    """

    def __init__(
        self,
        parent,
        placeholder: str = "",
        width: Optional[int] = None,
        delay_ms: int = 250,
    ):
        super().__init__(
            parent,
            fg_color=(
                parent.cget("fg_color") if hasattr(parent, "cget") else "transparent"
            ),
        )
        self.search_var = tk.StringVar()
        self._delay_ms = delay_ms

        self.entry = ctk.CTkEntry(
            self,
            width=width,
            placeholder_text=placeholder,
            textvariable=self.search_var,
            corner_radius=10,
        )
        self.entry.pack(fill="x", expand=True)

        self._callback: Optional[Callable[[], None]] = None
        self._debounced = debounce(self, self._on_debounced, delay_ms)
        # Conectar evento de teclas al debounced
        self.entry.bind("<KeyRelease>", lambda e: self._debounced())

    def _on_debounced(self):
        if self._callback:
            try:
                self._callback()
            except Exception:
                pass

    def on_change(self, callback: Callable[[], None]):
        """Registrar callback que se ejecuta tras debounce cuando cambia el texto."""
        self._callback = callback

    def get(self) -> str:
        """Devolver el texto actual de búsqueda."""
        return self.search_var.get().strip()
