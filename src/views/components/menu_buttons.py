import customtkinter as ctk

class MenuButton(ctk.CTkButton):

    def __init__(
        self,
        parent,
        text,
        color_hover,
        command
    ):
        super().__init__(
            master=parent,
            text=text,
            command=command,
            fg_color=("#F0F0F0", "#2B2B2B"),
            hover_color=color_hover,
            anchor="w",
            text_color="#1C1C1C",
            corner_radius=15,
            height=50,
            border_spacing=20,
            border_width=3,
            border_color="gray85",
            font=("Roboto Medium", 13),
        )
        self.pack(side="top", fill="x", padx=15, pady=6)
