from src.views.components.customers_view import CustomerView

class CustomerController:
    def __init__(self, content_area):
        self.content_area =content_area

    def display_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        self.view = CustomerView(self.content_area)
        self.view.pack(fill="both", expand=True)
