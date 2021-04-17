# IncomeClassPrediction
This project aims to classify the Income Group of a Data Science Individual using classification algorithms. The Income is primarily divided into 3 classes i.e. Low, Medium and High.

# Live Demo
https://income-class-prediction.herokuapp.com/

# Dataset
Dataset https://www.kaggle.com/elroyggj/indeed-dataset-data-scientistanalystengineer?select=indeed_job_dataset.csv
Dataset consists of the following columns:
- Job_Title:		      Title of Role
- Link:			          Weblink of Job Posting
- Queried_Salary:		  Salary Range of the Job Posting (Estimated/Actual if available)
- Job_Type:		        3 Categories of Job Types - data_scientist, data_analyst, data_engineer
- Skill:			        List of desired skills on indeed site
- No of Skill:		    Count of the number of desired skills
- Company:		        Company that posted the job posting
- No of Reviews:		  Number of Reviews for the Company
- No of Stars:		    Ratings for the Company
- Date Since Posted:  Number of days since the job was posted - if less than a day, will be rounded up to a full day
- Description:		    Web scrape of part of the job description
- Location:		        State the job opening is located in
- Company_Revenue:	  Annual revenue of hiring company
- Company_Employees:	Employee count of hiring company
- Company_Industry:	  Industry of hiring company

# Expansion of Skill column (Top 10 overall skills):
- python
- sql
- machine learning
- r
- hadoop
- tableau
- sas
- spark
- java
- Others

The project makes use of classification algorithms to classify the salary of an Individual based on the Skill set and Job Position in an organization.

NOTE: The data cleaning code is not added as the main focus was the implementation of Classification Algorithms. However both the raw and clean datasets are uploaded. So anyone intending to use the project can manipulate and utilize the datasets as per their use.

# Machine Learning algorithms used for classification
1. Naive Bayes Classifier
2. Multinomial Regression
3. Decision Tree Classifier

# Technologies Used
1. R
2. Python
3. EXCEL (for Naive Bayes only)

# GUI (Optional)
GUI was designed using tkinter, python
