#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 21:01:01 2020

@author: yiannimercer
"""


import glassdoor_scraper as gs
import pandas as pd 
path = "/Users/yiannimercer/Downloads/chromedriver-2"

df = gs.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_jobs.csv',index = False)

