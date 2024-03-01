import customtkinter
from customtkinter.windows.widgets.core_widget_classes.ctk_base_class import CTkImage
import tkinter as tk
import downloadFile
from tkinter import messagebox
import urllib.request
import io
from PIL import Image, ImageTk
import listUrls

# вывод приложение по центру экрана
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

# получает введенный линк и вызывает функцию вывода данных о загружаемом видео
def show_video_data():
    link_video = input_link.get()
    if link_video == "":
        messagebox.showerror("Error...", "You didn't enter anything")
    else:
        
        video = downloadFile.show_data_video(link_video)
        if video:
            video_name.configure(state="normal")
            video_name.insert("1.0", video["title"])
            video_name.configure(state="disabled")
          
            video_author.configure(text=video["author"])
            
            button_download.configure(state="normal")
            
            
            # вывод картинки
            image_url = video["image"]
            response = urllib.request.urlopen(image_url)
            image_data = response.read()
            image = Image.open(io.BytesIO(image_data))
            image = image.resize((250, int(image.height * (250 / image.width))), Image.BILINEAR)
            photo_image = ImageTk.PhotoImage(image)

            video_image.configure(image=photo_image)


        else:
            print("ERROR.....", video)
          
def download():
    link = input_link.get()
    is_download = downloadFile.download_video(link)
    print("Download Complete: ", is_download)   

customtkinter.set_ctk_parent_class(tk.Tk)


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"

# Тему можно создать свою, подключив json файл
customtkinter.set_default_color_theme("../my_files/blue.json")

app = customtkinter.CTk()
app.title("Dounload from YouTube")
app_width = 400
app_height = 400

center_window(app, app_width, app_height)

text_link = customtkinter.CTkLabel(app, text="URL: ") # text_color="lightblue"
text_link.grid(row=0, column=0, padx=10, pady=20, sticky="e")

url_var = tk.StringVar(value="Enter video link")
list_urls = [url['url'] for url in listUrls.list_urls]
input_link = customtkinter.CTkComboBox(app, variable=url_var, values=list_urls)
input_link.grid(row=0, column=1, padx=10, sticky="ew", columnspan=2)
app.columnconfigure(1, weight=1)

button_OK = customtkinter.CTkButton(app, text="OK", width=10, command=show_video_data)
button_OK.grid(row=0, column=3, padx=10, sticky="e")

text_title = customtkinter.CTkLabel(app, text="Name: ") #, text_color="blue"
text_title.grid(row=1, column=0, padx=10, sticky="e")

video_name = customtkinter.CTkTextbox(app, text_color="lightblue", 
                                      activate_scrollbars=False, 
                                      state="disabled", 
                                      wrap="word", 
                                      height=50, 
                                      width=300)
video_name.grid(row=1, column=1, padx=10, sticky="w", columnspan=4, rowspan=2)

text_autor = customtkinter.CTkLabel(app, text="Autor: ") #, text_color="blue"
text_autor.grid(row=3, column=0, padx=10, sticky="e")

video_author = customtkinter.CTkLabel(app, text="", text_color="lightblue")
video_author.grid(row=3, column=1, padx=10, sticky="w", columnspan=4)

text_image = customtkinter.CTkLabel(app, text="Image: ")
text_image.grid(row=6, column=0, padx=10, sticky="e")

video_image = customtkinter.CTkLabel(app, text="", compound="bottom")
video_image.grid(row=6, column=1, padx=20, pady=20, columnspan=4)
app.columnconfigure(1, weight=1)

button_download = customtkinter.CTkButton(app, text="Download", state="disabled", command=download)
button_download.grid(row=8, column=1, padx=20, pady=20, columnspan=2)
app.columnconfigure(0, weight=1)





app.mainloop()


# frame_1 = customtkinter.CTkFrame(master=app,  width=300, height=50, border_width=2, border_color="lightblue")
# frame_1.grid(row=0, column=0)
# frame_1.grid(pady=20, padx=20)

# text_link = customtkinter.CTkLabel(frame_1, text="URL:", fg_color="transparent", text_color="lightblue", anchor="w")
# # text_link.grid()

# frame_1 = customtkinter.CTkFrame(app, padding="10 10 20 20", border_width=2, border_color="lightgray")
# frame_1.grid(column=0, row=0, sticky="nsew")

# https://customtkinter.tomschimansky.com/documentation/widgets/button
# https://tkdocs.com/shipman/
# https://ru.stackoverflow.com/questions/tagged/customtkinter

# https://python-scripts.com/tkinter
