import wikipedia as wky
from tkinter import *
from tkinter import ttk as tk
from ttkthemes import ThemedTk
import webbrowser

gui = ThemedTk(theme="clearlooks")
gui.title("Random Wikipedia Page")

# button commands
def gen_page():
    rand_title = wky.random(pages=1)
    display.delete(0, END)
    display.insert(0, str(rand_title))

def open_page():
    title = str(display.get())
    link  = "https://en.wikipedia.org/wiki/" + title
    webbrowser.open(link, new=1)


# make a search box
display = tk.Entry(width=80)
display.grid(row=0, column=0)
display.insert(0, "Enter a wikipedia page you would like to go to and press \"Go To Page\"")

# buttons
rand_button = tk.Button(gui, text="Generate Random Page", command=gen_page)
open_button = tk.Button(gui, text="Go To Page", command=open_page)

rand_button.grid(row=2, column=0, sticky="nsew")
open_button.grid(row=3, column=0, stick="nsew")

gui.mainloop()