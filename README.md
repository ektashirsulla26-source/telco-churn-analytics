# Telecom Customer Churn Prediction

End-to-end Machine Learning project to predict telecom customer churn and identify high-risk customers.

## Project Objective

Customer churn is a major challenge for telecom companies.  
This project builds a predictive model to identify customers likely to churn and provides insights to support retention strategies.

## Dataset

- Telecom customer dataset
- 7000+ customer records with 33 variables
- Features include:
  - tenure
  - monthly charges
  - contract type
  - internet services
  - payment methods

## Project Workflow

Notebook 1 — EDA & Data Preparation
Name: 01_Telco_Churn_EDA_Feature_Engineering.ipynb
Sections:
1.Business Understanding
2.Data Overview
3.Data Cleaning
4.Handling Missing Values
5.Exploratory Data Analysis
6.Feature Engineering
7.Key Business Insights


Notebook 2 - Machine Learning Modelling
Name: 02_Telco_Churn_Modeling.ipynb
Sections
1.Import Clean Dataset
2.Train-Test Split
3.Feature Scaling
4.Model Training
5.Model Comparison
6.Hyperparameter Tuning
7.Model Evaluation
8.Feature Importance
9.Business Recommendation

## Models Used

- Logistic Regression
- Random Forest
- Gradient Boosting
- XGBoost

## Model Performance

Best Model: **Logistics Regression**

Key Metric:
- Churn Recall: **77%**

## Tech Stack

Python  
Pandas  
NumPy  
Scikit-learn  
XGBoost  
SMOTE
GridSearchCV
Streamlit  

## Project Structure
data/ # dataset
notebooks/ # EDA and experimentation
src/ # model training scripts
model/ # saved models

## Demo

Streamlit app for churn prediction.

## Business Impact

- Identifies customers with high churn probability
- Helps telecom companies target retention campaigns
- Supports data-driven decision making
