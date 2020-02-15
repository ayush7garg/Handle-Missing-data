# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 12:50:03 2020

@author: Ayush Garg
"""

import pandas as pd
import tkinter as tk
from tkinter import filedialog


def handle_missing_data(data):  
    global df
    df = pd.DataFrame(columns=data.columns)
    for i,j in data.iterrows():
        if not(j.isnull().any()):
            j_dict = j.to_dict()
            df = df.append(j_dict,ignore_index=True)
            
    root= tk.Tk()
    
    canvas1 = tk.Canvas(root, width = 300, height = 300, bg = 'lightsteelblue2', relief = 'raised')
    canvas1.pack()
    
    def exportCSV ():
        
        
        export_file_path = filedialog.asksaveasfilename(defaultextension='.csv')
        df.to_csv (export_file_path, index = None, header=True)
        root.destroy()
    
    saveAsButton_CSV = tk.Button(text='Export CSV', command=exportCSV, bg='green', fg='white', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 150, window=saveAsButton_CSV)
    
    root.mainloop()
    