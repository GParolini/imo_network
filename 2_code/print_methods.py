#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:02:39 2019

@author: giudittaparolini
"""

import data_methods as dm

#Get the surnames of the members using the surname 
def get_members(df):
    surnames = df["Surname"].tolist()
    surnames_strip = [x.strip(' ') for x in surnames]
    surnames_unique = list(set(surnames_strip))
    surnames_unique_sorted = sorted(surnames_unique)
    return surnames_unique_sorted


def get_members_counts(df):
    counts = df['Surname'].value_counts()
    return counts

def get_members_age(members,df):
    birth_year = []
    
    for member in members:
        member_year = []
        df_integ = dm.colval_to_int(df, "Born")
        df_filt = df_integ[df_integ['Surname'] == member]
        member_birth_year = df_filt.at[df_filt.index[0],'Born']
        member_year = [member, member_birth_year]
        
    
        birth_year.append(member_year)
    
    age_dict = { k[0]: k[1:] for k in birth_year }
    
    return(age_dict)

def get_members_nation(members,df):
    nation = []
    
    for member in members:
        member_nation = []
        df_filt = df[df['Surname'] == member]
        member_nation = df_filt.at[df_filt.index[0],'Nation (Affiliation) History']
        member_nation = [member, member_nation]
        
    
        nation.append(member_nation)
    
    nation_dict = { k[0]: k[1:] for k in nation }
    
    return(nation_dict)

def get_members_city(members,df):
    city = []
    
    for member in members:
        member_city = []
        df_filt = df[df['Surname'] == member]
        member_city = df_filt.at[df_filt.index[0],'City (Affiliation) History']
        member_city = [member, member_city]
        
    
        city.append(member_city)
    
    city_dict = { k[0]: k[1:] for k in city }
    
    return(city_dict)

def get_members_field(members,df):
    field = []
    
    for member in members:
        member_field = []
        df_filt = df[df['Surname'] == member]
        member_field = df_filt.at[df_filt.index[0],'Field of study']
        member_field = [member, member_field]
        
    
        field.append(member_field)
    
    field_dict = { k[0]: k[1:] for k in field }
    
    return(field_dict)

def get_field_counts(my_dict):
    my_list = list(my_dict.values())
    count_agr = my_list.count("Agriculture")
    return count_agr
    
    
    
    