import tkinter as tk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
from matplotlib import pyplot as plt

import cv2
from PIL import Image, ImageTk

from RTAgung import RTA
from Regina import Regina
from Zahra import Zahra


class Citra:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("1280x720")

        self.filename = ''
        self.matrix_img_left = None
        self.matrix_img_right = None
        self.matrix_hist_left = None
        self.matrix_hist_right = None

        self.rta = RTA(self.matrix_img_left)
        self.ina = Regina(self.matrix_img_left)
        self.zhr = Zahra(self.matrix_img_left)

        # create a toplevel menu
        menubar = tk.Menu()
        menubar.add_command(label="Open File", command=self.open_file)
        menubar.add_command(label="Save File", command=self.save_file)

        # display the menu
        self.window.config(menu=menubar)

        # TOP
        self.top_frame()

        # MID
        frame_mid = tk.Frame(master=self.window, height=10, bd=1, relief="raised")
        frame_mid.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        # BOT
        self.bot_frame()

        self.window.mainloop()

    def top_frame(self):
        # TOP
        frame_top = tk.Frame(master=self.window, width=200, height=420, bd=1, relief="raised")
        frame_top.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        # top left
        top_left = tk.Frame(master=frame_top, bd=1, width=640, height=420, relief="raised")
        top_left.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # citra left
        citra_left = tk.Frame(master=top_left, bd=1, width=640, height=280, relief="raised")
        citra_left.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        self.panel_img_left = tk.Label(citra_left, width=640)
        self.panel_img_left.pack()

        # hist left
        hist_left = tk.Frame(master=top_left, bd=1, width=640, height=200, relief="raised")
        hist_left.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        self.panel_hist_left = tk.Label(hist_left, width=640)
        self.panel_hist_left.pack()

        # top right
        top_right = tk.Frame(master=frame_top, bd=1, width=640, height=420, relief="raised")
        top_right.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # citra right
        citra_right = tk.Frame(master=top_right, bd=1, width=640, height=280, relief="raised")
        citra_right.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        self.panel_img_right = tk.Label(citra_right, width=640)
        self.panel_img_right.pack()

        # hist right
        hist_right = tk.Frame(master=top_right, bd=1, width=640, height=200, relief="raised")
        hist_right.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        self.panel_hist_right = tk.Label(hist_right, width=640)
        self.panel_hist_right.pack()

    def bot_frame(self):
        frame_bottom = tk.Frame(master=self.window, height=250, bd=1, relief="raised")
        frame_bottom.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        # bottom left
        bot_left = tk.Frame(master=frame_bottom, bd=1, width=640, height=250, relief="raised")
        bot_left.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # bottom right
        self.bot_right = tk.Frame(master=frame_bottom, bd=1, width=640, height=250, relief="raised")
        self.bot_right.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # button
        self.b_tresholding = tk.Button(bot_left, text="Tresholding", width=15, command=self.frame_tresh)
        self.b_tresholding.grid(row=0, column=0, padx=5, pady=5)

        self.b_equalization = tk.Button(bot_left, text="Equalization", width=15, command=self.frame_equal)
        self.b_equalization.grid(row=0, column=1, padx=5, pady=5)

        self.b_sketch = tk.Button(bot_left, text="Sketch", width=15, command=self.frame_sketch)
        self.b_sketch.grid(row=0, column=2, padx=5, pady=5)

        self.b_blur = tk.Button(bot_left, text="Blur", width=15, command=self.frame_blur)
        self.b_blur.grid(row=1, column=0, padx=5, pady=5)

        self.b_gray = tk.Button(bot_left, text="Grayscale", width=15, command=self.frame_gray)
        self.b_gray.grid(row=1, column=1, padx=5, pady=5)

        self.b_bright = tk.Button(bot_left, text="Brightness", width=15, command=self.frame_brightening)
        self.b_bright.grid(row=1, column=2, padx=5, pady=5)

        self.b_negative = tk.Button(bot_left, text="Negative", width=15, command=self.frame_negative)
        self.b_negative.grid(row=2, column=0, padx=5, pady=5)

        self.b_mirror = tk.Button(bot_left, text="Mirroring", width=15, command=self.frame_mirror)
        self.b_mirror.grid(row=2, column=1, padx=5, pady=5)

        self.b_sharpening = tk.Button(bot_left, text="Sharpening", width=15, command=self.frame_sharp)
        self.b_sharpening.grid(row=2, column=2, padx=5, pady=5)

        self.b_edge_detect = tk.Button(bot_left, text="Edge Detection", width=15, command=self.frame_edge_detect)
        self.b_edge_detect.grid(row=3, column=0, padx=5, pady=5)

    def open_file(self):
        filetypes = (
            ('image files', '*.jpeg'),
            ('image files', '*.JPEG'),
            ('image files', '*.jpg'),
            ('image files', '*.JPG'),
            ('image files', '*.png'),
        )

        self.filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        showinfo(
            title='Selected File',
            message=self.filename
        )

        self.show_img_left()
        self.show_hist_left()

    def save_file(self):
        self.matrix_img_right = cv2.cvtColor(self.matrix_img_right, cv2.COLOR_BGR2RGB)
        save_path = "result_image\\" + os.path.basename(self.filename)
        cv2.imwrite(save_path, self.matrix_img_right)

        showinfo(
            title='Image Saved',
            message=save_path
        )

    def show_img_left(self):
        self.matrix_img_left = cv2.imread(self.filename)
        self.matrix_img_left = cv2.resize(self.matrix_img_left, dsize=(533, 300), interpolation=cv2.INTER_CUBIC)
        self.matrix_img_left = cv2.cvtColor(self.matrix_img_left, cv2.COLOR_BGR2RGB)

        img = ImageTk.PhotoImage(image=Image.fromarray(self.matrix_img_left))

        self.panel_img_left.configure(image=img)
        self.panel_img_left.image = img

        self.rta.update_img(self.matrix_img_left)
        self.ina.update_img(self.matrix_img_left)
        self.zhr.update_img(self.matrix_img_left)

    def show_img_right(self):
        img = ImageTk.PhotoImage(image=Image.fromarray(self.matrix_img_right))

        self.panel_img_right.configure(image=img)
        self.panel_img_right.image = img
        self.show_hist_right()

    def show_hist_left(self):
        plt.figure(figsize=(22, 7))

        x = self.matrix_img_left
        b, g, r = cv2.split(x)
        b = b.flatten()
        g = g.flatten()
        r = r.flatten()
        num_bins = 255
        plt.hist(b, num_bins, color='blue', alpha=0.8)
        plt.hist(g, num_bins, color='green', alpha=0.8)
        plt.hist(r, num_bins, color='red', alpha=0.8)
        plt.xlim([0, 255])
        plt.savefig('hist_left.png')

        matrix_img_hist = cv2.imread('hist_left.png')
        matrix_img_hist = cv2.resize(matrix_img_hist, dsize=(640, 170), interpolation=cv2.INTER_CUBIC)
        matrix_img_hist = cv2.cvtColor(matrix_img_hist, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(image=Image.fromarray(matrix_img_hist))

        self.panel_hist_left.configure(image=img)
        self.panel_hist_left.image = img

    def show_hist_right(self):
        plt.figure(figsize=(22, 7))

        x = self.matrix_img_right
        num_bins = 255
        if x.ndim == 2:
            x = x.flatten()
            plt.hist(x, num_bins, color='black', alpha=0.8)
        else:
            b, g, r = cv2.split(x)
            b = b.flatten()
            g = g.flatten()
            r = r.flatten()
            plt.hist(b, num_bins, color='blue', alpha=0.8)
            plt.hist(g, num_bins, color='green', alpha=0.8)
            plt.hist(r, num_bins, color='red', alpha=0.8)

        plt.xlim([0, 255])
        plt.savefig('hist_right.png')

        matrix_img_hist = cv2.imread('hist_right.png')
        matrix_img_hist = cv2.resize(matrix_img_hist, dsize=(640, 170), interpolation=cv2.INTER_CUBIC)
        matrix_img_hist = cv2.cvtColor(matrix_img_hist, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(image=Image.fromarray(matrix_img_hist))

        self.panel_hist_right.configure(image=img)
        self.panel_hist_right.image = img

    def frame_gray(self):
        panel_gray = None
        close_btn = None

        def button_action():
            self.matrix_img_right = self.rta.to_grayscale()
            self.show_img_right()

        def close_panel():
            panel_gray.destroy()
            close_btn.destroy()

        panel_gray = tk.Button(self.bot_right, text="Process", command=button_action)
        panel_gray.pack()
        close_btn = tk.Button(self.bot_right, text="Close", command=close_panel)
        close_btn.pack()

    def frame_negative(self):
        panel_negative = None
        close_btn = None

        def button_action():
            self.matrix_img_right = self.rta.to_negative()
            self.show_img_right()

        def close_panel():
            panel_negative.destroy()
            close_btn.destroy()

        panel_negative = tk.Button(self.bot_right, text="Process", command=button_action)
        panel_negative.pack()
        close_btn = tk.Button(self.bot_right, text="Close", command=close_panel)
        close_btn.pack()

    def frame_brightening(self):
        panel_bright = None
        close_btn = None
        slider_input = None

        def button_action():
            data = slider_input.get()
            self.matrix_img_right = self.rta.brightening(data)
            self.show_img_right()

        def close_panel():
            panel_bright.destroy()
            close_btn.destroy()
            slider_input.destroy()

        slider_input = tk.Scale(self.bot_right, from_=-255, to=255, orient=tk.HORIZONTAL)
        slider_input.set(0)
        slider_input.pack()
        panel_bright = tk.Button(self.bot_right, text="Process", command=button_action)
        panel_bright.pack()
        close_btn = tk.Button(self.bot_right, text="Close", command=close_panel)
        close_btn.pack()

    def frame_edge_detect(self):
        panel_edge = None
        close_btn = None

        def button_action():
            self.matrix_img_right = self.rta.edge_detection()
            self.show_img_right()

        def close_panel():
            panel_edge.destroy()
            close_btn.destroy()

        panel_edge = tk.Button(self.bot_right, text="Process", command=button_action)
        panel_edge.pack()
        close_btn = tk.Button(self.bot_right, text="Close", command=close_panel)
        close_btn.pack()

    def frame_sketch(self):
        panel_sketch = None
        close_btn = None

        def button_action():
            self.matrix_img_right = self.ina.sketching()
            self.show_img_right()

        def close_panel():
            panel_sketch.destroy()
            close_btn.destroy()

        panel_sketch = tk.Button(self.bot_right, text="Process", command=button_action)
        panel_sketch.pack()
        close_btn = tk.Button(self.bot_right, text="Close", command=close_panel)
        close_btn.pack()

    def frame_blur(self):
        panel_blur = None
        close_btn = None
        var = tk.IntVar()

        def button_action():
            self.matrix_img_right = self.ina.blurring(var.get())
            self.show_img_right()

        def close_panel():
            panel_blur.destroy()
            close_btn.destroy()
            B0.destroy()
            B1.destroy()
            B2.destroy()
            B3.destroy()
            B4.destroy()

        B0 = tk.Radiobutton(self.bot_right, text="Gaussian Blur", variable=var, value=0)
        B0.pack()
        B1 = tk.Radiobutton(self.bot_right, text="Averaging Blur", variable=var, value=1)
        B1.pack()
        B2 = tk.Radiobutton(self.bot_right, text="Median Blurring", variable=var, value=2)
        B2.pack()
        B3 = tk.Radiobutton(self.bot_right, text="Bilateral Blurring", variable=var, value=3)
        B3.pack()
        B4 = tk.Radiobutton(self.bot_right, text="Blurring (Standard)", variable=var, value=4)
        B4.pack()

        panel_blur = tk.Button(self.bot_right, text="Process", command=button_action)
        panel_blur.pack()
        close_btn = tk.Button(self.bot_right, text="Close", command=close_panel)
        close_btn.pack()

    def frame_equal(self):
        panel_equal = None
        close_btn = None

        def button_action():
            self.matrix_img_right = self.ina.equalizationing()
            self.show_img_right()

        def close_panel():
            panel_equal.destroy()
            close_btn.destroy()

        panel_equal = tk.Button(self.bot_right, text="Process", command=button_action)
        panel_equal.pack()
        close_btn = tk.Button(self.bot_right, text="Close", command=close_panel)
        close_btn.pack()
    
    def frame_tresh(self):
        panel_tresh = None
        close_btn = None
        slider_input = None

        def button_action():
            data = slider_input.get()
            self.matrix_img_right = self.zhr.tresholding(th=data)
            self.show_img_right()

        def close_panel():
            panel_tresh.destroy()
            close_btn.destroy()
            slider_input.destroy()
        
        slider_input = tk.Scale(self.bot_right, from_=0, to=255, orient=tk.HORIZONTAL)
        slider_input.set(128)
        slider_input.pack()

        panel_tresh = tk.Button(self.bot_right, text="Process", command=button_action)
        panel_tresh.pack()
        close_btn = tk.Button(self.bot_right, text="Close", command=close_panel)
        close_btn.pack()

    def frame_mirror(self):
        panel_mirror = None
        close_btn = None
        var = tk.IntVar()

        def button_action():
            self.matrix_img_right = self.zhr.mirroring(var.get())
            self.show_img_right()

        def close_panel():
            panel_mirror.destroy()
            close_btn.destroy()
            B0.destroy()
            B1.destroy()
            B2.destroy()
        
        B0 = tk.Radiobutton(self.bot_right, text="Flip Vertical", variable=var, value=0)
        B0.pack()
        B1 = tk.Radiobutton(self.bot_right, text="Flip Horizontal", variable=var, value=1)
        B1.pack()
        B2 = tk.Radiobutton(self.bot_right, text="Flip Vertical & Horizontal", variable=var, value=-1)
        B2.pack()

        panel_mirror = tk.Button(self.bot_right, text="Process", command=button_action)
        panel_mirror.pack()
        close_btn = tk.Button(self.bot_right, text="Close", command=close_panel)
        close_btn.pack()

    def frame_sharp(self):
        panel_sharp = None
        close_btn = None

        def button_action():
            self.matrix_img_right = self.zhr.sharpening()
            self.show_img_right()

        def close_panel():
            panel_sharp.destroy()
            close_btn.destroy()
        
        panel_sharp = tk.Button(self.bot_right, text="Process", command=button_action)
        panel_sharp.pack()
        close_btn = tk.Button(self.bot_right, text="Close", command=close_panel)
        close_btn.pack()

Citra()
