import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()


file_path = filedialog.askopenfilename("Select the file to be muted")
