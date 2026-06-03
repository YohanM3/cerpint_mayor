import customtkinter as ctk
from src.utils.settings import COLOR_BLANCO, COLOR_BORDE


def create_page_container(
    parent,
    fg_color=COLOR_BLANCO,
    corner_radius=25,
    border_width=1,
    border_color=COLOR_BORDE,
    padx=20,
    pady=20,
    fill="both",
    expand=True,
    **pack_kwargs,
):
    """Crea un contenedor redondeado reutilizable para una vista.

    Parámetros opcionales:
    - fg_color: color de fondo del contenedor.
    - corner_radius: radio de las esquinas.
    - border_width: ancho del borde.
    - border_color: color del borde.
    - padx / pady: espacio exterior alrededor del contenedor.
    - fill: cómo debe llenar el contenedor padre.
    - expand: si debe expandirse en el espacio disponible.
    - pack_kwargs: otros valores válidos para pack().
    """
    page = ctk.CTkFrame(
        parent,
        fg_color=fg_color,
        corner_radius=corner_radius,
        border_width=border_width,
        border_color=border_color,
    )
    page.pack(fill=fill, expand=expand, padx=padx, pady=pady, **pack_kwargs)
    return page


def debounce(widget, func, delay_ms=200):
    """Crea una función debounced que ejecuta `func` tras `delay_ms` ms desde la
    última llamada. `widget` se usa para programar/cancelar el `after`.

    Uso:
        cb = debounce(self, lambda: self.on_search(), 200)
        entry.bind("<KeyRelease>", lambda e: cb())
    """

    after_id = {"id": None}

    def _call(*args, **kwargs):
        if after_id["id"]:
            try:
                widget.after_cancel(after_id["id"])
            except Exception:
                pass

        def _run():
            after_id["id"] = None
            try:
                func()
            except Exception:
                pass

        after_id["id"] = widget.after(delay_ms, _run)

    return _call
