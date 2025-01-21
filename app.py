import streamlit as st
import pickle
import numpy as np

def load_model(model_path):
    """Load the trained model from pickle file"""
    try:
        with open(model_path, 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None

def predict_heart_disease(model, features):
    """Make prediction using the loaded model"""
    feature_order = [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
        'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal'
    ]
    feature_array = np.array([features[feature] for feature in feature_order]).reshape(1, -1)
    prediction = model.predict(feature_array)[0]
    # probability = model.predict_proba(feature_array)[0][1]
    # return prediction, probability
    return prediction
# Set page config
st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

# Main title
st.title("Heart Disease Prediction using Machine Learning")
st.write("Enter the patient's information to predict heart disease risk")

# Load model
model = load_model("models/model.pkl")

if model is not None:
    # Create two columns for input fields
    col1, col2 = st.columns(2)

    with col1:
        # Left column inputs
        age = st.number_input("Age", min_value=0, max_value=120, value=45)
        
        sex = st.number_input("Sex (0: Female, 1: Male)", 
                            min_value=0, max_value=1, value=0)
        
        cp = st.number_input("Chest Pain Type", 
                            min_value=0, max_value=300, value=0)
        
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 
                                  min_value=0, max_value=300, value=120)
        
        chol = st.number_input("Cholesterol (mg/dl)", 
                              min_value=0, max_value=600, value=200)
        
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl (0: No, 1: Yes)", 
                             min_value=0, max_value=1, value=0)

    with col2:
        # Right column inputs
        restecg = st.number_input("Resting ECG Results", 
                                 min_value=0, max_value=2, value=0)
        
        thalach = st.number_input("Maximum Heart Rate", 
                                 min_value=0, max_value=300, value=150)
        
        exang = st.number_input("Exercise Induced Angina (0: No, 1: Yes)", 
                               min_value=0, max_value=1, value=0)
        
        oldpeak = st.number_input("ST Depression Induced by Exercise", 
                                 min_value=0.0, max_value=10.0, value=0.0, step=0.1)
        
        slope = st.number_input("Slope of Peak Exercise ST Segment", 
                               min_value=0, max_value=5, value=0)
        
        ca = st.number_input("Number of Major Vessels", 
                            min_value=0, max_value=4, value=0)
        
        thal = st.number_input("Thalassemia", 
                              min_value=0, max_value=3, value=0)

    # Create a dictionary of all features
    features = {
        'age': age,
        'sex': sex,
        'cp': cp,
        'trestbps': trestbps,
        'chol': chol,
        'fbs': fbs,
        'restecg': restecg,
        'thalach': thalach,
        'exang': exang,
        'oldpeak': oldpeak,
        'slope': slope,
        'ca': ca,
        'thal': thal
    }

    # Add a predict button
    if st.button("Predict", type="primary"):
        # prediction, probability = predict_heart_disease(model, features)
        prediction = predict_heart_disease(model, features)
        
        # Display prediction
        st.write("---")
        st.header("Prediction Results")
        
        # Create columns for results
        result_col1, result_col2 = st.columns(2)
        
        with result_col1:
            st.metric(
                label="Prediction",
                value="Heart Disease Detected" if prediction == 1 else "No Heart Disease Detected"
            )
            
        # with result_col2:
        #     st.metric(
        #         label="Probability",
        #         value=f"{probability:.1%}"
        #     )
            
        # Add risk level indicator
        # risk_level = "High" if probability > 0.9 else "Medium" if probability > 0.5 else "Low"
        # st.write(f"Risk Level: **{risk_level}**")
        
    # Add sample data section
    st.write("---")
    st.header("Sample Data Entry")
    st.write("You can copy these sample values to test the model:")
    
    sample_data = """
    Example entries from dataset:
    1. age=60, sex=1, cp=0, trestbps=140, chol=293, fbs=0, restecg=0, thalach=170, exang=0, oldpeak=1.2, slope=1, ca=2, thal=3
    2. age=69, sex=1, cp=3, trestbps=160, chol=234, fbs=1, restecg=0, thalach=131, exang=0, oldpeak=0.1, slope=1, ca=1, thal=2
    3. age=52, sex=1, cp=0, trestbps=125, chol=200, fbs=0, restecg=1, thalach=160, exang=0, oldpeak=1.0, slope=1, ca=1, thal=3
    """
    st.code(sample_data)

else:
    st.error("Failed to load the model. Please check if the model file exists at 'models/model.pkl'")