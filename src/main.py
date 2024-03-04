import customtkinter
import tkinter as tk
from interface import center_window, display_app


app = customtkinter.CTk()
customtkinter.set_ctk_parent_class(tk.Tk)
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"

# Тему можно создать свою, подключив json файл
customtkinter.set_default_color_theme("./themes/blue.json")

app.title("Dounload from YouTube")
app_width = 400
app_height = 400

center_window(app, app_width, app_height)

display_app(app)
app.mainloop()
