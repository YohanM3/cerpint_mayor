import customtkinter as ctk


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
            fg_color=("#F8FAFB", "#2B2B2B"),
            hover_color=color_hover,
            text_color="#1F2937",
            corner_radius=20,
            height=58,
            border_width=0,
            anchor="w",
            font=("Roboto Medium", 14),
        )
        self.pack(side="top", fill="x", padx=18, pady=8)
