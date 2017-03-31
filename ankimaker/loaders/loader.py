# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 15:14:08 2017

@author: carles
"""
import tkinter
from tkinter import ttk
from tkinter import filedialog

class Loader(ttk.LabelFrame):
    
    def __init__(self, parent, text):
        super().__init__(parent, text = text, height = 125, width = 320)
        self.init_frame()
        self.parent = parent
        self.grid_propagate(0)
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
        
    def init_frame(self):
        pass
        
    def hide(self):
        pass
    
    
    