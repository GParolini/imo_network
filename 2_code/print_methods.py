#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 15:02:39 2019

@author: giudittaparolini
"""


def get_members(df):
    surnames = df["Surname"].tolist()
    surnames_unique = list(set(surnames))
    surnames_unique_sorted = sorted(surnames_unique)
    return surnames_unique_sorted


def get_members_counts(df):
    counts = df['Surname'].value_counts()
    return counts
        