from src.views.components.sales_view import SalesView

class SalesController:
    def __init__(self, content_area):
        self.content_area = content_area

    def display_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        self.view = SalesView(self.content_area)
        self.view.pack(fill="both", expand=True)
