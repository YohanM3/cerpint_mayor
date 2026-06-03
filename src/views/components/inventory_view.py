import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from src.utils.ui_helpers import debounce
from src.utils.settings import COLOR_BLANCO, COLOR_BORDE, FUENTE_TITULO, FUENTE_NORMAL


class InventoryView(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color=COLOR_BLANCO)
        self.configure(border_width=1, border_color=COLOR_BORDE, corner_radius=25)

        header_frame = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        header_frame.pack(fill="x", padx=24, pady=(24, 10))

        title = ctk.CTkLabel(
            header_frame,
            text="Inventario de productos",
            font=FUENTE_TITULO,
            anchor="w",
        )
        title.pack(side="left", fill="x", expand=True)

        search_frame = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        search_frame.pack(fill="x", padx=24, pady=(0, 16))

        self.search_var = tk.StringVar()
        search_entry = ctk.CTkEntry(
            search_frame,
            textvariable=self.search_var,
            placeholder_text="Buscar producto, proveedor o categoría...",
        )
        search_entry.pack(side="left", fill="x", expand=True)
        # debounce para mejorar rendimiento en búsquedas
        self._debounced_search = debounce(self, lambda: self.filter_products(), 250)
        search_entry.bind("<KeyRelease>", lambda event: self._debounced_search())

        search_button = ctk.CTkButton(
            search_frame,
            text="Buscar",
            width=90,
            command=self.filter_products,
        )
        search_button.pack(side="left", padx=(12, 0))

        # Add-product UI moved to a separate CTkToplevel window (initially hidden)
        self._add_window = None

        self.table_frame = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        self.table_frame.pack(fill="both", expand=True, padx=24, pady=(0, 24))

        self._build_table()
        self._build_actions()
        self._load_products()

    def _build_table(self):
        columns = ("id", "name", "vendor", "stock", "price", "category")
        self.tree = ttk.Treeview(
            self.table_frame,
            columns=columns,
            show="headings",
            selectmode="browse",
            height=10,
        )

        self.tree.heading("id", text="ID")
        self.tree.heading("name", text="Nombre")
        self.tree.heading("vendor", text="Proveedor")
        self.tree.heading("stock", text="Stock")
        self.tree.heading("price", text="Precio")
        self.tree.heading("category", text="Categoría")

        self.tree.column("id", width=80, anchor="center")
        self.tree.column("name", width=240, anchor="w")
        self.tree.column("vendor", width=180, anchor="w")
        self.tree.column("stock", width=100, anchor="center")
        self.tree.column("price", width=120, anchor="e")
        self.tree.column("category", width=160, anchor="w")

        scrollbar = ttk.Scrollbar(
            self.table_frame,
            orient="vertical",
            command=self.tree.yview,
        )
        self.tree.configure(yscroll=scrollbar.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _build_actions(self):
        action_frame = ctk.CTkFrame(self, fg_color=COLOR_BLANCO)
        action_frame.pack(fill="x", padx=24, pady=(0, 12))

        from src.utils.settings import (
            BUTTON_HEIGHT_MD,
            BUTTON_CORNER_RADIUS,
            SPACING_SM,
        )

        btn_add = ctk.CTkButton(
            action_frame,
            text="Agregar producto",
            height=BUTTON_HEIGHT_MD,
            corner_radius=BUTTON_CORNER_RADIUS,
            command=self.open_add_screen,
        )
        btn_edit = ctk.CTkButton(
            action_frame,
            text="Editar selección",
            height=BUTTON_HEIGHT_MD,
            corner_radius=BUTTON_CORNER_RADIUS,
            command=self._open_edit_selection,
        )
        btn_remove = ctk.CTkButton(
            action_frame,
            text="Eliminar producto",
            height=BUTTON_HEIGHT_MD,
            corner_radius=BUTTON_CORNER_RADIUS,
        )

        btn_add.pack(side="left", padx=(0, SPACING_SM))
        btn_edit.pack(side="left", padx=(0, SPACING_SM))
        btn_remove.pack(side="left")

    def _load_products(self):
        self.products = [
            (
                "INV-001",
                "Lámina galvanizada",
                "Metalurgia López",
                45,
                "$26.50",
                "Material metálico",
            ),
            ("INV-002", "Cemento gris", "Cemex", 98, "$8.20", "Construcción"),
            (
                "INV-003",
                "Tornillo zincado",
                "Fijaciones del Norte",
                320,
                "$0.40",
                "Herrajes",
            ),
            ("INV-004", "Pintura blanca", "Colores Patria", 60, "$12.90", "Acabados"),
            (
                "INV-005",
                "Madera estructural",
                "Bosques del Sur",
                25,
                "$75.00",
                "Madera",
            ),
        ]
        self._refresh_table(self.products)

    def _refresh_table(self, rows):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for row in rows:
            self.tree.insert("", "end", values=row)

    def filter_products(self):
        query = self.search_var.get().strip().lower()
        if not query:
            self._refresh_table(self.products)
            return

        filtered = [
            row
            for row in self.products
            if query in row[1].lower()
            or query in row[2].lower()
            or query in row[5].lower()
        ]
        self._refresh_table(filtered)
    # --- Separate add/edit window (UI-only, mock save) ---
    def open_add_screen(self, edit=False, product=None):
        if self._add_window and tk.Toplevel.winfo_exists(self._add_window):
            self._add_window.lift()
            return

        self._add_window = ctk.CTkToplevel(self)
        title = "Editar producto" if edit else "Agregar producto"
        self._add_window.title(title)
        self._add_window.geometry("700x420")
        self._add_window.grab_set()

        panel = ctk.CTkFrame(self._add_window, fg_color=COLOR_BLANCO)
        panel.pack(fill="both", expand=True, padx=16, pady=12)

        fields = ctk.CTkFrame(panel, fg_color=COLOR_BLANCO)
        fields.pack(fill="x", padx=8, pady=8)

        lbl_name = ctk.CTkLabel(fields, text="Nombre", anchor="w")
        lbl_name.grid(row=0, column=0, sticky="w", padx=(0,6))
        entry_name = ctk.CTkEntry(fields, placeholder_text="Nombre del producto")
        entry_name.grid(row=1, column=0, sticky="we", padx=(0,6))

        lbl_brand = ctk.CTkLabel(fields, text="Marca", anchor="w")
        lbl_brand.grid(row=0, column=1, sticky="w", padx=(6,6))
        entry_brand = ctk.CTkEntry(fields, placeholder_text="Marca")
        entry_brand.grid(row=1, column=1, sticky="we", padx=(6,6))

        lbl_supplier = ctk.CTkLabel(fields, text="Proveedor", anchor="w")
        lbl_supplier.grid(row=2, column=0, sticky="w", padx=(0,6), pady=(8,0))
        entry_supplier = ctk.CTkEntry(fields, placeholder_text="Proveedor")
        entry_supplier.grid(row=3, column=0, sticky="we", padx=(0,6))

        lbl_price = ctk.CTkLabel(fields, text="Precio venta", anchor="w")
        lbl_price.grid(row=2, column=1, sticky="w", padx=(6,6), pady=(8,0))
        entry_price = ctk.CTkEntry(fields, placeholder_text="0.00")
        entry_price.grid(row=3, column=1, sticky="we", padx=(6,6))

        lbl_stock = ctk.CTkLabel(fields, text="Stock", anchor="w")
        lbl_stock.grid(row=4, column=0, sticky="w", padx=(0,6), pady=(8,0))
        entry_stock = ctk.CTkEntry(fields, placeholder_text="0")
        entry_stock.grid(row=5, column=0, sticky="we", padx=(0,6))

        lbl_category = ctk.CTkLabel(fields, text="Categoría", anchor="w")
        lbl_category.grid(row=4, column=1, sticky="w", padx=(6,6), pady=(8,0))
        entry_category = ctk.CTkEntry(fields, placeholder_text="Categoría")
        entry_category.grid(row=5, column=1, sticky="we", padx=(6,6))

        fields.grid_columnconfigure(0, weight=1)
        fields.grid_columnconfigure(1, weight=1)

        actions = ctk.CTkFrame(panel, fg_color=COLOR_BLANCO)
        actions.pack(fill="x", padx=8, pady=(6,10))

        btn_save = ctk.CTkButton(actions, text="Guardar (mock)", width=140, command=lambda: self._mock_save_toplevel(entry_name, entry_brand, entry_supplier, entry_price, entry_stock, entry_category))
        btn_cancel = ctk.CTkButton(actions, text="Cancelar", width=100, command=lambda: self._close_add_window())
        btn_save.pack(side="left", padx=(0,12))
        btn_cancel.pack(side="left")

        feedback = ctk.CTkLabel(panel, text="", text_color="#007BFF")
        feedback.pack(fill="x", padx=12, pady=(0,6))

        # if editing, prefill
        if edit and product:
            # product is a tuple matching table columns
            entry_name.insert(0, product[1])
            entry_brand.insert(0, product[2])
            entry_supplier.insert(0, product[2])
            entry_stock.insert(0, str(product[3]))
            entry_price.insert(0, str(product[4]))
            entry_category.insert(0, product[5])

        # store references for potential use
        self._add_widgets = {
            "window": self._add_window,
            "feedback": feedback,
        }

    def _close_add_window(self):
        if self._add_window:
            try:
                self._add_window.grab_release()
            except Exception:
                pass
            try:
                self._add_window.destroy()
            finally:
                self._add_window = None

    def _mock_save_toplevel(self, entry_name, entry_brand, entry_supplier, entry_price, entry_stock, entry_category):
        name = entry_name.get().strip()
        feedback = self._add_widgets.get("feedback") if hasattr(self, "_add_widgets") else None
        if not name:
            if feedback:
                feedback.configure(text="El nombre es obligatorio.")
            return
        if feedback:
            feedback.configure(text=f"Producto '{name}' agregado (mock).")
        # auto-close after brief delay
        self.after(700, self._close_add_window)

    def _open_edit_selection(self):
        sel = self.tree.selection()
        if not sel:
            return
        vals = self.tree.item(sel[0], "values")
        # open edit screen with prefilled values
        self.open_add_screen(edit=True, product=vals)
