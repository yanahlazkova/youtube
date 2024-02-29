import customtkinter
import tkinter



def open_window_error(text_error):
    def close_app():
        app.destroy()
    
    customtkinter.set_ctk_parent_class(tkinter.Tk)
    customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
    customtkinter.set_default_color_theme("./my_files/blue.json")

    app = customtkinter.CTk()
    app.title("Error...")
    app.geometry("250x100")

    text_error = customtkinter.CTkLabel(app, text=text_error, 
                                        text_color="red", 
                                        font=("", 14))
    text_error.grid(row=0, column=0, padx=20, pady=20)
    
    button = customtkinter.CTkButton(app, text="Close", command=close_app)
    app.columnconfigure(0, weight=1)
    button.grid()


    app.mainloop()
    
# open_window_error()
