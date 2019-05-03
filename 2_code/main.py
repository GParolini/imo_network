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
df_pre = pd.read_csv(os.path.join("..", "1_data", "df_clean_pre.csv"))
df_int = pd.read_csv(os.path.join("..", "1_data", "df_clean_int.csv"))
df_post = pd.read_csv(os.path.join("..", "1_data", "df_clean_post.csv"))


#Get members all
members_all = pr.get_members(df)
ut.print_txt_printouts (members_all, "members_all_list.txt")

#Get members pre-WWI
members_pre = pr.get_members(df_pre)
ut.print_txt_printouts (members_pre, "members_pre_list.txt")

#Get members interwar years
members_int = pr.get_members(df_int)
ut.print_txt_printouts (members_int, "members_int_list.txt")

#Get members postwar years
members_post = pr.get_members(df_post)
ut.print_txt_printouts (members_post, "members_post_list.txt")

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

#Get birth year all members
birth_year_all = pr.get_members_age(members_all,df)
ut.printdict_csv_printouts (birth_year_all, "members_all_birth_year.csv")

#Plot all members age
fig3 = pl.plot_age_members(birth_year_all)
ut.print_plot(fig3, "plot_age_members_all.png")


#Get birth year interwar members
birth_year_int = pr.get_members_age(members_int,df_int)
ut.printdict_csv_printouts (birth_year_int, "members_int_birth_year.csv")

#Plot interwar members age
fig4 = pl.plot_age_members(birth_year_int)
ut.print_plot(fig4, "plot_age_members_int.png")

#Get birth year post-WWII members
birth_year_post = pr.get_members_age(members_post,df_post)
ut.printdict_csv_printouts (birth_year_post, "members_post_birth_year.csv")

#Plot interwar members age
fig5= pl.plot_age_members(birth_year_post)
ut.print_plot(fig5, "plot_age_members_post.png")

#Get nations all members
nation_all = pr.get_members_nation(members_all,df)
ut.printdict_csv_printouts (nation_all, "members_all_nation.csv")

#Plot nations all members 
fig6= pl.plot_nation_members(nation_all)
ut.print_plot(fig6, "plot_nation_members_all.png")

#Get nations interwar members
nation_int = pr.get_members_nation(members_int,df_int)
ut.printdict_csv_printouts (nation_int, "members_int_nation.csv")

#Plot nations interwar members
fig7= pl.plot_nation_members(nation_int)
ut.print_plot(fig7, "plot_nation_members_int.png")

#Get nations post-WWII members
nation_post = pr.get_members_nation(members_post,df_post)
ut.printdict_csv_printouts (nation_post, "members_int_nation.csv")

#Plot nations post-WWII members
fig8= pl.plot_nation_members(nation_post)
ut.print_plot(fig8, "plot_nation_members_post.png")

#Get cities all members
city_all = pr.get_members_city(members_all,df)
print(city_all)
ut.printdict_csv_printouts (city_all, "members_all_city.csv")

#Plot cities all members 
fig9= pl.plot_city_members(city_all)
ut.print_plot(fig9, "plot_city_members_all.png")

#Get cities interwar members
city_int = pr.get_members_city(members_int,df_int)
ut.printdict_csv_printouts (city_int, "members_int_city.csv")

#Plot cities interwar members
fig10= pl.plot_city_members(city_int)
ut.print_plot(fig10, "plot_city_members_int.png")

#Get cities post-WWII members
city_post = pr.get_members_city(members_post,df_post)
ut.printdict_csv_printouts (city_post, "members_int_city.csv")

#Plot cities post-WWII members
fig11= pl.plot_city_members(city_post)
ut.print_plot(fig11, "plot_city_members_post.png")

#Get field all members
field_all = pr.get_members_field(members_all,df)
ut.printdict_csv_printouts (field_all, "members_all_field.csv")

#Plot fields for all members
fig12= pl.plot_field_members(field_all)
ut.print_plot(fig12, "plot_field_members_all.png")

#Get nation interwar members
field_int = pr.get_members_field(members_int,df_int)
ut.printdict_csv_printouts (field_int, "members_int_field.csv")

#Plot nations interwar members
fig13= pl.plot_field_members(field_int)
ut.print_plot(fig13, "plot_field_members_int.png")

#Get nation post-WWII members
field_post = pr.get_members_field(members_post,df_post)
ut.printdict_csv_printouts (field_post, "members_int_field.csv")

#Plot nations post-WWII members
fig14= pl.plot_field_members(field_post)
ut.print_plot(fig14, "plot_field_members_post.png")

#Get value counts fields all years
field_counts_all = pr.get_field_counts(field_all)
ut.print_csv_printouts (field_counts_all, "field_counts_all.csv")



