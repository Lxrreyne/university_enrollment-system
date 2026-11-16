import tkinter as tk


class Dashboard:

    def __init__(self, parent):
        self.parent = parent

        self.frame = tk.Frame(
            self.parent,
            bg="#F1F3F5"
        )

        self.frame.pack(fill="both", expand=True)
        self.create_header()

        self.stats_frame = tk.Frame(
            self.frame,
            bg="#F1F3F5"
        )

        self.stats_frame.pack(
            fill="x",
            padx=25,
            pady=10
        )

        # placeholders ========================
        students_card = self.create_stat_card(
            "Total Students",
            "1,250"
        )

        courses_card = self.create_stat_card(
            "Total Courses",
            "45"
        )

        enrollments_card = self.create_stat_card(
            "Total Enrollments",
            "2,340"
        )
        # ===================================

        students_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 10)
        )

        courses_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=10
        )

        enrollments_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(10, 0)
        )

        self.capacity_frame = tk.Frame(
            self.frame,
            bg="#FFFFFF",
            highlightbackground="#D9DDE2",
            highlightthickness=1
        )

        self.capacity_frame.pack(
            fill="x",
            padx=25,
            pady=20
        )

        self.create_capacity_section()

    def create_header(self):
        title = tk.Label(
            self.frame,
            text="Dashboard",
            font=("Arial", 22, "bold"),
            bg="#F1F3F5",
            fg="#07549C"
        )

        title.pack(anchor="w", padx=25, pady=20)


    def create_stat_card(self, title, value):
        card = tk.Frame(
            self.stats_frame,
            bg="#FFFFFF",
            padx=20,
            pady=15,
            highlightbackground="#D9DDE2",
            highlightthickness=1
        )

        label = tk.Label(
            card,
            text=title,
            font=("Arial", 11),
            fg="#555555",
            bg="#FFFFFF"
        )
        label.pack(anchor="w")

        number = tk.Label(
            card,
            text=value,
            font=("Arial", 24, "bold"),
            fg="#07549C",
            bg="#FFFFFF"
        )
        number.pack(anchor="w", pady=(8, 0))

        return card

    def create_capacity_section(self):
        title = tk.Label(
            self.capacity_frame,
            text="Courses Approaching Capacity",
            font=("Arial", 14, "bold"),
            fg="#07549C",
            bg="#FFFFFF"
        )

        title.pack(anchor="w", padx=20, pady=15)