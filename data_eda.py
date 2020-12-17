#!/usr/bin/env python
# coding: utf-8

# ## Import Libraries

# In[ ]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np


# ## Read in Data

# In[189]:


df = pd.read_csv('salary_data_clean.csv')


# ## Initial Observations

# In[190]:


df.head()


# In[191]:


df.columns


# ## Data Feature Engineering & Minor Clean Up
# 
# * Job Titles & Seniority
# * Fix some states that are not abbreviated 
# * Removing additional space in front of all abbreviated states 
# * Hourly Wage to Annual
# * Remove new line from job title
# * Convert columns to integer where needed

# In[192]:


df['Job Title'].value_counts()


# In[193]:


def title_simplifier(title):
    if 'scientist' in title.lower():
        return 'data scientist'
    elif 'data engineer' in title.lower():
        return 'data engineer'
    elif 'analyst' in title.lower():
        return 'analyst'
    elif 'machine learning' in title.lower():
        return 'mle'
    elif 'manager' in title.lower():
        return 'manager'
    elif 'director' in title.lower():
        return 'director'
    else:
        return 'na'
    
def seniority(title):
    if 'sr' in title.lower() or 'senior' in title.lower() or 'sr' in title.lower() or 'lead' in title.lower() or 'principal' in title.lower():
        return 'senior'
    elif 'jr' in title.lower() or 'jr.' in title.lower() or 'junior' in title.lower():
        return 'jr'
    else:
        return 'na'
    


# In[194]:


df['job_simplified'] = df['Job Title'].apply(title_simplifier)


# In[195]:


df.job_simplified.value_counts()


# In[196]:


df['seniority'] = df['Job Title'].apply(seniority)


# In[197]:


df.seniority.value_counts()


# In[198]:


df.job_state.value_counts()


# In[199]:


# Fix states that were not abbreviated
df[df['job_state']=='Tennessee'] = ' TN'
df[df['job_state']=='California'] = ' CA'
df[df['job_state']=='Maryland'] = ' MD'
df[df['job_state']=='New Jersey'] = ' NJ'
df[df['job_state']=='Wyoming'] = ' WY'
df[df['job_state']=='Utah'] = ' UT'
df[df['job_state']=='North Carolina'] = ' NC'
df[df['job_state']=='Oregon'] = ' OR'


# In[200]:


df.job_state.value_counts()


# In[201]:


# Remove extra space for all abbreviated states
df['job_state'] = df.job_state.apply(lambda x: x.strip())
df.job_state.value_counts()


# In[202]:


# Job description length
df['desc_len'] = df['Job Description'].apply(lambda x: len(x))
df['desc_len']


# In[203]:


# Hourly wage to annual 
df['min_salary'] = df.apply(lambda x: x.min_salary * 2 if x.hourly == 1 else x.min_salary, axis = 1)


# In[204]:


df[df.hourly == 1][['hourly','min_salary','max_salary']]


# In[205]:


df['max_salary'] = df.apply(lambda x: x.max_salary * 2 if x.hourly == 1 else x.max_salary, axis = 1)


# In[206]:


df[df.hourly == 1][['hourly','min_salary','max_salary']]


# In[207]:


# Remove '\n' in company_txt
df['company_txt'] = df.company_txt.apply(lambda x: x.replace('\n',''))


# In[208]:


df['company_txt']


# ## EDA

# In[209]:


# Need to convert respective columns to integer
df.columns


# In[210]:


#Replacing illegitamite ratings with 0
df['Rating'].value_counts()
df[df['Rating'] == ' TN'] = 0.0
df[df['Rating'] == ' CA'] = 0.0
df[df['Rating'] == ' MD'] = 0.0
df[df['Rating'] == ' NJ'] = 0.0
df[df['Rating'] == ' UT'] = 0.0
df[df['Rating'] == ' WY'] = 0.0
df[df['Rating'] == ' OR'] = 0.0
df[df['Rating'] == ' NC'] = 0.0


# In[ ]:


# Remove rows with 0.0
df = df[df['job_state'] != 0.0]
df = df[df['job_simplified'] != 0.0]


# In[211]:


df['Rating'].value_counts()


# In[212]:


df['Rating'] = df['Rating'].astype(int)
df['Founded'] = df['Founded'].astype(int)
df['hourly'] = df['hourly'].astype(int)
df['employer_provided'] = df['employer_provided'].astype(int)
df['min_salary'] = df['min_salary'].astype(int)
df['max_salary'] = df['max_salary'].astype(int)
df['avg_salary'] = df['avg_salary'].astype(int)
df['age'] = df['age'].astype(int)
df['python_yn'] = df['python_yn'].astype(int)
df['R_yn'] = df['R_yn'].astype(int)
df['spark_yn'] = df['spark_yn'].astype(int)
df['aws_yn'] = df['aws_yn'].astype(int)
df['excel_yn'] = df['excel_yn'].astype(int)
df['desc_len'] = df['desc_len'].astype(int)


# In[213]:


df.describe()


# In[160]:


df.columns


# In[161]:


df.Rating.hist()


# In[162]:


df.avg_salary.hist()


# In[163]:


df.age.hist()


# In[164]:


df.desc_len.hist()


# In[166]:


df.boxplot(column = ['age','avg_salary','Rating'])


# In[167]:


df.boxplot(column = ['age','avg_salary'])


# In[168]:


df.boxplot(column = 'Rating')


# In[170]:


df[['age','avg_salary','Rating','desc_len']].corr()


# In[172]:


cmap = sns.diverging_palette(220, 10, as_cmap = True)
sns.heatmap(df[['age','avg_salary','Rating','desc_len']].corr(), vmax =.3, center = 0, cmap = cmap,
           square = True, linewidths = .5, cbar_kws = {"shrink":.5})


# In[173]:


df.columns


# In[175]:


df_cat = df[['Location', 'Headquarters', 'Size', 'Founded','Type of ownership', 'Industry', 'Sector', 'Revenue','company_txt','job_state',
   'python_yn', 'R_yn', 'spark_yn','aws_yn', 'excel_yn', 'job_simplified', 'seniority']]


# In[214]:


for i in df_cat.columns:
    cat_num = df_cat[i].value_counts()
    print("graph for %s: total = %d" %(i,len(cat_num)))
    chart = sns.barplot(x =  cat_num.index, y = cat_num)
    chart.set_xticklabels(chart.get_xticklabels(),rotation = 90)
    plt.show()


# In[184]:


for i in df_cat[['Location','company_txt']].columns:
    cat_num = df_cat[i].value_counts()[:20]
    print("graph for %s: total = %d" %(i,len(cat_num)))
    chart = sns.barplot(x =  cat_num.index, y = cat_num)
    chart.set_xticklabels(chart.get_xticklabels(),rotation = 90)
    plt.show()


# In[185]:


df.columns


# In[221]:


pd.pivot_table(df, index = ['job_state','job_simplified'], values = 'avg_salary')


# In[216]:


df.job_simplified.value_counts()


# In[228]:


pd.pivot_table(df, index = ['job_state','job_simplified'], values = 'avg_salary').sort_values('job_state',ascending = False)


# In[229]:


pd.pivot_table(df,index = ['job_simplified','seniority'], values = 'avg_salary')


# In[237]:


pd.set_option('display.max_rows',None)
pd.pivot_table(df,index = ['job_state','job_simplified'], values = 'avg_salary', aggfunc = 'count').sort_values('job_state', ascending = False)


# In[241]:


pd.pivot_table(df[df.job_simplified == 'data scientist'],index = 'job_state', values = 'avg_salary').sort_values('avg_salary', ascending = False)


# In[242]:


df.columns


# In[243]:


# rating,industry, sector, revenue, hourly, python, r, spark, aws, excel, desc_len, Type of ownership 


# In[248]:


df_pivots = df[['Rating','Industry','Sector','Revenue','hourly','python_yn', 'R_yn', 'spark_yn',
       'aws_yn', 'excel_yn','desc_len','Type of ownership','avg_salary']]


# In[252]:


for i in df_pivots.columns:
    print(i)
    print(pd.pivot_table(df_pivots, index = i,values = 'avg_salary').sort_values('avg_salary',ascending = False))


# In[254]:


pd.pivot_table(df_pivots, index = 'Revenue', columns = 'python_yn',values = 'avg_salary',aggfunc = 'count')


# In[265]:


import nltk
nltk.download('stopwords')
nltk.download('punkt')
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# In[266]:


words = " ".join(df['Job Description'])

def punctuation_stop(text):
    """remove punctuation and stop words"""
    filtered = []
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    for w in word_tokens:
        if w not in stop_words and w.isalpha():
            filtered.append(w.lower())
    return filtered


words_filtered = punctuation_stop(words)

text = " ".join([ele for ele in words_filtered])

wc= WordCloud(background_color="white", random_state=1,stopwords=STOPWORDS, max_words = 2000, width =800, height = 1500)
wc.generate(text)

plt.figure(figsize=[10,10])
plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.show()


# In[ ]:




