import customtkinter as ctk
from src.views.components.search_input import SearchInput
from src.views.components.entity_table import EntityTable
from src.views.components.actions_bar import ActionsBar
from src.utils.settings import COLOR_BLANCO, FUENTE_NORMAL, FUENTE_TITULO, COLOR_BORDE


class CustomerView(ctk.CTkFrame):
    """
    Página de clientes compuesta a partir de componentes reutilizables.

    - `SearchInput` para la barra de búsqueda con debounce.
    - `EntityTable` para mostrar filas.
    - `ActionsBar` para botones CRUD (mock).

    Los datos actuales son mocks; la vista sólo se encarga de la presentación
    y delega la lógica de filtrado a `load_customers`.
    """

    def __init__(self, parent):
        super().__init__(parent, fg_color=COLOR_BLANCO)
        self.selected_rif = None

        # Header simple con título y campo de búsqueda
        header = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        header.pack(fill="x", padx=12, pady=(12, 6))

        self.title_label_customer = ctk.CTkLabel(
            header, text="Panel de clientes", font=FUENTE_TITULO, anchor="w"
        )
        self.title_label_customer.pack(side="left", padx=(6, 12))

        # Barra de búsqueda reutilizable (el callback actual llama a on_search)
        self.search_input = SearchInput(
            header, placeholder="Buscar cliente...", width=300, delay_ms=250
        )
        self.search_input.pack(side="right", padx=(6, 12))
        self.search_input.on_change(self.on_search)

        # Contenedor de la tabla con borde
        list_container = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        list_container.pack(fill="both", expand=True, padx=12, pady=(6, 12))

        table_frame = ctk.CTkFrame(
            list_container,
            fg_color=COLOR_BLANCO,
            border_width=1,
            border_color=COLOR_BORDE,
        )
        table_frame.pack(fill="both", expand=True)

        # Definir columnas y usar el componente EntityTable
        columns = [
            ("rif", "RIF", 120, "w"),
            ("name", "Nombre", 240, "w"),
            ("state", "Estado", 120, "w"),
            ("municipality", "Municipio", 140, "w"),
            ("advisor", "Asesor", 120, "w"),
        ]
        self.entity_table = EntityTable(table_frame, columns)
        self.entity_table.pack(fill="both", expand=True, padx=8, pady=8)

        # Barra de acciones reutilizable
        self.actions = ActionsBar(
            self, add_cb=self.on_add, edit_cb=self.on_edit, delete_cb=self.on_delete
        )
        self.actions.pack(fill="x", padx=12, pady=(6, 12))

        # Etiqueta de feedback
        self.result_label = ctk.CTkLabel(self, text="", font=FUENTE_NORMAL)
        self.result_label.pack(fill="x", padx=12, pady=(0, 8))

        # Datos mock (deben migrarse a modelo/servicio en el futuro)
        self.mock_customers = [
            (
                "J-12345678-9",
                "Distribuciones Industria S.A.",
                "Carabobo",
                "Naguanagua",
                "V-12345678",
            ),
            (
                "J-98765432-1",
                "Materiales del Norte C.A.",
                "Caracas",
                "Libertador",
                "V-87654321",
            ),
            (
                "J-55544433-2",
                "Ferretería El Rápido",
                "Zulia",
                "Maracaibo",
                "V-33445566",
            ),
        ]

        # Cargar inicialmente
        self.load_customers()

    def load_customers(self, search: str = None):
        """Cargar y filtrar datos (mock). La búsqueda se realiza en memoria aquí.

        En producción debería delegarse a un servicio o consulta SQL.
        """
        rows = list(self.mock_customers)
        if search:
            term = search.lower()
            rows = [
                row
                for row in self.mock_customers
                if term in row[0].lower()
                or term in row[1].lower()
                or term in row[2].lower()
                or term in row[3].lower()
                or term in row[4].lower()
            ]

        self.entity_table.populate(rows)

    def on_search(self):
        """Callback de la barra de búsqueda (invocado tras debounce)."""
        search_text = self.search_input.get()
        self.selected_rif = None
        self.result_label.configure(text="")
        self.load_customers(search=search_text)

    def on_tree_select(self, event):
        # Si se desea, se puede conectar el evento del tree a este método
        pass

    def on_add(self):
        self.result_label.configure(text="Acción: Agregar cliente (mock)")

    def on_edit(self):
        selected = self.entity_table.get_selected()
        if not selected:
            self.result_label.configure(text="Selecciona un cliente para editar.")
            return
        self.result_label.configure(
            text=f"Acción: Editar cliente RIF {selected} (mock)"
        )

    def on_delete(self):
        selected = self.entity_table.get_selected()
        if not selected:
            self.result_label.configure(text="Selecciona un cliente para eliminar.")
            return
        self.result_label.configure(
            text=f"Acción: Eliminar cliente RIF {selected} (mock)"
        )
