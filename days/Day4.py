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

class Day4(GenericDay):
    class Map(object):
        def __init__(self, midwayMap):
            self.midwayMap = midwayMap
            self.width = len(midwayMap[0])
            self.height = len(midwayMap)
            self.visitedMap = [[0 for x in range(self.width)] for y in range(self.height)]
            self.totalCalories = 0
            
        def visit(self, x, y):
            self.visitedMap[y][x] = 1
            return self.getItem(x, y)
        
        def outOfBounds(self, x, y):
            self.visitedMap[y][x] = 2
        
        def getItem(self, x, y):
            return self.midwayMap[y][x]
        
        def toString(self):
            s = "\033[0;37;40m"
            for y in range(self.height):
                for x in range(self.width):
                    c = self.getItem(x, y)
                    if c == "X":
                        c = "\033[1;30;42m"+ c 
                    elif (self.visitedMap[y][x] == 1):
                        c = "\033[1;30;43m"+ c 
                    elif (self.visitedMap[y][x] == 2):
                        c = "\033[1;30;41m"+ c 
                    else:
                        c = "\033[0;37;40m" + c
                    s += c
                s += "\n\033[0;37;40m"
            return s
        

        def toPlainString(self):
            s = ""
            for y in range(self.height):
                for x in range(self.width):
                    c = self.getItem(x, y)
                    if c == "X":
                        c = c
                    elif (self.visitedMap[y][x] == 1):
                        c = c
                    elif (self.visitedMap[y][x] == 2):
                        c = c
                    else:
                        c = c
                    s += c
                s += "\n"
            return s
            
    class Food(object):
        def __init__(self, food, calories, symbol, direction):
            self.food = food
            self.calories = calories
            self.symbol = symbol
            self.direction = direction
            pass
            
    class Position(object):
        def __init__(self):
            self.x = 0
            self.y = 0
            self.direction = 1 #N:0, E:1, S:2, W:3
            pass
        
        def turn(self, direction):
            self.direction += direction
            self.direction %= 4
                    
        def turnLeft(self):
            self.turn(-1)
            
        def turnRight(self):
            self.turn(1)
            
        def move(self):
            if(self.direction == 0): # Move North
                self.y -= 1
            elif(self.direction == 1): # Move East
                self.x += 1
            elif(self.direction == 2): # Move South
                self.y += 1
            elif(self.direction == 3): # Move West
                self.x -= 1
        
        def toString(self):
            return f"[{self.x},{self.y}]"
    # // Position
    
    def __init__(self, fileName, foodFile):
        GenericDay.__init__(self, "Day4 solution")
        self.fileName = fileName
        self.foodDf = pd.read_csv(foodFile)
    
    def readFile(self):
        text_file = open(self.fileName, "r")
        lines = [line.strip() for line in text_file.readlines()]
        
        return lines
    
    def findStartPosition(self, midwayMap):
        pos = self.Position()
        pos.x = 0
        pos.y = 0
        
        for y in range(midwayMap.height):
            for x in range(midwayMap.width):
                char = midwayMap.getItem(x, y)
                if char == "X":
                    pos.x = x
                    pos.y = y
                    return pos
            
        return None # No valid starting position
    
           
    def getSolutionObj(self):
        midwayMap = self.Map(self.readFile())
        
        pos = self.findStartPosition(midwayMap)
        
        outOfBounds = False
        while(not outOfBounds):
            prev_x = pos.x
            prev_y = pos.y
            pos.move()
            if (pos.x < 0 or pos.x >= midwayMap.width or pos.y < 0 or pos.y >= midwayMap.height):
                midwayMap.outOfBounds(prev_x, prev_y)
                outOfBounds = True
            else:
                item = midwayMap.visit(pos.x, pos.y)

                if item != ".":
                    idx = self.foodDf.loc[self.foodDf["Map Symbol"] == item] 
                    food = idx.iloc[0]
                    midwayMap.totalCalories += food.Calories
                    if (food.Direction == "L"):
                        pos.turnLeft()
                    elif(food.Direction == "R"):
                        pos.turnRight()
                    elif(food.Direction == "F"):
                        pass # We automatically "move forward" next cycle
                        
        return midwayMap
    
    def getSolution(self):
        return self.getSolutionObj().totalCalories
    
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
            m = str(s.toString())
            solution = tk.Text(popup, height=2+s.height, width=s.width)
            solution.insert(tk.END, f'Solution:\n{s.totalCalories}\nMap:\n{s.toPlainString()}')
            
            solution.tag_configure("visited", background="yellow")
            solution.tag_configure("start", background="green")
            solution.tag_configure("oob", background="red")
            
            for y in range(s.height):
                for x in range(s.width):   
                    c = s.getItem(x, y)
                    if c == "X":
                        solution.tag_add("start", f"{y+4}.0+{x}c")
                    elif (s.visitedMap[y][x] == 1):
                        solution.tag_add("visited", f"{y+4}.0+{x}c")
                    elif (s.visitedMap[y][x] == 2):
                        solution.tag_add("oob", f"{y+4}.0+{x}c")
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
        
    