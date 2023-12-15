import streamlit as st
import pandas as pd

# Load your trained model
# Replace 'your_model.pkl' with the actual path to your saved model file
model = RandomForestClassifier()  # Replace with your actual model class
# model.load_model('your_model.pkl')

# Function to make predictions
def make_prediction(user_input):
    # Preprocess user input if needed
    # Make predictions using the loaded model
    prediction = model.predict(user_input)
    return prediction

# Streamlit App
def main():
    st.title('Financial Inclusion Prediction App')

    # User Input Form
    st.sidebar.header('User Input for Prediction')

    # Example input components (replace with your actual features)
    country = st.sidebar.selectbox('Country', ['Kenya', 'Rwanda', 'Tanzania', 'Uganda'])
    year = st.sidebar.number_input('Year', min_value=2016, max_value=2023, value=2018)
    location_type = st.sidebar.radio('Location Type', ['Rural', 'Urban'])
    cellphone_access = st.sidebar.radio('Cellphone Access', ['Yes', 'No'])
    household_size = st.sidebar.number_input('Household Size', min_value=1, value=3)
    age_of_respondent = st.sidebar.number_input('Age of Respondent', min_value=18, max_value=100, value=25)
    gender_of_respondent = st.sidebar.radio('Gender of Respondent', ['Male', 'Female'])
    relationship_with_head = st.sidebar.selectbox('Relationship with Head', ['Spouse', 'Child', 'Other relative'])
    marital_status = st.sidebar.selectbox('Marital Status', ['Married/Living together', 'Single/Never Married'])
    education_level = st.sidebar.selectbox('Education Level', ['Primary education', 'Secondary education', 'Higher education'])
    job_type = st.sidebar.selectbox('Job Type', ['Self employed', 'Formally employed', 'Informally employed'])


    # Create a dictionary to hold user input
    user_input = {
        'country': country,
        'year': year,
        'location_type': location_type,
        'cellphone_access': cellphone_access,
        'household_size': household_size,
        'age_of_respondent': age_of_respondent,
        'gender_of_respondent': gender_of_respondent,
        'relationship_with_head': relationship_with_head,
        'marital_status': marital_status,
        'education_level': education_level,
        'job_type': job_type,
    }

    # Make prediction when the user clicks the button
    if st.sidebar.button('Predict'):
        # prediction = make_prediction(pd.DataFrame([user_input]))  # Convert user_input to a DataFrame
        st.sidebar.write('Prediction:', 'Coming Soon! 😎😎🔥')

if __name__ == "__main__":
    main()
