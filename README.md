# Data Science Salary Estimator: Project Overview 


* Created a tool that estmates data science salaries (MAE ~ $ 24K) to help data scientists negotitate their income when they get a job.
* Scraped over 1000 job descriptions from glassdoor using python and selenium
* Engineered features from the text of each job description to quantify the value companies put on skills such as, python, excel, aws, and spark.
* Optimized Linear, LASSO, and Random Forest Regressors using GridsearchCV to reach the best model.
* Built a client facing API using flask.

## Code and Resources Used
Python Version: 3.7.6    
Packages: pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle, require  
For Web Framework Requirements: pip install -r requirements.txt  
Scraper Guide: https://github.com/arapfaik/scraping-glassdoor-selenium  
Scraper Article: https://towardsdatascience.com/selenium-tutorial-scraping-glassdoor-com-in-10-minutes-3d0915c6d905  
Flask Productionization: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2  
Project Walk Through (Thank you Ken!): https://www.youtube.com/watch?v=MpF9HENQjDo&list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t


## Web Scraping
We modified the web scraper github repo (above) to scrape 1000 job openings from Glassdoor (https://www.glassdoor.com/index.htm).  From each job scraped, we got the following:
* Job title
* Salary Estimate
* Job Description
* Rating 
* Company
* Location
* Company Headquarters
* Company Size
* Company Founding Date
* Type of Ownership
* Industry
* Sector 
* Revenue 
* Revenue 

## Data Cleaning 
After scraping the data, I needed to clean it up so that it was usable for our model.  I made the following changes and created the following variables: 
* Parsed numeric data out of salary
* Made columns for employer provided salary and hourly wages
* Removed rows without salary 
* Parsed rating out of company text 
* Made a new column for company state
* Transformed founded date into age of company
* Made columns to indicate if different skills were listed in the job description: 
  * Python
  * R (RStudio)
  * Excel 
  * AWS
  * Spark
* Column for simplified job title and Seniority
* Column for the length of the job description 

## EDA

I examined the distributions of the data and the value counts for the various categorical variables.  Below are a few highlights.

![alt text](https://github.com/yiannimercer/ds_salary_estimator_proj/blob/main/ds_salalry_breakdown_job_simp.png) ![alt text](https://github.com/yiannimercer/ds_salary_estimator_proj/blob/main/ds_salary_corr_heatmap.png)

![alt text](https://github.com/yiannimercer/ds_salary_estimator_proj/blob/main/job_simp.png)

## Model Building

First, I transformed the categorical variables into dummy variables.  I also split the data into train and test sets with a test size of 20%.

I tried three different models and evaluated them using Mean Absolute Error.  I chose MAE because it is relatively easy to interpret and outliters aren't particularly bad for this type of analysis.  

The three models I developed: 
1) Multiple Linear Regression: Baseline for the model
2) LASSO Regresion: Due to the sparse data from the many categorical variables, I throught a normalized regression like LASSO would be effective. 
3) Random Forest: Again, with the sparsity associated with the date, I thought that this would be a good fit. 

## Model Performance

The LASSO Regression model far outperformed the Linear Regression.  However, the Random Forest model performed very similar. 
* Linear Regression: 9759815.54
* LASSO Regression: 24.48
* Random Forest: 26.39

## Productionaization

In this step, I built a flask API endpoint that was hosted on a local webserver by following along with Ken Jee and the TDS tutorial The API endpoint takes in a reqest with a list of values from a job listing and returns an estimated salary. 
