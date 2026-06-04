import customtkinter as ctk
from src.views.components.search_input import SearchInput
from src.views.components.entity_table import EntityTable
from src.views.components.actions_bar import ActionsBar
from src.utils.settings import COLOR_BLANCO, FUENTE_TITULO, FUENTE_NORMAL, COLOR_BORDE


class SellersView(ctk.CTkFrame):
    """
    Página de vendedores construida con componentes reutilizables.

    Mantiene la misma funcionalidad que antes pero ahora usa `SearchInput`,
    `EntityTable` y `ActionsBar` para evitar duplicación.
    """

    def __init__(self, parent):
        super().__init__(parent, fg_color=COLOR_BLANCO)
        self.selected_cedula = None

        header = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        header.pack(fill="x", padx=12, pady=(12, 6))

        self.title_label_sellers = ctk.CTkLabel(
            header, text="Panel de vendedores", font=FUENTE_TITULO, anchor="w"
        )
        self.title_label_sellers.pack(side="left", padx=(6, 12))

        self.search_input = SearchInput(
            header, placeholder="Buscar vendedor...", width=300, delay_ms=250
        )
        self.search_input.pack(side="right", padx=(6, 12))
        self.search_input.on_change(self.on_search)

        list_container = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        list_container.pack(fill="both", expand=True, padx=12, pady=(6, 12))

        table_frame = ctk.CTkFrame(
            list_container,
            fg_color=COLOR_BLANCO,
            border_width=1,
            border_color=COLOR_BORDE,
        )
        table_frame.pack(fill="both", expand=True)

        columns = [
            ("cedula", "Cédula", 140, "w"),
            ("name", "Nombre", 220, "w"),
            ("phone", "Teléfono", 140, "w"),
            ("address", "Dirección", 240, "w"),
        ]
        self.entity_table = EntityTable(table_frame, columns)
        self.entity_table.pack(fill="both", expand=True, padx=8, pady=8)

        self.actions = ActionsBar(
            self, add_cb=self.on_add, edit_cb=self.on_edit, delete_cb=self.on_delete
        )
        self.actions.pack(fill="x", padx=12, pady=(6, 12))

        self.result_label = ctk.CTkLabel(self, text="", font=FUENTE_NORMAL)
        self.result_label.pack(fill="x", padx=12, pady=(0, 8))

        # Datos mock
        self.mock_vendors = [
            ("V-12345678", "Carlos Pérez", "+58 412-1234567", "Av. Principal 45"),
            ("V-87654321", "María González", "+58 414-7654321", "Calle 23 con 7"),
            ("V-33445566", "Luis Ramírez", "+58 412-3344556", "Carrera 8, Quinta Azul"),
        ]

        self.load_vendors()

    def load_vendors(self, search: str = None):
        rows = list(self.mock_vendors)
        if search:
            term = search.lower()
            rows = [
                row
                for row in self.mock_vendors
                if term in row[0].lower()
                or term in row[1].lower()
                or term in row[2].lower()
                or term in row[3].lower()
            ]
        self.entity_table.populate(rows)

    def on_search(self):
        search_text = self.search_input.get()
        self.selected_cedula = None
        self.result_label.configure(text="")
        self.load_vendors(search=search_text)

    def on_add(self):
        self.result_label.configure(text="Acción: Agregar vendedor (mock)")

    def on_edit(self):
        selected = self.entity_table.get_selected()
        if not selected:
            self.result_label.configure(text="Selecciona un vendedor para editar.")
            return
        self.result_label.configure(
            text=f"Acción: Editar vendedor Cédula {selected} (mock)"
        )

    def on_delete(self):
        selected = self.entity_table.get_selected()
        if not selected:
            self.result_label.configure(text="Selecciona un vendedor para eliminar.")
            return
        self.result_label.configure(
            text=f"Acción: Eliminar vendedor Cédula {selected} (mock)"
        )
