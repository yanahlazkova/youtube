from pytube import YouTube
import windowError

# link = "https://youtu.be/tNSjC0sZiy8"

def download_video(link):
    
    try:
        yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
        is_download = yt.streams.get_highest_resolution().download("videos")
        
        return True # Download Complete!
    except Exception as e:
        windowError.open_window_error(e)
     

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
        windowError.open_window_error("YouTube link is invalid")

    
# show_data_video("https://youtu.be/tNSjC0sZiy8")