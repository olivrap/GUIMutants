import tkinter as tk
import os #file manipulation
import pathlib
from tkinter import filedialog
import sys

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
f = open(file_path, "r")

code  = f.read()
codeAux = code.replace("Rafa", "okay", 1) 

print(codeAux)

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
    try:
        os.mkdir(pathRew)
    except FileExistsError:
        print("Directory " , pathRew ,  " already exists")

    try: 
        fileMO = pathRew+"/"+str(count)+filename
        mo_File = open(fileMO, "w")
        mo_File.write(MOCode)
    except Exception:
        print("Something went wrong -- refresh your folder")



    ## parent = f.parent.absolute()
    ## print(parent)
    ##if not os.filePath.exists(filePath.parent)



def rew(writtenCode):
    
    if writtenCode.find("add("):
        count = 1;
        initialPos = writtenCode.find("add(")-1
        finalPos = len(writtenCode)

        while (-1 != writtenCode.find(".add(", initialPos, finalPos)):
            ## print("Achei", writtenCode.find(".add", initialPos, finalPos))
            pos = writtenCode.find(".add(", initialPos, finalPos)
            lastLine = writtenCode.rfind('\n', 0, pos)
            newString = replacer(writtenCode, "\n\t//", lastLine)
            saveMO(file_path, "rew", newString, count)
            count +=1;
            initialPos = 1+writtenCode.find(".add(", initialPos, finalPos)
                  
       # initialPos = writtenCode.rfind('\n', 0, pos)
    else:
        print("No mutants created to REW")

"""
    while writtenCode.rfind('\n', 0, pos):
        pos = writtenCode.find("add")
        num += 1
        print("Ocorrencia ", num)
        initialPos = pos
        

    if writtenCode.find("add"):
        print("yes, we can")
        pos = writtenCode.find("add")
        lastLine = writtenCode.rfind('\n', 0, pos)
        print("Position ", pos)
        print("Last bn", lastLine)
        newString = replacer(writtenCode, "\n\t//", lastLine)
        print("---------------\n\n\n")
        print(newString)
        print("---------------\n\n\n")
        saveMO(file_path, "rew", newString)
        print("identificar widgets e removê-los\n criar uma pasta (se já existir, sobrescrever)\n salvar os códigos mutados\n fechar a pasta")
    #identificar widgets e removê-los
    #criar uma pasta (se já existir, sobrescrever)
    #salvar os códigos mutados
    #fechar a pasta
"""

def numbers_to_strings(op):
    match op:
        case "all":
            print("-- all of the Mutant operators are being applied --")
            return "implement all of the mutant operators"
        case "rew":
            rew(codeAux)
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
