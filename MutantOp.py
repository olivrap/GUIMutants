import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()


f = open(file_path, "r")
code  = print(f.read())



