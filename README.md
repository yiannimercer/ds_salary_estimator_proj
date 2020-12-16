# Data Science Salary Estimator: Project Overview 
### This project was completed by following Ken Jee's Data Science Project From Scratch Series on Youtube. (Series linked below)

* Created a tool that estmates data science salaries (MAE ~ 24K) to help data scientists negotitate their income when they get a job.
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

## YouTube Project Walk-Through (This project is an exact replica and was completed for learning purposes)
https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t

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
