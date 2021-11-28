import tkinter as tk
from tkinter import ttk, NW, filedialog
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import cv2
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("1280x720")

filename = ''
matrix_img = None


def open_file():
    global filename

    filetypes = (
        ('image files', '*.jpeg'),
        ('image files', '*.JPEG'),
        ('image files', '*.jpg'),
        ('image files', '*.JPG'),
        ('image files', '*.png'),
    )

    filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected File',
        message=filename
    )

    open_img()


def open_img():
    global matrix_img
    global panel
    x = filename

    matrix_img = cv2.imread(x)
    matrix_img = cv2.resize(matrix_img, dsize=(480, 270), interpolation=cv2.INTER_CUBIC)
    matrix_img = cv2.cvtColor(matrix_img, cv2.COLOR_BGR2RGB)

    img = ImageTk.PhotoImage(image=Image.fromarray(matrix_img))

    panel = tk.Label(citra_left, image=img)
    panel.image = img
    panel.pack()


# create a toplevel menu
menubar = tk.Menu()
menubar.add_command(label="Open File", command=open_file)
menubar.add_command(label="Save File", command=window.quit)

# display the menu
window.config(menu=menubar)

# top ==================================================================================================================
frame_top = tk.Frame(master=window, width=200, height=420, bd=1, relief="raised")
frame_top.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# top left
top_left = tk.Frame(master=frame_top, bd=1, width=640, height=420, relief="raised")
top_left.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# citra left
citra_left = tk.Frame(master=top_left, bd=1, width=640, height=280, relief="raised")
citra_left.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# hist left
hist_left = tk.Frame(master=top_left, bd=1, width=640, height=100, relief="raised")
hist_left.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# top right
top_right = tk.Frame(master=frame_top, bd=1, width=640, height=420, relief="raised")
top_right.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# citra right
citra_right = tk.Frame(master=top_right, bd=1, width=640, height=280, relief="raised")
citra_right.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# hist right
hist_right = tk.Frame(master=top_right, bd=1, width=640, height=100, relief="raised")
hist_right.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


# mid ==================================================================================================================
frame_mid = tk.Frame(master=window, height=50, bd=1, relief="raised")
frame_mid.pack(fill=tk.BOTH, side=tk.TOP, expand=True)


# bottom ===============================================================================================================
frame_bottom = tk.Frame(master=window, height=250, bd=1, relief="raised")
frame_bottom.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# bottom left
bot_left = tk.Frame(master=frame_bottom, bd=1, width=640, height=250, relief="raised")
bot_left.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# bottom right
bot_right = tk.Frame(master=frame_bottom, bd=1, width=640, height=250, relief="raised")
bot_right.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

window.mainloop()


'''
def open_img():
global matrix_img
x = filename
matrix_img = cv2.imread(x)
matrix_img = cv2.resize(matrix_img, dsize=(480, 270), interpolation=cv2.INTER_CUBIC)
img = ImageTk.PhotoImage(image=Image.fromarray(matrix_img))
panel = tk.Label(citra_left, image=img)
panel.image = img
panel.pack()


canvas = tk.Canvas(citra_left, width=300, height=300)
canvas.pack()
img = ImageTk.PhotoImage(Image.open(filename))
canvas.create_image(20, 20, anchor=NW, image=img)
'''