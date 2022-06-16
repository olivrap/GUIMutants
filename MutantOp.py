import tkinter as tk
from tkinter import filedialog
import sys

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
f = open(file_path, "r")

code  = f.read()
codeAux = code.replace("Rafa", "okay", 1) 

print(codeAux)


#



