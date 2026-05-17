# 🏠 Bangalore House Price Prediction

A Machine Learning based web application that predicts Bangalore house prices based on user inputs such as location, area type, square feet, BHK, bathrooms, and balconies.

The project performs complete Data Science workflow including data cleaning, preprocessing, Exploratory Data Analysis (EDA), feature engineering, model training, evaluation, and Streamlit deployment.

---

<video controls src="House Price Prediction-1.mp4" title="Title"></video>

# Project Objective

The main goal of this project is to help users estimate the approximate budget or price of a house in Bangalore using Machine Learning algorithms.

Users can provide:
- Location
- Area Type
- Total Square Feet
- BHK Count
- Bathrooms
- Balcony Count

Based on these inputs, the trained ML model predicts the estimated house price.

---

# Dataset Information

Dataset used:
- Bengaluru House Price Dataset

Total Features:
1. area_type
2. availability
3. location
4. size
5. society
6. total_sqft
7. bath
8. balcony
9. price

Target Column:
- `price`

---

# Technologies Used

## Programming Language
- Python

## Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Streamlit

---

# Exploratory Data Analysis (EDA)

EDA was performed to understand the dataset and identify:
- Missing values
- Outliers
- Data distribution
- Correlation between features
- Top locations
- BHK distribution
- Price distribution

Visualizations Used:
- Histogram
- Bar Chart
- Scatter Plot
- Correlation Heatmap

---

# Data Preprocessing

The following preprocessing steps were performed:

## 1. Missing Value Handling
- Removed null values
- Dropped unnecessary columns

## 2. Feature Engineering
- Extracted BHK count from size column
- Converted total_sqft into numerical format

## 3. Location Cleaning
- Removed extra spaces
- Grouped rare locations into `other`

## 4. Outlier Removal
- Removed unrealistic sqft values
- Removed price per sqft outliers
- Removed BHK outliers
- Removed bathroom anomalies

## 5. Encoding
- Applied One Hot Encoding on:
  - location
  - area_type

---

# Machine Learning Models Used

Three regression models were trained and compared.

## 1. Linear Regression
Used as a baseline model for price prediction.

## 2. Decision Tree Regressor
Used for non-linear relationship learning.

## 3. Random Forest Regressor
Used for better accuracy and robust prediction.

---

# Model Evaluation

Evaluation Metrics Used:
- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

The best performing model:
✅ Random Forest Regressor

Approximate Accuracy:
- R² Score: 0.92 – 0.96

---

# Model Saving

The trained model was saved using:
- `model.pkl`

Feature columns were saved using:
- `columns.json`

These files are later used in Streamlit deployment.

---

# Streamlit Web Application

A professional Streamlit UI was created where users can:
- Select location from dropdown
- Select area type
- Enter total sqft
- Enter BHK
- Enter bathrooms
- Enter balconies

The application predicts the estimated house price instantly.

---

# Sample Inputs

| Feature | Example |
|---|---|
| Location | Whitefield |
| Area Type | Super built-up Area |
| Sqft | 1300 |
| BHK | 3 |
| Bathrooms | 2 |
| Balcony | 1 |

---

# Sample Output

```bash
Estimated House Price : ₹ 118.45 Lakhs
```

# Concepts Covered

- Data Science
- Machine Learning
- Regression Models
- Data Cleaning
- Feature Engineering
- Outlier Detection
- Model Evaluation
- Web App Deployment
- Streamlit UI

---

# Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow for real-world house price prediction. It combines Data Analysis, ML model building, and Streamlit deployment into a fully functional predictive web application.

The application helps users estimate house prices in Bangalore based on important property features with good prediction accuracy.

---