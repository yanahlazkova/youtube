import customtkinter
import tkinter, os
from tkinter import messagebox

def open_window_message(text_title, text_message):
    messagebox.showinfo(text_title, text_message)


def open_window_error(text_error):
    messagebox.showerror("Error...", text_error)
    
    
def show_message_link(title, text_link):
    def close_app():
        app.destroy()
        
    def open_directory(event):
        os.startfile(text_link)
        
    customtkinter.set_ctk_parent_class(tkinter.Tk)
    customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("./themes/blue.json")

    app = customtkinter.CTk()
    app.title(title)
    # app.geometry("350x200")

    text_label = customtkinter.CTkLabel(app, text=text_link, text_color="steelblue1", cursor="hand2")
    
    text_label.grid(row=0, column=0, padx=20, pady=20)
    text_label.bind("<Button-1>", open_directory)
    
    button = customtkinter.CTkButton(app, text="Close", command=close_app)
    app.columnconfigure(0, weight=1)
    button.grid(pady=20)


    app.mainloop()