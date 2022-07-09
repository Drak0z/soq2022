# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 12:47:08 2022

@author: peter.davids
"""

import tkinter as tk
import tkinter.ttk as ttk
import threading, queue

class GenericDay:
    def __init__(self, name):
        self.name = name
        
    def getSolution():
        raise NotImplementedError
       
    def solve(self):
        def finishProgress():
            popup.progress.stop()
            popup.progress.destroy()
            popup.progress = ttk.Progressbar(popup, orient=tk.HORIZONTAL, mode='determinate')
            popup.progress['value'] = 100
            popup.progress.pack()
            #popup.progress.destroy()
        
        def work(self, q):
            s = self.getSolution()
            finishProgress()
            
            solution = tk.Text(popup, height=2, width=30)
            solution.insert(tk.END, 'Solution:\n{0}'.format(str(s)))
            solution.pack()
            
        popup = tk.Tk()
        popup.title(self.name)
        
        popup.progress = ttk.Progressbar(popup, orient=tk.HORIZONTAL, mode='indeterminate')
        popup.progress.start()
        popup.progress.pack()
                
        q=queue.Queue()
        threading.Thread(target=work, args=(self, q), daemon=True).start()
        
        try:
            from ctypes import windll
        
            windll.shcore.SetProcessDpiAwareness(1)
        finally:
            popup.mainloop()
            