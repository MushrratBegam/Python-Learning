from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("Image slideshow viewer")

#List of image path
image_path = [
    r"C:\Users\mushr\OneDrive\Pictures\WhatsApp Image 2024-12-25 at 23.48.07.jpeg",
    r"C:\Users\mushr\OneDrive\ドキュメント\WhatsApp Image 2025-11-01 at 22.40.23_5f46bf82.jpg",
    r"C:\Users\mushr\OneDrive\ドキュメント\WhatsApp Image 2025-11-01 at 22.40.23_5a33de16.jpg",
    r"C:\Users\mushr\OneDrive\ドキュメント\WhatsApp Image 2025-11-01 at 22.40.23_1c233ddd.jpg",
]

# risize the images to 1080x1080
image_size = (180,180)
images = [Image.open(path). resize(image_size) for path in image_path]
photo_images = [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image = photo_image)
        label.update
        time.sleep(2)
        
slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_path)):
        update_image()
    
play_button = tk.Button(root, text = 'play slideshow', command = start_slideshow)
play_button.pack()

root.mainloop()
        