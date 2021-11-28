import tkinter
from tkinter import *

# window
main_window = tkinter.Tk()
main_window.geometry("1280x720")

# main panel
main_panel = PanedWindow(orient=VERTICAL, bd=1, relief="raised", bg="blue")
main_panel.pack(fill=BOTH, expand=1)

# top panel ============================================================================================================
top_panel = PanedWindow(main_panel, orient=HORIZONTAL, bd=1, relief="raised", bg="red")
main_panel.add(top_panel, height=420)

top_left = PanedWindow(top_panel, orient=VERTICAL)
top_panel.add(top_left, width=640)

top_right = PanedWindow(top_panel, orient=VERTICAL)
top_panel.add(top_right, width=640)

# mid panel ============================================================================================================
mid_panel = PanedWindow(main_panel, orient=VERTICAL)
main_panel.add(mid_panel, height=50)

# bottom panel =========================================================================================================
bottom_panel = PanedWindow(main_panel, orient=HORIZONTAL, bd=1, relief="raised", bg="red")
main_panel.add(bottom_panel, height=250)

bot_left = PanedWindow(bottom_panel, orient=VERTICAL)
bottom_panel.add(bot_left, width=640)

bot_right = PanedWindow(bottom_panel, orient=VERTICAL)
bottom_panel.add(bot_right, width=640)




main_window.mainloop()

"""
top_label = tkinter.Label(main_panel, text="top panel")
main_panel.add(top_label, height=400)

mid_label = tkinter.Label(main_panel, text="middle panel")
main_panel.add(mid_label, height=70)

bottom_label = tkinter.Label(main_panel, text="bottom panel")
main_panel.add(bottom_label, height=250)

def click_event():
    clickLabel = tkinter.Label(main_window, text="Test tekan")
    clickLabel.pack()


label = tkinter.Label(main_window, text="Test Program \n ini GUI")
button = tkinter.Button(main_window, text="Tombol Testing", command=click_event)

label.pack()
button.pack()
"""

