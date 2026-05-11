"""
Student Record Management System
Main Launcher

Author(s): Gabriell Briones Magdalaga
Date: May 11, 2026
Version: 4.0
"""

import customtkinter as ctk
from src.ui.main_window import MainWindow

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()