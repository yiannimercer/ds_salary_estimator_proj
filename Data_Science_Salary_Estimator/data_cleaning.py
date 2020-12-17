#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 23:52:21 2020

@author: yiannimercer
"""


import pandas as pd 

df = pd.read_csv('glassdoor_jobs.csv')

# salary parsing
# Company Name text only 
# state field
# age of company 
# parsing of jobs description (python, etc.)

##### SALARY PARSING ####

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower() else 0)
df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower() else 0)


#Removing the rows with no salary estimate
df = df[df['Salary Estimate'] != '-1']



#Clearning Salary Estimate Column for the text and the '$' and 'K'
salary = df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_Kd = salary.apply(lambda x: x.replace('K','').replace('$',''))

min_hr = minus_Kd.apply(lambda x: x.lower().replace('per hour','')).replace('employer provided salary:','')

df['min_salary'] = min_hr.apply(lambda x: x.split('-')[0])
df['max_salary'] = min_hr.apply(lambda x: x.split('-')[1])
df['min_salary'] = df['min_salary'].astype(int)
df['max_salary'] = df['max_salary'].astype(int)

df['avg_salary'] = (df.max_salary + df.min_salary)/2

##### COMPANY NAME TEXT ONLY #####

df['company_txt'] = df.apply(lambda x: x['Company Name'] if x['Rating'] < 0 else x['Company Name'][:-3], axis = 1)

##### STATE FIELD ####
df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1] if len(x.split(','))== 2 else x.split(',')[0])

df.job_state.value_counts()

##### AGE OF COMPANY #####

df['age'] = df.Founded.apply(lambda x: x if x < 1 else 2020 - x)


##### PARSING JOB DESCRIPTIONS #####

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
df.python_yn.value_counts()
#r studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() else 0)
df.R_yn.value_counts()
#spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark_yn.value_counts()
#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_yn.value_counts()
#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel_yn.value_counts()

df.to_csv('salary_data_clean.csv', index = False)


