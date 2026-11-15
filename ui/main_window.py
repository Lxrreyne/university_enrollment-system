import tkinter as tk

from .components.header import Header
from .components.sidebar import Sidebar

class MainWindow:

    def __init__(self, root):
        self.root = root

        self.root.title("QCU - Course Registration System")
        self.root.geometry("1280x800")
        self.root.minsize(1000, 650)

        self.root.configure(bg="#F1F3F5")

        self.build_layout()

    def build_layout(self):
        # Header
        self.header = Header(self.root)
        self.header.pack(fill="x")

        # Main body
        self.body = tk.Frame(
            self.root,
            bg="#F1F3F5"
        )
        self.body.pack(
            fill="both",
            expand=True
        )

        # Sidebar
        self.sidebar = Sidebar(
            self.body,
            self.show_page
        )
        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # Page container
        self.page_container = tk.Frame(
            self.body,
            bg="#F1F3F5"
        )
        self.page_container.pack(
            side="left",
            fill="both",
            expand=True
        )

        # Default page
        self.sidebar.set_active("Dashboard")
        self.show_page("Dashboard")

    def show_page(self, page_name):

        # Clear the previous page
        for widget in self.page_container.winfo_children():
            widget.destroy()

        # Page title
        title = tk.Label(
            self.page_container,
            text=page_name,
            font=("Arial", 23, "bold"),
            fg="#07549C",
            bg="#F1F3F5"
        )

        title.pack(
            anchor="w",
            padx=30,
            pady=(30, 5)
        )

        # Temporary description
        description = tk.Label(
            self.page_container,
            text=f"{page_name} page will be displayed here.",
            font=("Arial", 10),
            fg="#555555",
            bg="#F1F3F5"
        )

        description.pack(
            anchor="w",
            padx=30
        )