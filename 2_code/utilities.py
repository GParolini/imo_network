#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:23:39 2019

@author: giudittaparolini
"""

import csv
import os
import matplotlib.pyplot as plt


# Print to a csv file in the folder 1_data
def print_csv_data (df, filename):
    df.to_csv(os.path.join("..", "1_data", filename))


# Print to a txt file in the folder 3_printouts
def print_txt_printouts (to_be_printed, filename):
    with open(os.path.join("..", "3_printouts", filename),'w') as outfile:
        for item in to_be_printed:
            print(item, file=outfile)
       
# Print to a csv file in the folder 3_printouts
def print_csv_printouts (df, filename):
    df.to_csv(os.path.join("..", "3_printouts", filename), header=None)
    
# Print a dictionary to a csv file in 3_printouts
def printdict_csv_printouts (my_dict, filename):
    with open(os.path.join("..", "3_printouts", filename), 'w') as f:
        for key in my_dict.keys():
            f.write("%s,%s\n"%(key,my_dict[key]))

# Print a jpg figure in the folder 4_plots
def print_plot (fig, filename):
    plt.savefig(os.path.join("..", "4_plots", filename))
    plt.close()
    

