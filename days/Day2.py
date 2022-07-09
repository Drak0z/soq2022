# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:59:55 2022

@author: peter.davids
"""

from days.GenericDay import GenericDay
import math

class Day2(GenericDay):
    def __init__(self, days, fromTime, toTime):
        GenericDay.__init__(self, "Day2 solution")
        self.days = days
        self.fromTime = fromTime
        self.toTime = toTime
        
    def isPrime(self, n):
        for i in range(2,int(math.sqrt(n))+1):
          if (n%i) == 0:
            return False
        return True
       
    def getSolution(self):
        result = 0
        hh = 11
        
        while hh < 24:
            mi = 00
            while mi<60 and (hh*100+mi) < self.toTime:
                if (self.isPrime(hh*100+mi)):
                    result += 13
                mi += 1
            hh += 1
        
        result *= self.days
        return result
    
