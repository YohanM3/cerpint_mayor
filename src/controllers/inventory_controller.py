from src.views.components.inventory_view import InventoryView

class InventoryController:
    def __init__(self, content_area):
        self.content_area = content_area

    def display_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        self.view = InventoryView(self.content_area)
        self.view.pack(fill="both", expand=True)
