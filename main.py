import customtkinter
import tkinter
import downloadFile
import windowError
import urllib.request
import io
from PIL import Image, ImageTk

# вывод приложение по центру экрана
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    
    window.geometry(f"{width}x{height}+{x}+{y}")

# получает введенный линк и вызывает функцию вывода данных о загружаемом видео
def show_video_data():
    # link_video = input_link.configure(textvariable="https://youtu.be/tNSjC0sZiy8")
    

    link_video = input_link.get()
    if link_video == "":
        windowError.open_window_error("You didn't enter anything")
    else:
        
        video = downloadFile.show_data_video(link_video)
        # print("video: ", video)
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
            image.thumbnail((250,250))
            # image = image.resize((100))
            photo_image = ImageTk.PhotoImage(image)

            video_image.configure(image=photo_image)


        else:
            print("ERROR.....", video)
          
def download():
    link = input_link.get()
    is_download = downloadFile.download_video(link)
    print("Download Complete: ", is_download)   

customtkinter.set_ctk_parent_class(tkinter.Tk)


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"

# Тему можно создать свою, подключив json файл
# customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("./my_files/blue.json")
# customtkinter.set_default_color_theme("./my_files/dark-blue.json")

app = customtkinter.CTk()
app.title("Dounload from YouTube")
# app.geometry("400x400")
app_width = 400
app_height = 400

center_window(app, app_width, app_height)

text_link = customtkinter.CTkLabel(app, text="URL: ") # text_color="lightblue"
text_link.grid(row=0, column=0, padx=10, pady=20, sticky="e")

url_var = tkinter.StringVar()
input_link = customtkinter.CTkEntry(app, placeholder_text="Enter video link ", textvariable=url_var)
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


# video = loaded.download_video("https://youtu.be/tNSjC0sZiy8") # ("https://youtu.be/tNSjC0sZiy8")



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