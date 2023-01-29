# Import Required Dependencies
import tkinter
import customtkinter
from pytube  import YouTube

y = 22 # Variable for checking Quality

# Choose Quality
def optionmenu_callback(choice):
    global y
    if(choice=="720p"):
        y=22
    elif(choice=="360p"):
        y=18
    elif(choice=="144p"):
        y=17
    else:
        y=140

# Start Download
def startDownload():
    finishLabel.configure(text="")
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_by_itag(y)
        video.download()
        finishLabel.configure(text="Download Successful")
        finishLabel.configure(text_color="green")
    except:
        finishLabel.configure(text="Invalid Link")
        finishLabel.configure(text_color="red")
    
# Manage Progress Bar
def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = bytes_downloaded/total_size * 100
    per = str(int(percentage))
    progress.configure(text=per+"%")
    progress.update()
    progressBar.set(float(percentage)/100)
    

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

# App frame
app = customtkinter.CTk()
app.geometry("640x400")
app.title("YouTube Downloader 🌱")

# Add UI Elements
title = customtkinter.CTkLabel(app,text="Insert YouTube Link :",font=("default",18))
title.pack(padx=10,pady=10)

# Link Input
link = customtkinter.CTkEntry(app,width=300, height=30)
link.pack(padx=10,pady=10)

# Choices Dropdown
drop = customtkinter.CTkOptionMenu(app, values=["720p", "360p", "144p" , "Audio"],command=optionmenu_callback)
drop.pack(padx=10,pady=10)

# Progress Percentage
progress = customtkinter.CTkLabel(app,text="0%")
progress.pack(padx=10,pady=0)
progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

# Download Button
button = customtkinter.CTkButton(app, text="Download", command=startDownload)
button.pack(padx=10,pady=10)

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack(padx=10,pady=10)

# Run App
app.mainloop()