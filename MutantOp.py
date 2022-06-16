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

def numbers_to_strings(op):
    match op:
        case "all":
            print("-- all of the Mutant operators are being applied --")
            return "implement all of the mutant operators"
        case "rew":
            return "MO - Remove Existing Widget"
        case "swi":
            return  "SWI - Set Widget Invisible"   
        case _:
            return "unknow command" 

op = sys.argv[1]

print(numbers_to_strings(op))    

#cases
#
#
#
#
#
##
