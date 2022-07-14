# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 10:59:55 2022

@author: peter.davids
"""

from days.GenericDay import GenericDay

class Day6(GenericDay):
    def __init__(self):
        GenericDay.__init__(self, "Day6 solution")
        self.fileName = "./data/day6_data.csv"

    def readFile(self):
        text_file = open(self.fileName, "r")
        lines = [line.strip() for line in text_file.readlines()]
        return lines

    def getSolution(self):
        result = 0
        data_length = 8
        
        art = []
        garbledData = self.readFile()
        
        for i in range(len(garbledData)):
            line = garbledData[i]
            col = line.split(",")
            #col[0] = row
            row = int(col[0])
            #col[1] = column
            column = int(col[1])
            #col[2] = 8-character segment
            data = str(col[2]).ljust(data_length, " ")
            y = len(art)
            while y <= row:
                art.append([])
                y += 1
                
            x = len(art[row])
            while x <= column:
                art[row].append("".ljust(data_length, " "))
                x += 1
            
            #print(f"Data at {row},{column}: {art[row]}")
            art[row][column] = data

        for y in range(len(art)):
            line = ""
            for x in range(len(art[y])):
                line += art[y][x]
            print(line)
            
        return result
    
