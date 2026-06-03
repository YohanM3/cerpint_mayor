import customtkinter as ctk
from tkinter import ttk
from src.utils.ui_helpers import debounce
from src.utils.settings import (
    COLOR_BLANCO,
    FUENTE_TITULO,
    FUENTE_NORMAL,
    COLOR_SECUNDARIO,
    COLOR_BORDE,
)


class SellersView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=COLOR_BLANCO)
        self.selected_cedula = None

        header = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        header.pack(fill="x", padx=12, pady=(12, 6))

        self.title_label_sellers = ctk.CTkLabel(
            header, text="Panel de vendedores", font=FUENTE_TITULO, anchor="w"
        )
        self.title_label_sellers.pack(side="left", padx=(6, 12))

        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(
            header,
            width=300,
            placeholder_text="Buscar vendedor...",
            textvariable=self.search_var,
            corner_radius=10,
        )
        self.search_entry.pack(side="right", padx=(6, 12))
        self._debounced_search = debounce(self, lambda: self.on_search(), 250)
        self.search_entry.bind("<KeyRelease>", lambda event: self._debounced_search())

        list_container = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        list_container.pack(fill="both", expand=True, padx=12, pady=(6, 12))

        self.table_frame = ctk.CTkFrame(
            list_container,
            fg_color=COLOR_BLANCO,
            border_width=1,
            border_color=COLOR_BORDE,
        )
        self.table_frame.pack(fill="both", expand=True)

        tree_container = ctk.CTkFrame(self.table_frame, fg_color=COLOR_BLANCO)
        tree_container.pack(fill="both", expand=True, padx=8, pady=8)

        self.tree = ttk.Treeview(
            tree_container,
            columns=("cedula", "name", "phone", "address"),
            show="headings",
            selectmode="browse",
        )
        self.tree.heading("cedula", text="Cédula")
        self.tree.heading("name", text="Nombre")
        self.tree.heading("phone", text="Teléfono")
        self.tree.heading("address", text="Dirección")
        self.tree.column("cedula", width=140, anchor="w")
        self.tree.column("name", width=220, anchor="w")
        self.tree.column("phone", width=140, anchor="w")
        self.tree.column("address", width=240, anchor="w")
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        scrollbar = ttk.Scrollbar(
            tree_container, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        actions = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        actions.pack(fill="x", padx=12, pady=(6, 12))

        self.add_button = ctk.CTkButton(
            actions, text="Agregar", fg_color=COLOR_SECUNDARIO, command=self.on_add
        )
        from src.utils.settings import (
            BUTTON_HEIGHT_MD,
            BUTTON_CORNER_RADIUS,
            SPACING_SM,
        )

        self.add_button.configure(
            height=BUTTON_HEIGHT_MD, corner_radius=BUTTON_CORNER_RADIUS
        )
        self.add_button.pack(side="left", padx=SPACING_SM)

        self.edit_button = ctk.CTkButton(actions, text="Editar", command=self.on_edit)
        self.edit_button.configure(
            height=BUTTON_HEIGHT_MD, corner_radius=BUTTON_CORNER_RADIUS
        )
        self.edit_button.pack(side="left", padx=SPACING_SM)

        self.delete_button = ctk.CTkButton(
            actions, text="Eliminar", command=self.on_delete
        )
        self.delete_button.configure(
            height=BUTTON_HEIGHT_MD, corner_radius=BUTTON_CORNER_RADIUS
        )
        self.delete_button.pack(side="left", padx=SPACING_SM)

        self.result_label = ctk.CTkLabel(self, text="", font=FUENTE_NORMAL)
        self.result_label.pack(fill="x", padx=12, pady=(0, 8))

        self.mock_vendors = [
            {
                "cedula": "V-12345678",
                "name": "Carlos Pérez",
                "phone": "+58 412-1234567",
                "address": "Av. Principal 45",
            },
            {
                "cedula": "V-87654321",
                "name": "María González",
                "phone": "+58 414-7654321",
                "address": "Calle 23 con 7",
            },
            {
                "cedula": "V-33445566",
                "name": "Luis Ramírez",
                "phone": "+58 412-3344556",
                "address": "Carrera 8, Quinta Azul",
            },
        ]

        self.load_vendors()

    def load_vendors(self, search=None):
        rows = self.mock_vendors
        if search:
            term = search.lower()
            rows = [
                row
                for row in self.mock_vendors
                if term in row["cedula"].lower()
                or term in row["name"].lower()
                or term in row["phone"].lower()
                or term in row["address"].lower()
            ]
        self.populate_table(rows)

    def populate_table(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in rows:
            self.tree.insert(
                "",
                "end",
                iid=row.get("cedula"),
                values=(
                    row.get("cedula"),
                    row.get("name"),
                    row.get("phone"),
                    row.get("address"),
                ),
            )

    def on_search(self):
        search_text = self.search_var.get().strip()
        self.selected_cedula = None
        self.result_label.configure(text="")
        self.load_vendors(search=search_text)

    def on_tree_select(self, event):
        selection = self.tree.selection()
        if selection:
            self.selected_cedula = selection[0]
            self.result_label.configure(
                text=f"Seleccionado Cédula {self.selected_cedula}"
            )
        else:
            self.selected_cedula = None
            self.result_label.configure(text="")

    def on_add(self):
        self.result_label.configure(text="Acción: Agregar vendedor (mock)")

    def on_edit(self):
        if not self.selected_cedula:
            self.result_label.configure(text="Selecciona un vendedor para editar.")
            return
        self.result_label.configure(
            text=f"Acción: Editar vendedor Cédula {self.selected_cedula} (mock)"
        )

    def on_delete(self):
        if not self.selected_cedula:
            self.result_label.configure(text="Selecciona un vendedor para eliminar.")
            return
        self.result_label.configure(
            text=f"Acción: Eliminar vendedor Cédula {self.selected_cedula} (mock)"
        )
