# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:59:55 2022

@author: peter.davids
"""

from days.GenericDay import GenericDay
import math

class Day8(GenericDay):
        
    def __init__(self, fileName, nComposite):
        GenericDay.__init__(self, "Day8 solution")
        self.fileName = fileName
        self.nComposite = nComposite
        #self.fileName = "./data/day7_sheepsum.2.txt"

    def readFile(self):
        text_file = open(self.fileName, "r")
        lines = [line.strip() for line in text_file.readlines()]
        return lines
      
    # Can I reuse/import this from day2 somehow?
    def isPrime(self, n):
        for i in range(2,int(math.sqrt(n))+1):
          if (n%i) == 0:
            return False
        return True
    
    def isEven(self, x):
        return x%2 == 0
    
    def findNthCompositeNumber(self, n):
        numberFound = 0
        x = 0
        while numberFound < n:
            x += 1
            # If a number is not a prime, and it is larger than 1, it is a composite
            if (x > 3 and not self.isPrime(x) and self.isEven(x)):
                numberFound += 1
        return x
    

    def getSolution(self):
        names = self.readFile()
        entry = self.findNthCompositeNumber(self.nComposite)
        
        return names[entry-1]
    
