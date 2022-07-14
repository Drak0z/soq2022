# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:59:55 2022

@author: peter.davids
"""

from days.GenericDay import GenericDay
import pandas as pd

class Day7(GenericDay):
        
    def __init__(self, fileName):
        GenericDay.__init__(self, "Day7 solution")
        self.fileName = fileName
        #self.fileName = "./data/day7_sheepsum.2.txt"

    def readFile(self):
        text_file = open(self.fileName, "r")
        lines = [line.strip() for line in text_file.readlines()]
        return lines

    def getSolution(self):
        twoOf = 0
        threeOf = 0
        
        file = self.readFile()
        
        for line in file:
            data = pd.Series(list(line)).value_counts()
            if 2 in data.values: 
                twoOf += 1 
            if 3 in data.values: 
                threeOf += 1 
        
        print (f"{twoOf} * {threeOf} = {twoOf*threeOf}")
        return twoOf * threeOf
    
