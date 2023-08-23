from tkinter import Tk, messagebox, Label, Entry, Button, filedialog, StringVar
from PIL import Image, ImageTk
import json
import os
import ctypes

# Function to maximize the window and set it to full screen
def maximize_window():
    main.state('zoomed')

# Function to close the window and stop executing when 'q' is pressed
def close_window(event):
    if event.char.lower() == 'q':
        main.destroy()

main = Tk()
main.title("User Waste Photo Upload Screen")
main.attributes('-fullscreen', True)  # Open the window in full screen

# Set the background image
background_image = Image.open("overlay-bg.jpg")
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
background_photo = ImageTk.PhotoImage(background_image.resize((screen_width, screen_height), Image.ANTIALIAS))
background_label = Label(main, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Maximize the window on startup
maximize_window()

name = StringVar()
location = StringVar()
desc = StringVar()
photo = StringVar()
video_path = ""

def upload_video():
    global video_path
    video_path = filedialog.askopenfilename(initialdir="videos")
    video_entry.delete(0, 'end')
    video_entry.insert(0, video_path)

count = 1  # Initial count value

def save():
    global count
    details = {
        "name": name.get(),
        "location": location.get(),
        "description": desc.get(),
        "photo_path": photo.get(),
        "video_path": video_path
    }
    directory = "C:/Users/LENOVO/OneDrive/Desktop/portfolio/Major/user_details/"
    os.makedirs(directory, exist_ok=True)  # Create the directory if it doesn't exist
    file_name = os.path.join(directory, f"user_details_{count}.json")
    with open(file_name, "w") as file:
        json.dump(details, file)
    count += 1  # Increment the count value
    messagebox.showinfo("Details Accepted", "Your image, video, and details have been sent to waste collectors")

font = ('times', 15, 'bold')

# Create a transparent image for title background
title_bg = Image.new("RGBA", (560, 50), (255, 255, 255, 0))
title_photo = ImageTk.PhotoImage(title_bg)

# Create a label with transparent image as background
title_label = Label(main, image=title_photo, text='Geo Tracking of Waste and Triggering Alerts using Deep Learning',
                    justify='left', compound='center', font=font, fg='black')
title_label.place(x=50, y=10, width=560, height=50)

font1 = ('times', 14, 'bold')
l1 = Label(main, text="Username * ")
l1.place(x=50, y=100)
l1.config(font=font1)
username_entry = Entry(main, textvariable=name)
username_entry.place(x=250, y=100)

l2 = Label(main, text="Location * ")
l2.place(x=50, y=150)
l2.config(font=font1)
location_entry = Entry(main, textvariable=location)
location_entry.place(x=250, y=150)

l3 = Label(main, text="Description * ")
l3.place(x=50, y=200)
l3.config(font=font1)
desc_entry = Entry(main, textvariable=desc)
desc_entry.place(x=250, y=200)

l4 = Label(main, text="Video Path * ")
l4.place(x=50, y=250)
l4.config(font=font1)
video_entry = Entry(main)
video_entry.place(x=250, y=250)

upload_video_button = Button(main, text="Upload Video", command=upload_video)
upload_video_button.place(x=400, y=250)
upload_video_button.config(font=font1)

savebutton = Button(main, text="Save Request", command=save)
savebutton.place(x=170, y=300)
savebutton.config(font=font1)

# Bind the 'q' key press event to the close_window function
main.bind('<Key>', close_window)

main.mainloop()
