#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:18:45 2019

@author: giudittaparolini
"""

import pandas as pd
import os

#import data for all meetings
df1913 = pd.read_csv(os.path.join("..", "1_data", "1913_Rome.csv"))
df1919 = pd.read_csv(os.path.join("..", "1_data", "1919_Paris.csv"))
df1921 = pd.read_csv(os.path.join("..", "1_data", "1921_London.csv"))
df1923 = pd.read_csv(os.path.join("..", "1_data", "1923_Utrecht.csv"))
df1926 = pd.read_csv(os.path.join("..", "1_data", "1926_Zurich.csv"))
df1929 = pd.read_csv(os.path.join("..", "1_data", "1929_Copenhagen.csv"))
df1932 = pd.read_csv(os.path.join("..", "1_data", "1932_Munich.csv"))
df1935 = pd.read_csv(os.path.join("..", "1_data", "1935_Danzig.csv"))
df1937 = pd.read_csv(os.path.join("..", "1_data", "1937_Salzburg.csv"))
df1946 = pd.read_csv(os.path.join("..", "1_data", "1946_London.csv"))
df1947 = pd.read_csv(os.path.join("..", "1_data", "1947_Toronto.csv"))


#Transform the numerical data in a column from floats to integers 
def colval_to_int(df, column):
    df[column] = (
    df[column].fillna(0)
    .astype(int)
    .astype(object)
    .where(df[column].notnull())
    )
    return df

#generate data for all meetings
frames_all = [df1913, df1919, df1921, df1923, df1926, df1929, df1932, df1935, df1937, df1946, df1947]
df_keys = pd.concat(frames_all, keys=['1913', '1919', '1921', '1923', '1926', '1929', '1932', '1925', '1937', '1946', '1947'])
df_keys_dropcol = df_keys.drop(["Person title (if any)"], axis = 1)
df_keys_dropcol.Surname.str.strip()
df_keys_dropcol.Name.str.strip()
df_keys_dropcol['Field of study'].str.strip()
df_keys_born = colval_to_int(df_keys_dropcol, "Born")
df_keys_died = colval_to_int(df_keys_born, "Died")
df_keys_died.to_csv(os.path.join("..", "1_data", "df_clean_all.csv"))

#generate data for pre-WWI
df1913_dropcol = df1913.drop(["Person title (if any)"], axis = 1)
df1913_dropcol.Surname.str.strip()
df1913_dropcol.Name.str.strip()
df1913_dropcol['Field of study'].str.strip()
df1913_born = colval_to_int(df1913_dropcol, "Born")
df1913_died = colval_to_int(df1913_born, "Died")
df1913_died.to_csv(os.path.join("..", "1_data", "df_clean_pre.csv"))

#generate data for interwar meetings
frames_interwar = [df1919, df1921, df1923, df1926, df1929, df1932, df1935, df1937]
df_keys_int = pd.concat(frames_interwar, keys=['1919', '1921', '1923', '1926', '1929', '1932', '1925', '1937',])
df_keys_int_dropcol = df_keys_int.drop(["Person title (if any)"], axis = 1)
df_keys_int_dropcol.Surname.str.strip()
df_keys_int_dropcol.Name.str.strip()
df_keys_int_dropcol['Field of study'].str.strip()
df_keys_int_born = colval_to_int(df_keys_int_dropcol, "Born")
df_keys_int_died = colval_to_int(df_keys_int_born, "Died")
df_keys_int_died.to_csv(os.path.join("..", "1_data", "df_clean_int.csv"))

#generate data for post-WWII meetings
frames_post = [df1946, df1947]
df_keys_post = pd.concat(frames_post, keys=['1946', '1947'])
df_keys_post_dropcol = df_keys_post.drop(["Person title (if any)"], axis = 1)
df_keys_post_dropcol.Surname.str.strip()
df_keys_post_dropcol.Name.str.strip()
df_keys_post_dropcol['Field of study'].str.strip()
df_keys_post_born = colval_to_int(df_keys_post_dropcol, "Born")
df_keys_post_died = colval_to_int(df_keys_int_born, "Died")
df_keys_post_died.to_csv(os.path.join("..", "1_data", "df_clean_post.csv"))

