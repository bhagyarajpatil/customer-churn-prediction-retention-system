# customer-churn-prediction-retention-system
End-to-end Customer Churn Prediction &amp; Retention System using Python, Pandas, Scikit-learn, XGBoost, LightGBM, SHAP, and Streamlit. Predicts churn probability, classifies customer risk, explains key churn factors, and generates personalized retention recommendations.


An end-to-end **Machine Learning web application** that predicts whether a customer is likely to churn and provides insights that can help businesses take proactive **customer retention** actions.

The system uses customer demographic, service usage, contract, billing, and payment information to estimate churn probability.

---

## 🚀 Project Overview

Customer churn is a major challenge for subscription-based businesses such as telecom companies.

Instead of waiting until customers leave, this project uses Machine Learning to identify **high-risk customers in advance**.

The application allows users to enter customer information and receive:

* 🔮 Churn prediction
* 📈 Churn probability
* ⚠️ Customer risk level
* 👤 Customer profile information
* 💡 Retention recommendations

---

## 🎯 Objectives

* Predict whether a customer is likely to churn.
* Identify customers with a high probability of leaving.
* Analyze the factors associated with customer churn.
* Provide actionable retention recommendations.
* Deploy the ML model through an interactive Streamlit application.

---

## 🛠️ Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* XGBoost

### Web Application

* Streamlit

### Development Tools

* Jupyter Notebook
* PyCharm / VS Code
* Git & GitHub

---

## 📂 Dataset Features

The dataset contains customer information such as:

| Category       | Features                                         |
| -------------- | ------------------------------------------------ |
| 👤 Customer    | Gender, Senior Citizen, Partner, Dependents      |
| 📱 Services    | Phone Service, Multiple Lines                    |
| 🌐 Internet    | Internet Service, Online Security, Online Backup |
| 🛡️ Protection | Device Protection, Tech Support                  |
| 🎬 Streaming   | Streaming TV, Streaming Movies                   |
| 📄 Contract    | Contract, Paperless Billing                      |
| 💳 Payment     | Payment Method                                   |
| 💰 Billing     | Monthly Charges, Total Charges                   |
| ⏳ Tenure       | Tenure Months                                    |
| 🎯 Target      | Churn Value                                      |

---

## 🔄 Machine Learning Workflow

```text
Raw Customer Data
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Feature Engineering
        ↓
Categorical Encoding
        ↓
Feature Scaling
        ↓
Train-Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Selection
        ↓
Model Saving
        ↓
Streamlit Application
        ↓
Churn Prediction
        ↓
Retention Recommendation
```

---

## 🤖 Machine Learning Model

The project can evaluate multiple classification algorithms, including:

* Logistic Regression
* Random Forest
* Gradient Boosting
* XGBoost
* LightGBM 

The selected model is trained on historical customer data and used to predict the likelihood of churn for new customers.

### Prediction Output

The application provides:

```text
Churn Prediction: Yes / No

Churn Probability: XX%

Risk Level:
Low / Medium / High
```

---

## 📊 Customer Risk Classification

The predicted probability can be converted into a simple risk category:

| Churn Probability | Risk           |
| ----------------: | -------------- |
|             0–30% | 🟢 Low Risk    |
|            30–60% | 🟡 Medium Risk |
|           60–100% | 🔴 High Risk   |

This allows businesses to prioritize customers who need immediate attention.

---

## 💡 Retention Strategy

The system can provide retention suggestions based on customer characteristics.

### 🔴 High-Risk Customer

Possible actions:

* Offer personalized discounts.
* Provide a better plan or upgrade.
* Contact the customer proactively.
* Offer technical support.
* Provide loyalty benefits.

### 🟡 Medium-Risk Customer

Possible actions:

* Send personalized offers.
* Improve customer engagement.
* Recommend suitable service plans.
* Monitor future activity.

### 🟢 Low-Risk Customer

Possible actions:

* Maintain service quality.
* Offer loyalty rewards.
* Encourage long-term contracts.

---

## 🖥️ Streamlit Application

The Streamlit interface allows users to enter customer information such as:

```text
Gender
Senior Citizen
Partner
Dependents
Tenure Months
Phone Service
Multiple Lines
Internet Service
Online Security
Online Backup
Device Protection
Tech Support
Streaming TV
Streaming Movies
Contract
Paperless Billing
Payment Method
Monthly Charges
Total Charges
```

After submitting the information, the application displays the predicted churn result and risk level.



## 📦 Requirements


```text
pandas
numpy
scikit-learn
xgboost
streamlit
matplotlib
seaborn
```

---

## 📈 Model Evaluation

The classification model can be evaluated using:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC-AUC

For churn prediction, **Recall and F1-score are particularly important**, because missing a customer who is actually going to churn can result in lost revenue.

---

## 🔍 Key Business Value

This project demonstrates how Machine Learning can be converted into a practical business solution.

### Business Benefits

* Identify customers at risk of churn.
* Prioritize retention campaigns.
* Reduce customer acquisition costs.
* Improve customer lifetime value.
* Support data-driven decision making.
* Enable proactive customer engagement.

---

## 🌟 Future Improvements

* Add SHAP-based model explainability.
* Show the top factors influencing each prediction.
* Add customer segmentation.
* Build a retention recommendation engine.
* Add a dashboard for monitoring churn trends.
* Store prediction history in a database.
* Add authentication.
* Deploy the application to Streamlit Cloud.
* Add automated model retraining.

---

## 👨‍💻 Skills Demonstrated

This project demonstrates practical experience in:

* Python
* Data Cleaning
* Exploratory Data Analysis
* Feature Engineering
* Data Visualization
* Classification
* Model Evaluation
* Ensemble Learning
* XGBoost
* Model Serialization
* Streamlit
* Git & GitHub
* Machine Learning Deployment

---

## 📌 Project Purpose

This project was developed as a practical **Machine Learning and Data Scientist portfolio project** to demonstrate how customer data can be transformed into actionable business insights and predictive solutions.

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.
