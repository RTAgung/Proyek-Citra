import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

window = tk.Tk()
window.geometry("1280x720")

filename = ''


def select_file():
    global filename

    filetypes = (
        ('image files', '*.jpeg'),
        ('image files', '*.jpg'),
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


# create a toplevel menu
menubar = tk.Menu()
menubar.add_command(label="Open File", command=select_file)
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
citra_left = tk.Frame(master=top_left, bd=1, width=640, height=320, relief="raised")
citra_left.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# hist left
hist_left = tk.Frame(master=top_left, bd=1, width=640, height=100, relief="raised")
hist_left.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

# top right
top_right = tk.Frame(master=frame_top, bd=1, width=640, height=420, relief="raised")
top_right.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# citra right
citra_right = tk.Frame(master=top_right, bd=1, width=640, height=320, relief="raised")
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
