import streamlit as st
import numpy as np
import joblib
import json

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Bangalore House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# ---------------------------------------------------
# Load Model
# ---------------------------------------------------

model = joblib.load("C:\\Users\\DELL\\OneDrive\\Desktop\\House Price Prediction\\models\\model.pkl")

with open("C:\\Users\\DELL\\OneDrive\\Desktop\\House Price Prediction\\app\columns.json", "r") as f:
    data_columns = json.load(f)["data_columns"]

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------

st.markdown(
    """
    <style>

    .main {
        padding-top: 1rem;
    }

    .stButton>button {
        width: 100%;
        height: 50px;
        font-size: 18px;
        border-radius: 10px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("🏠 Project Details")

st.sidebar.markdown("""
### Bangalore House Price Prediction

This project predicts Bangalore house prices using Machine Learning models.

### Dataset Features
- Area Type
- Location
- Total Sqft
- BHK
- Bathrooms
- Balcony
- Price

### ML Algorithms Used
- Linear Regression
- Decision Tree
- Random Forest

### Best Model
✅ Random Forest Regressor

### Concepts Used
- Data Cleaning
- Feature Engineering
- Outlier Removal
- One Hot Encoding
- Model Training
- Model Evaluation
- Streamlit Deployment
""")

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("🏠 Bangalore House Price Prediction")

st.markdown(
    "Predict estimated house price based on property details."
)

# ---------------------------------------------------
# Input Layout
# ---------------------------------------------------

col1, col2 = st.columns(2)

# ---------------------------------------------------
# Area Type
# ---------------------------------------------------

with col1:

    area_type = st.selectbox(
        "Area Type",
        [
            "Select Area Type",
            "Super built-up Area",
            "Built-up Area",
            "Plot Area",
            "Carpet Area"
        ]
    )

# ---------------------------------------------------
# Location
# ---------------------------------------------------

with col2:

    location = st.selectbox(
        "Location",
        [
            "Select Location",
            "Whitefield",
            "Electronic City",
            "Sarjapur Road",
            "Marathahalli",
            "Bellandur",
            "HSR Layout",
            "JP Nagar",
            "Hebbal",
            "Yelahanka",
            "Thanisandra",
            "Koramangala",
            "Indira Nagar",
            "Jayanagar",
            "Banashankari",
            "Rajaji Nagar",
            "BTM Layout",
            "Malleshwaram",
            "Hennur",
            "Kengeri",
            "other"
        ]
    )

# ---------------------------------------------------
# Numerical Inputs
# ---------------------------------------------------

col3, col4 = st.columns(2)

with col3:

    sqft = st.number_input(
        "Total Sqft",
        min_value=0.0,
        value=0.0
    )

with col4:

    bhk = st.number_input(
        "BHK",
        min_value=0,
        value=0
    )

# ---------------------------------------------------

col5, col6 = st.columns(2)

with col5:

    bath = st.number_input(
        "Bathrooms",
        min_value=0,
        value=0
    )

with col6:

    balcony = st.number_input(
        "Balconies",
        min_value=0,
        value=0
    )

# ---------------------------------------------------
# Predict Button
# ---------------------------------------------------

predict_button = st.button("Predict House Price")

# ---------------------------------------------------
# Prediction
# ---------------------------------------------------

if predict_button:

    # Validation

    if area_type == "Select Area Type":

        st.warning("Please select Area Type")

    elif location == "Select Location":

        st.warning("Please select Location")

    elif sqft <= 0:

        st.warning("Please enter Total Sqft")

    elif bhk <= 0:

        st.warning("Please enter BHK")

    else:

        x = np.zeros(len(data_columns))

        # Numerical Features

        x[0] = sqft
        x[1] = bath
        x[2] = balcony
        x[3] = bhk

        # Location Encoding

        location_column = "location_" + location.lower()

        if location_column in data_columns:

            loc_index = data_columns.index(location_column)

            x[loc_index] = 1

        # Area Type Encoding

        area_column = "area_type_" + area_type.lower()

        if area_column in data_columns:

            area_index = data_columns.index(area_column)

            x[area_index] = 1

        # Prediction

        prediction = model.predict([x])[0]

        # Result

        st.success(
            f"Estimated House Price : ₹ {round(prediction,2)} Lakhs"
        )

        st.balloons()