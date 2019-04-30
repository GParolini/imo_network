#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:34:14 2019

@author: giudittaparolini
"""

import pandas as pd
import os
import print_methods as pr
import plot_methods as pl
import utilities as ut


df = pd.read_csv(os.path.join("..", "1_data", "df_clean_all.csv"))
df_int = pd.read_csv(os.path.join("..", "1_data", "df_clean_int.csv"))

#Get members
members = pr.get_members(df)
ut.print_txt_printouts (members, "members_list.txt")

#Get value counts members all years
members_counts_all = pr.get_members_counts(df)
ut.print_csv_printouts (members_counts_all, "members_counts_all.csv")

#Get value counts members interwar years
members_counts_int = pr.get_members_counts(df_int)
ut.print_csv_printouts (members_counts_int, "members_counts_int.csv")

#Plot the members counts for all years
fig1 = pl.count_plot_members_all(df)
ut.print_plot(fig1, "plot_members_counts_all.png")

#Plot the members counts for the interwar years
fig2 = pl.hist_members_int()
ut.print_plot(fig2, "plot_members_hist_int.png")
