'''
Day 2 Puzzle 1 Advent of code 2024

Red-Nosed reports
'''

from pathlib import Path

import numpy as np
import pandas as pd

# get input file
path = Path(__file__).resolve().parents[1] # get grandparent directory of this script
#print(path)
input_path = f'{path}\\input.txt'
#print(input_path)

# read input file using pandas
reports = np.array(pd.read_csv(input_path, header = None))
print(reports[0], reports[0][0]) # check this only shows one report - it does :D

# # begin to determine if reports are safe or unsafe
# for report in reports: # single out each report
#     print(report)
    
#     # get difference between each number in the report
#     grad = np.diff(report)
#     print(grad)