import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title("Chương trình đọc ảnh")

image = Image.open("otto.png")
new_size = (400, 400)
image = image.resize(new_size, Image.ANTIALIAS)
otto.imshow("image", image)

img = ImageTk.PhotoImage(image)

label = tk.Label(window, image=img)
label.image = img
label.pack()
window.mainloop()