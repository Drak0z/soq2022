# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 09:59:31 2022

@author: peter.davids
"""

import tkinter as tk
from days.Day0 import Day0
from days.Day1 import Day1
from days.Day2 import Day2
from days.Day3 import Day3
from days.Day4 import Day4
from days.Day5 import Day5
from days.Day6 import Day6
from days.Day7 import Day7

# Test Cases
# Day0 - First power of 2 to go over 10 is 16
t0 = Day0(10)
assert t0.getSolution() == 16
del t0

# Day1 given: Sum of multiples of 3, 4, 5 below 20 is 133
t1 = Day1(20)
assert t1.getSolution() == 133
del t1 

# Day2 given: 1103 is the "first" primetime, 13 people collect a dollar, and we select 1 day, then the outcome is 13 dollars
t2 = Day2(1, 1100, 1104)
assert t2.getSolution() == 13
del t2 

# Day3: Simple data file with 4 records, where one animal weighs 3 times as much as the others
t3 = Day3("./data/day3_testdata.csv")
assert t3.getSolution() == 60
del t3

# Day4: Given input testdata, produce 7498 as output
t4 = Day4("./data/day4_testdata.txt", "./data/day4_foods.csv")
assert t4.getSolution() == 7498
del t4


# Day4: Given input testdata, produce 12 as output
t7 = Day7("./data/day7_sheepsum.test.txt")
assert t7.getSolution() == 12
del t7

# Actual implementation
#Let's make ourselves a window with buttons
root = tk.Tk()
root.title("Stampede of Quorum 2022 - Main Runner")

window_width = 600
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)

def_button_width = 20
def_button_height = 2

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

#Day 0 button (08-07-2022)
d0 = Day0(1000000)
d0_button = tk.Button(root, text = 'Solve Day0', command = d0.solve)
d0_button.grid(row=1, column=0, padx=2, pady=2)

#Day 1 button (09-07-2022)
d1 = Day1(1000)
d1_button = tk.Button(root, text = 'Solve Day1', command = d1.solve)
d1_button.grid(row=1, column=1, padx=2, pady=2)

#Day 2 button (10-07-2022)
d2 = Day2(10, 1100, 2400)
d2_button = tk.Button(root, text = 'Solve Day2', command = d2.solve)
d2_button.grid(row=1, column=2, padx=2, pady=2)

#Day 3 button (11-07-2022)
d3 = Day3("./data/day3_data.csv")
d3_button = tk.Button(root, text = 'Solve Day3', command = d3.solve)
d3_button.grid(row=2, column=0, padx=2, pady=2)

#Day 4 button (12-07-2022)
d4 = Day4("./data/day4_map.txt", "./data/day4_foods.csv")
d4_button = tk.Button(root, text = 'Solve Day4', command = d4.solve)
d4_button.grid(row=2, column=1, padx=2, pady=2)


d5 = Day5("CUbWn UWffUi.UsioUh q.Whaf ZUliXinUehiqUcnUWffmUqcnbUsiolUNcenieUWhZUsiolUZcmYiUZWhY mVUQb hUCUqWmUsiolUWa Uq Uom ZUniUom UqWmbchaUgWYbch mUniUmnil UZWnWVUufmiUjf Wm UjcYeUojUjloh mVU aamVUWhZU.ilnsUm p hUfcnl mUi.UsiolU.Wpilcn UYiiechaUicfV")
d5_button = tk.Button(root, text = 'Solve Day5', command = d5.solve)
d5_button.grid(row=2, column=2, padx=2, pady=2)


d6 = Day6()
d6_button = tk.Button(root, text = 'Solve Day6', command = d6.solve)
d6_button.grid(row=3, column=0, padx=2, pady=2)


d7 = Day7("./data/day7_sheepsum.2.txt")
d7_button = tk.Button(root, text = 'Solve Day7', command = d7.solve)
d7_button.grid(row=3, column=1, padx=2, pady=2)

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()