# [Student Job Profile Suggester (Click here)](https://student-job-profile-suggester.streamlit.app/)

**🔗 Live Demo:**  
👉 [Click here to try it](https://student-job-profile-suggester-6dkmzzx7rxkg6fpce4pxp7.streamlit.app/)

This project aims to predict suitable job profiles for students based on their scores in various subjects and skills. The predictions are made using machine learning models. A Streamlit web application is provided to allow users to input their scores and receive job suggestions.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Models](#models)
- [Contributing](#contributing)
- [License](#license)

## Features
- Predicts suitable job profiles based on student scores in various subjects.
- Utilizes multiple machine learning models including Decision Tree, Random Forest, and Gradient Boosting, XG Boosting
- Implements Bayesian optimization for hyperparameter tuning.
- Provides a user-friendly web interface using Streamlit for real-time predictions.

## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Matplotlib
- Seaborn
- Streamlit
- BayesOpt

## Dataset
The dataset used in this project contains information about students' scores in the following subjects:
- DSA
- DBMS
- OS
- CN
- Mathematics
- Aptitude
- Communication
- Problem Solving
- Creativity
- Participation in Hackathons
- Skills (Top 1 and Top 2)
- Job Profile (Target variable)

## Usage
Run the Streamlit web application:
```bash
streamlit run app.py
```

## Models
The following models are trained and evaluated in this project:
- Decision Tree Classifier
- Random Forest Classifier
- radient Boosting
- XG Boosting

## 📁 Project Structure
```
Student-Job-Profile-Suggester/
├── app.py # Main Streamlit app
├── Models/
│ └── best_modelsV2.joblib # Trained ML model (XGB + encoders)
├── Code/
│ └── suggester.ipynb # Jupyter notebook (training & EDA)
├── Dataset/
│ └── StudentPlacement.csv
│ └── StudentPlacementGen.csv
├── requirements.txt # Project dependencies
```

## 🧪 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/akupadhyay8/Student-Job-Profile-Suggester.git
cd Student-Job-Profile-Suggester
```

### Instructions to Use
1. **Copy the Markdown Code**: Copy the above code into a new file named `README.md` in your project directory.
2. **Update the Content**: Feel free to modify any section to reflect your project specifics or to add additional details.
3. **Push to GitHub**: Once you've updated the README file, you can commit and push your changes to your GitHub repository.

## ⭐ Show Your Support

If you like this project:

- Give it a ⭐ on GitHub

- Share it with your peers

- Fork and customize your own version!

Let me know if you need any further assistance!

