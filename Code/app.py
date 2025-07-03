import streamlit as st
import numpy as np
import joblib  # Using joblib for loading the saved model

# incuding model file from directory
model_path = r"..\Models\best_modelsV2.joblib"

# Initialize model components
best_models, scaler, skill_encoder, profile_encoder = None, None, None, None

# Try to load the model and handle errors
try:
    best_models, scaler, skill_encoder, profile_encoder = joblib.load(model_path)
except FileNotFoundError:
    st.error("Error: Model V2 file not found!")
    st.stop()  # Stop further execution if the model is not loaded

# Function to get user input
def get_user_input():
    skillsList = ('Angular', 'Ansible', 'BASH/SHELL', 'C/C++', 'Cisco Packet Tracer', 'Deep Learning',
                'Figma', 'GitHub', 'HTML/CSS', 'Java', 'JavaScript', 'Linux', 'Machine Learning', 'MySQL',
                'Node.js', 'Oracle', 'Photoshop', 'PyTorch', 'Python', 'R', 'React', 'TensorFlow', 'Wireshark')
    
    # Drop-down for skill selections
    skill_1 = st.selectbox('Skill 1', skillsList, index=21)
    skill_2 = st.selectbox('Skill 2', skillsList, index=19)

    # Collecting user inputs for each feature using sliders
    dsa = st.slider('DSA score (0-100)', min_value=0, max_value=100, value=72)
    dbms = st.slider('DBMS score (0-100)', min_value=0, max_value=100, value=74)
    os = st.slider('Operating Systems score (0-100)', min_value=0, max_value=100, value=73)
    cn = st.slider('Computer Networks score (0-100)', min_value=0, max_value=100, value=60)
    mathematics = st.slider('Mathematics score (0-100)', min_value=0, max_value=100, value=87)
    aptitude = st.slider('Aptitude score (0-100)', min_value=0, max_value=100, value=82)
    communication = st.slider('Communication score (0-100)', min_value=0, max_value=100, value=64)
    problem_solving = st.slider('Problem Solving score (0-10)', min_value=0, max_value=10, value=7)
    creativity = st.slider('Creativity score (0-10)', min_value=0, max_value=10, value=6)
    hackathons = st.slider('Number of Hackathons', min_value=0, max_value=10, value=4)

    # Ensure input is transformed appropriately for skills
    user_skills = skill_encoder.transform([[skill_1, skill_2]]).toarray()

    # Create a list of numerical features i.e. user_input
    user_input = [dsa, dbms, os, cn, mathematics, aptitude, communication, problem_solving, creativity, hackathons]

    # Combine numerical features and encoded skills
    numerical_features = scaler.transform(np.array(user_input).reshape(1, -1))
    user_input_transformed = np.hstack((numerical_features, user_skills))  # Combine arrays


    return user_input_transformed

# Main function to build the Streamlit app
def main():
    # Project Title and Description
    st.title("Job Profile Prediction")
    st.write("### About This Project")
    st.write(
        """
        This project aims to predict suitable job profiles for students based on their scores in various subjects and skills.
        The predictions are made using machine learning models.
        This web application allows users to input their scores and receive job suggestions.
        """
    )
    
    st.write("### How to Use This Application")
    st.write(
        """
        1. Select your top two skills from the dropdown lists provided.
        2. Use the sliders to enter your scores in various subjects including DSA, DBMS, Operating Systems, Computer Networks, Mathematics, Aptitude, Communication, Problem Solving, Creativity, and Hackathons.
        3. Click the **Predict Job Profile** button to see your predicted job profile based on the entered information.
        """
    )

    st.warning("Note: The model doesn't solely depends on yours skills, but also on the scores you given. Model suggests according your scores and skills combined.")

    # Get user input
    user_input_original = get_user_input()

    # When the user clicks the "Predict" button
    if st.button('Predict Job Profile'):
        # Make a prediction based on the user input
        user_input = user_input_original.copy()
        # Predict using the model
        predicted_profile = best_models['XGB'].predict(user_input)
        predicted_job = profile_encoder.inverse_transform(predicted_profile)
        
        # Display the prediction result
        st.success(f'Predicted Job Profile: {predicted_job[0]}')  


# Run the app
if __name__ == '__main__':
    main()