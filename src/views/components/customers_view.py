import customtkinter as ctk
from tkinter import ttk
from src.utils.ui_helpers import debounce
from src.utils.settings import (
    COLOR_BLANCO,
    FUENTE_NORMAL,
    FUENTE_TITULO,
    COLOR_SECUNDARIO,
    COLOR_BORDE,
)


class CustomerView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=COLOR_BLANCO)
        self.selected_rif = None

        header = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        header.pack(fill="x", padx=12, pady=(12, 6))

        self.title_label_customer = ctk.CTkLabel(
            header, text="Panel de clientes", font=FUENTE_TITULO, anchor="w"
        )
        self.title_label_customer.pack(side="left", padx=(6, 12))

        self.search_var = ctk.StringVar()
        self.search_entry = ctk.CTkEntry(
            header,
            width=300,
            placeholder_text="Buscar cliente...",
            textvariable=self.search_var,
            corner_radius=10,
        )
        self.search_entry.pack(side="right", padx=(6, 12))
        # usar búsqueda debounced para evitar recalculos en cada tecla
        self._debounced_search = debounce(self, lambda: self.on_search(), 250)
        self.search_entry.bind("<KeyRelease>", lambda event: self._debounced_search())

        # Tabla de clientes
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
            columns=("rif", "name", "state", "municipality", "advisor"),
            show="headings",
            selectmode="browse",
        )
        self.tree.heading("rif", text="RIF")
        self.tree.heading("name", text="Nombre")
        self.tree.heading("state", text="Estado")
        self.tree.heading("municipality", text="Municipio")
        self.tree.heading("advisor", text="Asesor")
        self.tree.column("rif", width=120, anchor="w")
        self.tree.column("name", width=240, anchor="w")
        self.tree.column("state", width=120, anchor="w")
        self.tree.column("municipality", width=140, anchor="w")
        self.tree.column("advisor", width=120, anchor="w")
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)

        scrollbar = ttk.Scrollbar(
            tree_container, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Botones de acción
        actions = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        actions.pack(fill="x", padx=12, pady=(6, 12))

        from src.utils.settings import (
            BUTTON_HEIGHT_MD,
            BUTTON_CORNER_RADIUS,
            SPACING_SM,
        )

        self.add_button = ctk.CTkButton(
            actions,
            text="Agregar",
            fg_color=COLOR_SECUNDARIO,
            command=self.on_add,
            height=BUTTON_HEIGHT_MD,
            corner_radius=BUTTON_CORNER_RADIUS,
        )
        self.add_button.pack(side="left", padx=SPACING_SM)

        self.edit_button = ctk.CTkButton(
            actions,
            text="Editar",
            command=self.on_edit,
            height=BUTTON_HEIGHT_MD,
            corner_radius=BUTTON_CORNER_RADIUS,
        )
        self.edit_button.pack(side="left", padx=SPACING_SM)

        self.delete_button = ctk.CTkButton(
            actions,
            text="Eliminar",
            command=self.on_delete,
            height=BUTTON_HEIGHT_MD,
            corner_radius=BUTTON_CORNER_RADIUS,
        )
        self.delete_button.pack(side="left", padx=SPACING_SM)

        self.result_label = ctk.CTkLabel(self, text="", font=FUENTE_NORMAL)
        self.result_label.pack(fill="x", padx=12, pady=(0, 8))

        self.mock_customers = [
            {
                "rif": "J-12345678-9",
                "name": "Distribuciones Industria S.A.",
                "state_name": "Carabobo",
                "municipality": "Naguanagua",
                "advisor_cedula": "V-12345678",
            },
            {
                "rif": "J-98765432-1",
                "name": "Materiales del Norte C.A.",
                "state_name": "Caracas",
                "municipality": "Libertador",
                "advisor_cedula": "V-87654321",
            },
            {
                "rif": "J-55544433-2",
                "name": "Ferretería El Rápido",
                "state_name": "Zulia",
                "municipality": "Maracaibo",
                "advisor_cedula": "V-33445566",
            },
        ]

        self.load_customers()

    def load_customers(self, search=None):
        rows = self.mock_customers
        if search:
            term = search.lower()
            rows = [
                row
                for row in self.mock_customers
                if term in row["rif"].lower()
                or term in row["name"].lower()
                or term in row["state_name"].lower()
                or term in row["municipality"].lower()
                or term in row["advisor_cedula"].lower()
            ]

        self.populate_table(rows)

    def populate_table(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in rows:
            self.tree.insert(
                "",
                "end",
                iid=row.get("rif"),
                values=(
                    row.get("rif"),
                    row.get("name"),
                    row.get("state_name"),
                    row.get("municipality"),
                    row.get("advisor_cedula"),
                ),
            )

    def on_search(self):
        search_text = self.search_var.get().strip()
        self.selected_rif = None
        self.result_label.configure(text="")
        self.load_customers(search=search_text)

    def on_tree_select(self, event):
        selection = self.tree.selection()
        if selection:
            self.selected_rif = selection[0]
            self.result_label.configure(text=f"Seleccionado RIF {self.selected_rif}")
        else:
            self.selected_rif = None
            self.result_label.configure(text="")

    def on_add(self):
        self.result_label.configure(text="Acción: Agregar cliente (mock)")

    def on_edit(self):
        if not self.selected_rif:
            self.result_label.configure(text="Selecciona un cliente para editar.")
            return
        self.result_label.configure(
            text=f"Acción: Editar cliente RIF {self.selected_rif} (mock)"
        )

    def on_delete(self):
        if not self.selected_rif:
            self.result_label.configure(text="Selecciona un cliente para eliminar.")
            return
        self.result_label.configure(
            text=f"Acción: Eliminar cliente RIF {self.selected_rif} (mock)"
        )
