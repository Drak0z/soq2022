# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:59:55 2022

@author: peter.davids
"""

from days.GenericDay import GenericDay

class Day1(GenericDay):
    def __init__(self, target):
        GenericDay.__init__(self, "Day1 solution")
        self.target = target
       
    def getSolution(self):
        bases = [3,4,5]
        result = 0
        
        for b in bases:
            i = 1
            while i*b < self.target:
                result = result + i*b
                i = i+1
            
        return result
    
