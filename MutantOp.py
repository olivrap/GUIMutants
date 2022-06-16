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

#op = argv[1]


print(sys.argv[1])


print ("Number of arguments:", len(sys.argv))
print ("(Argument List: " , str(sys.argv))




