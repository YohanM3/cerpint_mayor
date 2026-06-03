from src.views.components.sales_view import SalesView
from src.utils.ui_helpers import create_page_container


class SalesController:
    def __init__(self, content_area):
        self.content_area = content_area

    def display_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        page = create_page_container(self.content_area)
        self.view = SalesView(page)
        self.view.pack(fill="both", expand=True)
