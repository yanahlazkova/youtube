# import customtkinter
# import tkinter
from tkinter import messagebox

def open_window_message(text_title, text_message):
    messagebox.showinfo(text_title, text_message)


def open_window_error(text_error):
    messagebox.showerror("Error...", text_error)
    
    # def close_app():
    #     app.destroy()
    
    # customtkinter.set_ctk_parent_class(tkinter.Tk)
    # customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    # customtkinter.set_default_color_theme("./my_files/blue.json")

    # app = customtkinter.CTk()
    # app.title("Error...")
    # app.geometry("350x200")

    # text_error = customtkinter.CTkLabel(app, text=text_error, 
    #                                     text_color="red", 
    #                                     font=("", 14))
    # text_error.grid(row=0, column=0, padx=20, pady=20)
    
    # button = customtkinter.CTkButton(app, text="Close", command=close_app)
    # app.columnconfigure(0, weight=1)
    # button.grid()


    # app.mainloop()