from pytube import YouTube
from tkinter import messagebox
import windowMessage, os


def download(link):

    is_download = download_video(link)
    # if link=""
    if is_download:
        path = os.path.dirname(is_download)
        windowMessage.show_message_link("Download Complete... ", path)


def download_video(link):

    try:
        # yt = YouTube(link, on_complete_callback=windowMessage.open_window_message("Message...", "Download complete!"))
        yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        # messagebox.showinfo("Сообщение", "Перейдите по ссылке")

        # is_download = yt.streams.get_highest_resolution().download("videos")
        # return is_download # Download Complete!
    except Exception as e:
        windowMessage.open_window_error(e)


def show_data_video(link):
    try:
        yt = YouTube(link)

        title = yt.title
        author = yt.author
        image = yt.thumbnail_url
        video = {"title": title, "author": author, "image": image}
        print("Title: ", yt.title)
        print("Video: ", yt.views)
        print("Url miniature: ", yt.thumbnail_url)
        print("Author: ", yt.author)
        return video
    except:
        windowMessage.open_window_error("YouTube link is invalid")


# show_data_video("https://youtu.be/tNSjC0sZiy8")
