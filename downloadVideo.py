import pytube

link = "youtube.com/watch?v=qu8X8UxBjjM&list=PPSV"
yt = pytube.YouTube(link)
yt.streams.get_highest_resolution().download()
print("downloaded", link)