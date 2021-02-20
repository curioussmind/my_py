import tkinter
from pytube import YouTube

root = tkinter.Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Youtube video downloader")

tkinter.Label(root, text="Youtube Video Downloader", font="arial 20 bold").pack()

# Enter the link
link = tkinter.StringVar()
tkinter.Label(root, text='Paste link here:', font='arial 15 bold').place(x=160, y=60)
link_enter = tkinter.Entry(root, width=70, textvariable = link).place(x=32, y=90)

# function to download video
def downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tkinter.Label(root, text='Downloaded', font='arial 15').place(x=180, y=210)

tkinter.Button(root, text='Download', font='arial 15 bold', bg = 'blue', padx = 2, command = downloader).place(x=180, y=150)

root.mainloop()
