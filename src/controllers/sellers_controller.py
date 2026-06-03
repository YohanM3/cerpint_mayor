from src.views.components.sellers_view import SellersView


class SellersController:
    def __init__(self, content_area):
        self.content_area = content_area

    def display_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        self.view = SellersView(self.content_area)
        self.view.pack(fill="both", expand=True)
