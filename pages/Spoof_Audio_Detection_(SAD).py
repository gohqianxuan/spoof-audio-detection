import streamlit as st
import os
import time
import joblib
import scipy.io
import subprocess
import pandas as pd
import soundfile as sf
from sklearn.preprocessing import StandardScaler

# Function to extract features using MATLAB script
def extract_features(audio_path):
    mat_path = 'features.mat'

    # Run MATLAB with the script file and pass arguments
    subprocess.run(["matlab", "-nosplash", "-nodesktop", "-r", f"feature_extraction('{audio_path}', '{mat_path}')"])

    with st.spinner("Analyzing audio patterns..."):
        # Wait until the "features.mat" file is created
        max_wait_time = 30  # Maximum wait time in seconds
        waited_time = 0

        while not os.path.exists("features.mat") and waited_time < max_wait_time:
            time.sleep(1)  # Wait for 1 second
            waited_time += 1

        # Check if the "features.mat" file is now available
        if os.path.exists("features.mat"):
            # Load the features from the MAT file
            mat_contents = scipy.io.loadmat(mat_path)
            hybrid_features = mat_contents['hybridFeatures']

        else:
            st.warning("Error: Unable to generate features. Please try uploading the audio file again.")
            # You might want to handle the error condition appropriately (e.g., display a message to the user)

    return hybrid_features

# Function to normalize the extracted features
def normalize_features(features):
    # Extract features from the training data
    train = pd.read_csv(r"D:\User\Downloads\DSProject_Data\PartialSpoof\GTCC-MFCC_train.csv", header=None)
    X_train = train.iloc[:, :-1]
    
    # Fit and transform the training data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)

    # Normalize the input features based on the training data statistics
    normalized_features = scaler.transform(features)

    return normalized_features

# Function to predict class using machine learning model
def predict_class(features):
    # Load the trained model
    model = joblib.load("RandomForestClassifier")
    
    # Make predictions
    prediction = model.predict(features)

    return prediction[0]

# Streamlit app
st.title("Spoof Audio Detection (SAD)")

# Customize the sidebar
aboutInfo = """
This project attempts to explore the use of machine learning in detecting both fully and partially spoofed audio. 
\nCheck if the audio is bona fide or spoofed with SAD!"""

st.sidebar.title("About Us")
st.sidebar.info(aboutInfo)

# Upload audio file
audio_formats = ["wav", "mp3", "ogg"] 
uploaded_file = st.file_uploader("Choose an audio file", type=audio_formats)

if uploaded_file is not None:
    st.audio(uploaded_file, format=f'audio/{os.path.splitext(uploaded_file.name)[-1][1:]}', start_time=0)

    # Save the uploaded file temporarily
    audio_path = "uploaded_audio" 
    file_extension = os.path.splitext(uploaded_file.name)[-1].replace(".", "")
    audio_path += f".{file_extension}" 

    with open(audio_path, "wb") as f:
        f.write(uploaded_file.getvalue())

    # Extract features using MATLAB
    features = extract_features(audio_path)

    # Normalize the input features based on the training data statistics
    normalized_features = normalize_features(features) 

    # Predict class using the machine learning model
    prediction = predict_class(normalized_features)

    # Display the prediction
    st.subheader("Prediction: " + ("Spoof Detected!" if prediction == 0 else "Bona Fide Voice!"))

    if prediction == 0:
        col1, col2 = st.columns([1, 3.5])

        # Image column
        with col1:
            st.image("https://i.imgur.com/ZhWCcT1.png", width=150)  

        # Text column
        with col2:
            st.text("\n\n")  # Add two empty lines
            st.write("Uh-oh! This audio file seems to be crafted by a mischievous machine.")
            st.write("Maybe a sneaky robot tried to trick us!")

    else:
        col1, col2 = st.columns([1, 3])

        # Image column
        with col1:
            st.image("https://i.imgur.com/vRqhj7A.png", width=130) 
            
        # Text column
        with col2:
            st.text("\n\n")  # Add two empty lines
            st.markdown("Yay! Congratulations! This audio file is likely the sweet sound of a genuine human voice.")
            st.markdown("It seems like a wonderful human serenade!")

    # Remove the temporary audio file
    os.remove(audio_path)
    os.remove("features.mat")
