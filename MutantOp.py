import tkinter as tk
import os
import pathlib
from tkinter import filedialog
import sys

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
f = open(file_path, "r")
code  = f.read()

def replacer(s, newstring, index, nofail=False):
    # raise an error if index is outside of the string
    if not nofail and index not in range(len(s)):
        raise ValueError("index outside given string")

    # if not erroring, but the index is still not in the correct range..
    if index < 0:  # add it to the beginning
        return newstring + s
    if index > len(s):  # add it to the end
        return s + newstring

    # insert the new string between "slices" of the original
    return s[:index] + newstring + s[index + 1:]

def saveMO(filePath, MOName, MOCode, count):
    filename = os.path.basename(filePath) 
    from pathlib import Path
    path = Path(filePath)
    root = path.parent.absolute()
    dir = MOName
    pathRew = os.path.join(root, dir)
    if (pathRew)
    try:
        os.mkdir(pathRew)
    except FileExistsError:
        # directory is already created
        print("Directory " , pathRew ,  " already exists")
    try: 
        fileMO = pathRew+"/"+str(count)+filename
        mo_File = open(fileMO, "w")
        mo_File.write(MOCode)
    except Exception:
        # file generation failed
        print("Something went wrong -- refresh your folder")

def rew(writtenCode): #mutant generation for REW mutant operators    
    if writtenCode.find("add("):
        count = 1;
        initialPos = writtenCode.find("add(")-1
        finalPos = len(writtenCode)
        while (-1 != writtenCode.find(".add(", initialPos, finalPos)):
            pos = writtenCode.find(".add(", initialPos, finalPos)
            lastLine = writtenCode.rfind('\n', 0, pos)
            newString = replacer(writtenCode, "\n\t//", lastLine)
            saveMO(file_path, "rew", newString, count)
            count +=1;
            initialPos = 1+writtenCode.find(".add(", initialPos, finalPos)
        print(count," GUI-based mutants generated from REW") 
    else:
        print("No mutants were created from REW")
     

def numbers_to_strings(op): #switch case based on user's option
    match op:
        case "all":
            print("-- all of the Mutant operators are being applied --")
            return "implement all of the mutant operators"
        case "rew": #GUI mutant operators 01
            rew(code)
            return "MO - Remove Existing Widget"
        case "swi": #GUI mutant operators 02
            return  "SWI - Set Widget Invisible"   
        case _:
            return "unknow command - please, do it again" 


def main():
    ### reading user's option on how to create the GUI-based mutants
    op = sys.argv[1]
    print(numbers_to_strings(op))  


##calling our main
if __name__== "__main__":
   main()