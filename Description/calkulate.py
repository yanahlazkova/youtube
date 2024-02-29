import customtkinter
import tkinter

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

customtkinter.set_ctk_parent_class(tkinter.Tk)

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


root = customtkinter.CTk()
root.geometry("400x400")
root.title("Feet to Meters")

mainframe = customtkinter.CTkFrame(master=root) # ttk.Frame(root, padding="3 3 12 12")
mainframe.pack(pady=20, padx=60, fill="both", expand=True) # mainframe.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# feet = StringVar()
feet_entry = customtkinter.CTkEntry(master=mainframe, placeholder_text="0")
feet_entry.pack(pady=10, padx=10) # feet_entry.grid(column=2, row=1, sticky=(W, E))

meters = StringVar()
meters = customtkinter.CTkLabel(master=mainframe, justify=customtkinter.LEFT, textvariable="meters") # ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
meters.pack(pady=10, padx=10)
# ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

# ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
# ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
# ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

# for child in mainframe.winfo_children(): 
#     child.grid_configure(padx=5, pady=5)

# feet_entry.focus()
# root.bind("<Return>", calculate)

root.mainloop()