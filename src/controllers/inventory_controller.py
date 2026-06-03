from src.views.components.inventory_view import InventoryView
from src.utils.ui_helpers import create_page_container


class InventoryController:
    def __init__(self, content_area):
        self.content_area = content_area

    def display_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        page = create_page_container(self.content_area)
        self.view = InventoryView(page)
        self.view.pack(fill="both", expand=True)
