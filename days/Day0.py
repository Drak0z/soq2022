# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:59:55 2022

@author: peter.davids
"""

from days.GenericDay import GenericDay

class Day0(GenericDay):
    def __init__(self, target):
        GenericDay.__init__(self, "Day0 solution")
        self.target = target
        
    def getSolution(self):
        base = 2
        power = 1
        while (self.target is not None and pow(base, power)) < self.target:
            power += 1
            
        return pow(base, power)
    
