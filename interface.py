import tkinter as tk
from tkinter import filedialog
import pandas as pd
import smtplib
import getpass


root= tk.Tk()

canvas1 = tk.Canvas(root, width = 720, height = 360, bg = 'tomato')
canvas1.pack()

def getExcel ():
    global df
    
    import_file_path = filedialog.askopenfilename()
    df = pd.concat(pd.read_excel(import_file_path, sheet_name=None))
    root.destroy()
    return df
     


browseButton_Excel = tk.Button(text='Import Excel File', command=getExcel, bg='black', fg='tomato', font=('verdana', 12, 'bold'))
canvas1.create_window(360, 180, window=browseButton_Excel)


    



root.mainloop()



