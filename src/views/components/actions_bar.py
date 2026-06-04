import customtkinter as ctk
from typing import Callable, Optional

from src.utils.settings import (
    BUTTON_HEIGHT_MD,
    BUTTON_CORNER_RADIUS,
    SPACING_SM,
    COLOR_SECUNDARIO,
)


class ActionsBar(ctk.CTkFrame):
    """
    Barra de acciones reutilizable con botones Agregar/Editar/Eliminar.

    Los callbacks son opcionales; si no se pasan no ocurre nada al pulsar.
    """

    def __init__(
        self,
        parent,
        add_cb: Optional[Callable[[], None]] = None,
        edit_cb: Optional[Callable[[], None]] = None,
        delete_cb: Optional[Callable[[], None]] = None,
    ):
        super().__init__(
            parent,
            fg_color=(
                parent.cget("fg_color") if hasattr(parent, "cget") else "transparent"
            ),
        )

        self.add_cb = add_cb
        self.edit_cb = edit_cb
        self.delete_cb = delete_cb

        self.add_button = ctk.CTkButton(
            self,
            text="Agregar",
            fg_color=COLOR_SECUNDARIO,
            command=lambda: self._safe_call(self.add_cb),
            height=BUTTON_HEIGHT_MD,
            corner_radius=BUTTON_CORNER_RADIUS,
        )
        self.add_button.pack(side="left", padx=(0, SPACING_SM))

        self.edit_button = ctk.CTkButton(
            self,
            text="Editar",
            command=lambda: self._safe_call(self.edit_cb),
            height=BUTTON_HEIGHT_MD,
            corner_radius=BUTTON_CORNER_RADIUS,
        )
        self.edit_button.pack(side="left", padx=(0, SPACING_SM))

        self.delete_button = ctk.CTkButton(
            self,
            text="Eliminar",
            command=lambda: self._safe_call(self.delete_cb),
            height=BUTTON_HEIGHT_MD,
            corner_radius=BUTTON_CORNER_RADIUS,
        )
        self.delete_button.pack(side="left")

    def _safe_call(self, cb: Optional[Callable[[], None]]):
        if cb:
            try:
                cb()
            except Exception:
                pass
