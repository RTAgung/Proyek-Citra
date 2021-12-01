import tkinter as tk
from tkinter import ttk, NW, filedialog, E, W
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from PIL.ImageTk import PhotoImage
from matplotlib import pyplot as plt


import cv2
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

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
    show_hist()


def open_img():
    global matrix_img
    global panel
    x = filename

    matrix_img = cv2.imread(x)
    matrix_img = cv2.resize(matrix_img, dsize=(630, 270), interpolation=cv2.INTER_CUBIC)
    matrix_img = cv2.cvtColor(matrix_img, cv2.COLOR_BGR2RGB)

    img = ImageTk.PhotoImage(image=Image.fromarray(matrix_img))

    panel = tk.Label(citra_left, image=img)
    panel.image = img
    panel.pack()


def show_hist():
    global matrix_img

    x = filename

    matrix_img = cv2.imread(x)
    matrix_img = cv2.resize(matrix_img, dsize=(480, 270), interpolation=cv2.INTER_CUBIC)
    matrix_img = cv2.cvtColor(matrix_img, cv2.COLOR_BGR2RGB)

    histr = cv2.calcHist([matrix_img], [0], None, [256], [0, 256])

    '''f = Figure(figsize=(1, 1), dpi=50)
    a = f.add_subplot()
    canvas = FigureCanvasTkAgg(f, hist_left)
    canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)'''

    plt.plot(histr)
    plt.savefig('hist_left.png')

    matrix_img_hist = cv2.imread('hist_left.png')
    matrix_img_hist = cv2.resize(matrix_img_hist, dsize=(480, 90), interpolation=cv2.INTER_CUBIC)
    matrix_img_hist = cv2.cvtColor(matrix_img_hist, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(image=Image.fromarray(matrix_img_hist))

    panel = tk.Label(hist_left, image=img)
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

# button
'''image = Image.open('play.png')
image = image.resize((30,30))
play = PhotoImage(file ='play.png')'''

b_hist_left = tk.Button(frame_mid, text ="show histogram", width=20)
b_hist_left.grid(row=0, column=0, padx=10, pady=15)

b_play = tk.Button(frame_mid, text ="process", width=20)
b_play.grid(row=0, column=1, padx=390, pady=15)

b_hist_right = tk.Button(frame_mid, text ="show histogram", width=20)
b_hist_right.grid(row=0, column=2, padx=10, pady=15, sticky=W)


# bottom ===============================================================================================================
frame_bottom = tk.Frame(master=window, height=250, bd=1, relief="raised")
frame_bottom.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# bottom left
bot_left = tk.Frame(master=frame_bottom, bd=1, width=640, height=250, relief="raised")
bot_left.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# button
b_tresholding = tk.Button(bot_left, text ="Tresholding", width=15)
b_tresholding.grid(row=0, column=0, padx=5, pady=5)

b_equalization = tk.Button(bot_left, text ="Equalization", width=15)
b_equalization.grid(row=0, column=1, padx=5, pady=5)

b_sketch = tk.Button(bot_left, text ="Sketch", width=15)
b_sketch.grid(row=0, column=2, padx=5, pady=5)

b_blur = tk.Button(bot_left, text ="Blur", width=15)
b_blur.grid(row=1, column=0, padx=5, pady=5)

b_gray = tk.Button(bot_left, text ="Grayscale", width=15)
b_gray.grid(row=1, column=1, padx=5, pady=5)

b_bright = tk.Button(bot_left, text ="Brightness", width=15)
b_bright.grid(row=1, column=2, padx=5, pady=5)

b_negative = tk.Button(bot_left, text ="Negative", width=15)
b_negative.grid(row=2, column=0, padx=5, pady=5)

b_mirror = tk.Button(bot_left, text ="Mirroring", width=15)
b_mirror.grid(row=2, column=1, padx=5, pady=5)

b_sharpening = tk.Button(bot_left, text ="Sharpening", width=15)
b_sharpening.grid(row=2, column=2, padx=5, pady=5)

b_edge_detect = tk.Button(bot_left, text ="Edge Detection", width=15)
b_edge_detect.grid(row=3, column=0, padx=5, pady=5)

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