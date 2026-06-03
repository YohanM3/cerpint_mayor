import customtkinter as ctk
from src.utils.settings import (
    MENU_BUTTON_BG,
    MENU_BUTTON_TEXT,
    BUTTON_HEIGHT_LG,
    BUTTON_CORNER_RADIUS,
    SPACING_MD,
    SPACING_SM,
    FUENTE_NORMAL,
)


class MenuButton(ctk.CTkButton):

    def __init__(
        self,
        parent,
        text,
        color_hover,
        command,
    ):
        super().__init__(
            master=parent,
            text=text,
            command=command,
            fg_color=MENU_BUTTON_BG,
            hover_color=color_hover,
            text_color=MENU_BUTTON_TEXT,
            corner_radius=BUTTON_CORNER_RADIUS,
            height=BUTTON_HEIGHT_LG,
            border_width=0,
            anchor="w",
            font=FUENTE_NORMAL,
        )
        self.pack(side="top", fill="x", padx=SPACING_MD, pady=SPACING_SM)
