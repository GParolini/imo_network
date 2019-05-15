#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:14:09 2019

@author: giudittaparolini
"""
import pandas as pd
import os
import seaborn as sns
import matplotlib.pyplot as plt


#Count plot of the members attendance all meetings
def count_plot_members_all(df):
     sns.set(style="darkgrid")
     sns.set(rc={"figure.figsize":(14,25)})
     sns.countplot(y="Surname", data=df, order = df["Surname"].value_counts().index)
     

#Histogram of the members attendance for interwar meetings
def hist_members_int():
    df_int= pd.read_csv(os.path.join("..", "3_printouts", "members_counts_int.csv"), sep=',',header=None, index_col =0)
    df_int.plot(kind='barh')
    plt.ylabel('Surname')
    plt.xlabel('Count')
    plt.title('Attendance during interwar years')
    return
    
#Plot of the age distribution
def plot_age_members(my_dict):
    for key in my_dict:
        plt.scatter(my_dict[key], [key], label=key)
    return
    
#Plot of the geographic distribution (nation)
def plot_nation_members(my_dict):
    for key in my_dict:
        plt.scatter(my_dict[key], [key], label=key)
        plt.xticks(fontsize=10, rotation=90)
    return

#Plot of the geographic distribution (city)
def plot_city_members(my_dict):
    for key in my_dict:
        plt.scatter(my_dict[key], [key], label=key)
        plt.xticks(fontsize=10, rotation=90)
    return
    
#Plot of the field distribution
def plot_field_members(my_dict):
   for key in my_dict:
        plt.scatter(my_dict[key], [key], label=key)
        plt.xticks(fontsize=10, rotation=90)
   return
        
