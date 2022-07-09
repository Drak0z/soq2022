# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 09:59:31 2022

@author: peter.davids
"""

import tkinter as tk
from days.Day0 import Day0
from days.Day1 import Day1
from days.Day2 import Day2

# Test Cases
# Day0 - First power of 2 to go over 10 is 16
t0 = Day0(10)
assert t0.getSolution() == 16
del t0

# Day1 given: Sum of multiples of 3, 4, 5 below 20 is 133
t1 = Day1(20)
assert t1.getSolution() == 133
del t1 

# Day2 given: 1103 is the "first" primetime, 13 people collect a dollar, and we select 1 day
t2 = Day2(1, 1100, 1104)
assert t2.getSolution() == 13
del t2 

# Actual implementation
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


d0 = Day0(1000000)
d0_button = tk.Button(root, text = 'Solve Day0', command = d0.solve)
d0_button.grid(row=1, column=0, padx=2, pady=2)


d1 = Day1(1000)
d1_button = tk.Button(root, text = 'Solve Day1', command = d1.solve)
d1_button.grid(row=1, column=1, padx=2, pady=2)

d2 = Day2(10, 1100, 2400)
d2_button = tk.Button(root, text = 'Solve Day2', command = d2.solve)
d2_button.grid(row=1, column=2, padx=2, pady=2)

try:
    from ctypes import windll

    windll.shcore.SetProcessDpiAwareness(1)
finally:
    root.mainloop()