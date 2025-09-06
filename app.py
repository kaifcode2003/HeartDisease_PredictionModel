import streamlit as st
import pandas as pd
import joblib

# Load saved model, scaler, and expected columns
model = joblib.load("Logistic_Regression.pkl")
scaler = joblib.load("heart_scaler.pkl")
expected_columns = joblib.load("heart_columns.pkl")

# Page config
st.set_page_config(page_title="❤️ Heart Stroke Predictor", layout="wide")

# Title & description
st.title("❤️ Heart Stroke Prediction App")
st.markdown(
    """
    Welcome to the **Heart Stroke Risk Predictor**.  
    Choose demo data or enter your own details in the sidebar.  
    """
)

# Credit line
st.markdown(
    "<p style='text-align:right; font-size:16px; color:gray;'>🛠️ Developed by <b>Mohd Kaif</b></p>",
    unsafe_allow_html=True
)

# Sidebar input sections
st.sidebar.header("📝 Input Your Details")

# --- Demographics ---
st.sidebar.subheader("👤 Demographics")
age = st.sidebar.slider("Age", 18, 100, 40)
sex = st.sidebar.radio("Sex", ["M", "F"])

# --- Medical History ---
st.sidebar.subheader("🫀 Medical Info")
chest_pain = st.sidebar.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
fasting_bs = st.sidebar.radio("Fasting Blood Sugar > 120 mg/dL", [0, 1])
exercise_angina = st.sidebar.radio("Exercise-Induced Angina", ["Y", "N"])

# --- Test Results ---
st.sidebar.subheader("📊 Test Results")
resting_bp = st.sidebar.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)
cholesterol = st.sidebar.number_input("Cholesterol (mg/dL)", 100, 600, 200)
resting_ecg = st.sidebar.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
max_hr = st.sidebar.slider("Max Heart Rate", 60, 220, 150)
oldpeak = st.sidebar.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)
st_slope = st.sidebar.selectbox("ST Slope", ["Up", "Flat", "Down"])

# Predict button
if st.sidebar.button("🔍 Predict Risk"):

    # Create a raw input dictionary
    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    # Create input dataframe
    input_df = pd.DataFrame([raw_input])

    # Fill in missing columns with 0s
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[expected_columns]

    # Scale the input
    scaled_input = scaler.transform(input_df)

    # Make prediction
    prediction = model.predict(scaled_input)[0]

    # Show result
    st.subheader("📌 Prediction Result")
    if prediction == 1:
        st.markdown(
            """
            <div style='background-color:#ffe6e6; padding:15px; border-radius:10px;'>
                <h3 style='color:red;'>⚠️ High Risk of Heart Disease</h3>
                <p style='color:#660000; font-size:16px; font-weight:bold;'>
                    Please consult a cardiologist for further guidance.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div style='background-color:#e6ffe6; padding:15px; border-radius:10px;'>
                <h3 style='color:green;'>✅ Low Risk of Heart Disease</h3>
                <p style='color:#004d00; font-size:16px; font-weight:bold;'>
                    Keep maintaining a healthy lifestyle!
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

# Footer credit
st.markdown(
    "<hr><p style='text-align:center; color:gray;'>© 2025 | Developed by <b>Mohd Kaif</b></p>",
    unsafe_allow_html=True
)
