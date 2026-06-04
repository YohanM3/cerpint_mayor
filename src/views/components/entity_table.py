import tkinter as tk
from tkinter import ttk
from typing import List, Tuple, Iterable


class EntityTable(tk.Frame):
    """
    Componente de tabla reutilizable.

    - `columns` es una lista de tuplas `(id, heading, width, anchor)`.
    - Provee métodos `populate(rows)`, `clear()` y `get_selected()`.
    """

    def __init__(self, parent, columns: Iterable[Tuple[str, str, int, str]]):
        super().__init__(parent)
        self.columns = [c[0] for c in columns]

        self.tree = ttk.Treeview(
            self, columns=self.columns, show="headings", selectmode="browse"
        )

        for col_id, heading, width, anchor in columns:
            self.tree.heading(col_id, text=heading)
            self.tree.column(col_id, width=width, anchor=anchor)

        self.v_scroll = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.v_scroll.set)

        self.tree.pack(side="left", fill="both", expand=True)
        self.v_scroll.pack(side="right", fill="y")

    def populate(self, rows: List[Tuple]):
        """Rellena la tabla con `rows`, que son tuplas en el mismo orden de columnas."""
        self.clear()
        for row in rows:
            # usar el primer campo como iid si existe
            iid = row[0] if len(row) > 0 else None
            try:
                self.tree.insert("", "end", iid=iid, values=row)
            except Exception:
                self.tree.insert("", "end", values=row)

    def clear(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

    def get_selected(self):
        sel = self.tree.selection()
        if sel:
            return sel[0]
        return None
