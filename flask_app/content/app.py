import streamlit as st
import pickle
import numpy as np

# Load Models
def load_model(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

# Crop details with yield information
crop_details = {
    "rice": {"type": "High yield", "amount": "6-8 tons per hectare"},
    "wheat": {"type": "Moderate yield", "amount": "4-6 tons per hectare"},
    "maize": {"type": "High yield", "amount": "8-10 tons per hectare"},
    "millet": {"type": "Low yield", "amount": "2-3 tons per hectare"},
    "cotton": {"type": "Fiber crop", "amount": "2-3 bales per hectare"},
    "sugarcane": {"type": "High sugar yield", "amount": "70-100 tons per hectare"},
    "barley": {"type": "Moderate yield", "amount": "3-4 tons per hectare"},
    "oilseeds": {"type": "Oil crop", "amount": "1.5-2 tons per hectare"}
}

# Custom CSS
st.markdown("""
    <style>
    body {
        background-image: url('https://via.placeholder.com/1920x1080?text=Agriculture+Background');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .crop-output {
        background-color: #e0f7fa;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #26a69a;
        font-size: 18px;
        margin-top: 20px;
    }
    .team-section {
        color: #00796b;
        font-weight: bold;
        margin-top: 10px;
    }
    .main-header {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 10px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# UI Components
st.markdown("""
<div class='main-header'>
    <h1>🌾 Crop Recommendation System</h1>
</div>
""", unsafe_allow_html=True)

# Team Members
st.markdown("""
<div class='team-section'>
**Team Members:**<br>
RA2211003011436 - Yetukuri Gargeya Sreenadh<br>
RA2211003011437 - Kodumuru Ashish<br>
RA2211003011440 - Pabolu Hari Venkata Mani Sai Vineeth<br>
RA2211003011422 - Mohd Tahir Majid
</div>
""", unsafe_allow_html=True)

st.write("Enter the following details to get a crop recommendation:")

# Sidebar for Model Selection
st.sidebar.title("Model Selection")
model_option = st.sidebar.selectbox(
    "Choose a model for prediction:",
    ("Random Forest", "XGBoost", "LightGBM", "SVM", "KNN",  "MLP")
)

# Input Fields
N = st.number_input('Nitrogen', min_value=0)
P = st.number_input('Phosphorus', min_value=0)
K = st.number_input('Potassium', min_value=0)
temperature = st.number_input('Temperature', min_value=0.0)
humidity = st.number_input('Humidity', min_value=0.0)
ph = st.number_input('pH', min_value=0.0)
rainfall = st.number_input('Rainfall', min_value=0.0)

model_files = {
    "Random Forest": "random_forest.pkl",
    "XGBoost": "xgboost.pkl",
    "LightGBM": "lightgbm.pkl",
    "SVM": "svm.pkl",
    "KNN": "knn.pkl",
    "MLP": "mlp.pkl"
}

# Predict Button
if st.button("Predict Crop"):
    model = load_model(model_files[model_option])
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(input_data)
    crop = prediction[0]
    details = crop_details.get(crop, {"type": "Unknown", "amount": "Data not available"})
    
    st.markdown(f"""
        <div class='crop-output'>
            <strong>Recommended Crop:</strong> {crop}<br>
            <strong>Type of Yield:</strong> {details['type']}<br>
            <strong>Expected Yield:</strong> {details['amount']}
        </div>
    """, unsafe_allow_html=True)
