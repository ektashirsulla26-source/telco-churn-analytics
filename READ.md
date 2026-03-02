# 📊 Telco Customer Churn Prediction

## 📌 Business Problem

Customer churn is a major challenge in the telecom industry. Acquiring new customers costs significantly more than retaining existing ones.

This project aims to analyze customer behavior and build a machine learning model to predict customers who are likely to churn. The objective is to help the business proactively retain high-risk customers and reduce revenue loss.

---

## 🎯 Project Objectives

- Perform exploratory data analysis (EDA) to understand churn behavior
- Identify key drivers influencing customer churn
- Build and compare multiple machine learning models
- Evaluate model performance using appropriate metrics
- Provide actionable business insights for retention strategy

---

## 📂 Project Structure

## 📂 Project Structure

```
telco-customer-churn/
│
├── data/                  # Raw and processed datasets
│   ├── raw/               # Original dataset
│   └── processed/         # Cleaned & transformed data
│
├── notebooks/             # Jupyter notebooks
│   ├── 01_EDA_and_Feature_Engineering.ipynb
│   └── 02_Model_and_Evaluation.ipynb
│
├── src/                   # Reusable utility functions
│   └── utils.py
│
├── README.md              # Project documentation
└── requirements.txt       # Project dependencies
```
---

## 🛠 Tools & Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- Jupyter Notebook

---

## 🔎 Exploratory Data Analysis (EDA)

The following analysis was performed:

- Target Distribution (Churn Imbalance %)
- Tenure analysis
- Contract type impact on churn
- Monthly charges analysis
- Payment method impact
- Internet Service impact
- Correlation heatmap

### 📊 Key EDA Insights

Key Insights from EDA
1. Dataset shows class imbalance (26.6 % churn).
2. Customers with month-to-month contracts have highest churn rate.
3. Short-tenure customers churn significantly more.
4. Customers with higher monthly charges show increased churn probability.
5. Certain payment methods (e.g., electronic check) show higher churn rates.
“Before modeling, I performed detailed EDA to understand churn behavior across tenure, contract type, service usage, and financial attributes. I identified strong behavioral signals such as short tenure and month-to-month contracts being major churn drivers.”

---

## ⚙ Feature Engineering & Preprocessing

- Tenure Groups (Behavioral Segmentation)
- Handling missing values
- Encoding categorical variables
- Feature scaling
- Stratified train-test split
- Data preparation for modeling

---

## 🤖 Model Building & Evaluation

Multiple classification models were trained:

- Logistic Regression
- Random Forest
- XGBoost

### 📈 Evaluation Metrics Used

- Accuracy
- Precision
- Recall
- F1-Score
- ROC-AUC Score
- Confusion Matrix
- Cross-Validation

### 📊 Model Performance (Example)

| Model                | ROC-AUC Score |
|----------------------|---------------|
| Logistic Regression  | 0.842         |
| Random Forest        | 0.820         |
| XGBoost              | 0.826         |


---

## 💰 Business Impact

The model enables identification of high-risk customers, allowing:

- Targeted retention campaigns
- Contract upgrade offers
- Personalized pricing strategies
- Early engagement for new customers

By proactively retaining high-risk customers, telecom companies can significantly reduce revenue loss.

---

## 📌 Key Business Insights

1. Month-to-month contract customers require focused retention strategy.
2. Customers in early tenure phase need proactive engagement.
3. High monthly charge customers benefit from personalized offers.
4. Contract-based customers (1–2 years) show lower churn probability.
5. Predictive modeling can support revenue-driven decision making.

---

## 🚀 How to Run This Project

1. Clone the repository:
git clone <your-repository-link>

2. Install dependencies:
pip install -r requirements.txt

3. Run notebooks in order:
- 01. EDA_and_Feature_Engineering.ipynb
- 02. Model_and_Evaluation.ipynb

---

## 📈 Future Improvements

- Hyperparameter tuning
- SHAP for model interpretability
- Model deployment using Streamlit
- API-based churn prediction service

---

## 👩‍💻 Author

Ekta Shirsulla  
Aspiring Data Scientist | Machine Learning Enthusiast


