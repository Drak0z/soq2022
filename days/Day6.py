# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:59:55 2022

@author: peter.davids
"""

from days.GenericDay import GenericDay

class Day6(GenericDay):
    class Art(object):
        def __init__(self, data_length):
            self.art_map = []
            self.data_length = data_length
            pass
        
        def expandY(self, max_y):
            y = len(self.art_map)
            while y <= max_y:
                self.art_map.append([])
                y += 1
                pass
            pass
        
        def expandX(self, y, max_x):                
            x = len(self.art_map[y])
            while x <= max_x:
                self.art_map[y].append("".ljust(self.data_length, " "))
                x += 1
                pass
            pass
            
        def addDataAt(self, data, x, y):
            data = data.ljust(self.data_length, " ")
            self.expandY(y)
            self.expandX(y, x)
            self.art_map[y][x] = data
            pass
        
        def __str__(self):
            result = ""
            for y in range(len(self.art_map)):
                for x in range(len(self.art_map[y])):
                    result += self.art_map[y][x]
                result += "\n"
                pass
            return result
            
        
    def __init__(self):
        GenericDay.__init__(self, "Day6 solution")
        self.fileName = "./data/day6_data.csv"

    def readFile(self):
        text_file = open(self.fileName, "r")
        lines = [line.strip() for line in text_file.readlines()]
        return lines

    def getSolution(self):
        data_length = 8
        
        art = self.Art(data_length)
        garbledData = self.readFile()
        
        for i in range(len(garbledData)):
            line = garbledData[i]
            col = line.split(",")
            y = int(col[0])
            x = int(col[1])
            data = str(col[2])
            art.addDataAt(data, x, y)

        print(art)
            
        return str(art)
    
