# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:59:55 2022

@author: peter.davids
"""

from days.GenericDay import GenericDay
import pandas as pd

import tkinter as tk
import tkinter.ttk as ttk
import threading, queue

class Day3(GenericDay):
    class Scale():
        def __init__(self):
            self.animals = [None] * 4
            self.animals_lr = [None] * 4
            return
            
        def numAnimals(self):
            num = 0
            for a in self.animals:
                if a is not None: num+=1
            return num
        
        def isBalanced(self):
            return self.getLeftWeight() > 0 and self.getLeftWeight() == self.getRightWeight()
        
        def getWeight(self, pos): 
            weight = 0
            for i in range (len(self.animals)):
                if (self.animals_lr[i]==pos): 
                    weight += self.animals[i].Weight
            return weight
        
        def getLeftWeight(self): 
            return self.getWeight('l')

        def getRightWeight(self): 
            return self.getWeight('r')
        
        def setAnimal(self, pos, face, animal):
            for a in range(len(self.animals)):
                if a != pos and self.animals[a] is not None and self.animals[a].Animal == animal.Animal:
                    return False
            self.animals[pos] = animal
            self.animals_lr[pos] = face
            return True
        
        def toString(self):
            left_str = ""
            right_str = " "
            for i in range(len(self.animals)):
                animal_str = ""
                if self.animals[i].Species == 'sheep': animal_icon = "🐑"
                elif self.animals[i].Species == 'cow': animal_icon = "🐄"
                
                animal_str += (f"[{animal_icon} {self.animals[i].Animal} ({self.animals[i].Weight}g)] ")
                if self.animals_lr[i] == 'l': left_str += animal_str
                elif self.animals_lr[i] == 'r': right_str += animal_str
            
            scale_str = "-^-"
            if self.getLeftWeight() > self.getRightWeight():
                scale_str = "_^‾"
            elif self.getLeftWeight() < self.getRightWeight():
                scale_str = "‾^_"                
            return (str(left_str + scale_str + right_str))
                        
    def __init__(self, dataFile):
        GenericDay.__init__(self, "Day3 solution")
        self.dataFile = dataFile
    
    def loadData(self, dataFile):
        df = pd.read_csv(dataFile)
        return df
      
    def balanceAnimal(self, df, s, n):
        if n == 4 and s.isBalanced(): 
                return s
        
        if n >= 4:
            return None
        
        for a in range(df.shape[0]):
            
            for pos_a in ['l', 'r']:
                if s.setAnimal(n, pos_a, df.iloc[a]):
                    result = self.balanceAnimal(df, s, n+1)
                    if result is not None: return result
        
        return None
                
    def getSolutionObj(self):
        df = self.loadData(self.dataFile)
        
        s = self.Scale()
        result_scale = self.balanceAnimal(df, s, 0)
        return result_scale
    
    def getSolution(self):
        return self.getSolutionObj().getLeftWeight()
    
    # There must be a cleaner way to do this....
    def solve(self):
        def finishProgress():
            popup.progress.stop()
            popup.progress.destroy()
            popup.progress = ttk.Progressbar(popup, orient=tk.HORIZONTAL, mode='determinate')
            popup.progress['value'] = 100
            popup.progress.pack()
            #popup.progress.destroy()
        
        def work(self, q):
            s = self.getSolutionObj()
            finishProgress()
            
            solution = tk.Text(popup, height=4, width=len(s.toString())+4)
            solution.insert(tk.END, f'Solution:\n{s.getLeftWeight()}\nScale:\n{s.toString()}')
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
