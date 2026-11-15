import tkinter as tk


class MainWindow:

    def __init__(self, root):
        self.root = root

        self.root.title("QCU - Course Registration System")
        self.root.geometry("1280x800")
        self.root.minsize(1000, 650)

        self.root.configure(bg="#F1F3F5")

        self.build_layout()

    def build_layout(self):
        def build_layout(self):
            # Header
            self.header = tk.Frame(
                self.root,
                bg="white",
                height=75
            )
            self.header.pack(fill="x")
            self.header.pack_propagate(False)

            # Main body
            self.body = tk.Frame(
                self.root,
                bg="#F1F3F5"
            )
            self.body.pack(fill="both", expand=True)

            # Sidebar
            self.sidebar = tk.Frame(
                self.body,
                bg="#07549C",
                width=220
            )
            self.sidebar.pack(side="left", fill="y")
            self.sidebar.pack_propagate(False)

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