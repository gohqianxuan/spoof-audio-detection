import streamlit as st
import os
import time
import joblib
import scipy.io
import subprocess
import numpy as np
import soundfile as sf
import plotly.express as px

# Function to get audio data
def get_sound_data(path):
    data, sr = sf.read(path)
    return data, sr

# Function to plot animated waveform
def plot_animated_waveform(audio_data, sample_rate):
    time = np.arange(0, len(audio_data)) / sample_rate
    fig = px.line(x=time, y=audio_data, labels={'x': 'Time (s)', 'y': 'Amplitude'})    
    st.plotly_chart(fig, use_container_width=True)

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
            
    return hybrid_features

# Function to normalize the extracted features
def normalize_features(features):
    # Load StandardScaler()
    scaler = joblib.load("Scaler")

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

# Customize the sidebar
howTo = """
1. Upload your audio file
2. Explore its waveform
3. Wait for a few seconds
4. Check out the result"""

st.sidebar.markdown("<h1 style='font-family: Bahnschrift;'>How To Use</h1>", unsafe_allow_html=True)
st.sidebar.info(howTo)
st.sidebar.write("")
st.sidebar.caption("© Made by Goh Qian Xuan. All rights reserved.")

# Customize page title
st.markdown("<h1 style='font-family: Bahnschrift;'>Spoof Audio Detection (SpAD)</h1>", unsafe_allow_html=True)

# Styling
style = """
    <style>    
        .stTabs [data-baseweb="tab-list"] {
            gap: 6px;
        }

        .stTabs [data-baseweb="tab"] {
            height: 40px;
            box-shadow: rgba(50, 50, 105, 0.15) 0px 2px 5px 0px, rgba(0, 0, 0, 0.05) 0px 1px 1px 0px;
            border-radius: 15px 15px 0px 0px;
            border-style: none;
            background-color: #F0F2F6; 
            padding: 8px 15px 6px 15px;
            font-weight: bold;
        }

        .stTabs [aria-selected="true"] {
            background-color: #FFFFFF;
        }
    
        [data-testid="stSidebarNav"] {
            background-image: url(https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmRscmdoZXdvY3VsbWg2ZzA2NzE2d3VhdHdtejJ6b2VkeTA2NmRkaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/ASBM73xrwXA7ij894w/giphy.gif);
            background-repeat: no-repeat;
            padding-top: 85px;
            background-position: 20px 20px;
            background-size: 280px;
            height: 48%;
        }

        div.st-emotion-cache-t6mpn0.e1f1d6gn2 {
            width: 50%;
        }
        
        div.st-emotion-cache-5rimss.e1nzilvr5 {
            font-family: 'Inter', sans-serif;
        }

        div.st-emotion-cache-16idsys.e1nzilvr5 {
            font-family: 'Inter', sans-serif;
        }

        [data-testid="stAppViewContainer"] > .main {
            background-image: linear-gradient(rgba(255, 255, 255, 0.88), rgba(255, 255, 255, 0.88)), 
                              url("https://i.imgur.com/pcvge06.jpg");
            background-size: cover;  /* Use "cover" to maintain aspect ratio and cover the entire container */
            background-position: center;
            background-repeat: repeat;
        }

        div.st-emotion-cache-r421ms.e1f1d6gn0 {
            box-shadow: rgba(50, 50, 105, 0.15) 0px 2px 5px 0px, rgba(0, 0, 0, 0.05) 0px 1px 1px 0px;
            border-radius: 15px;
            border-style: none;
            background-color: white; 
            padding: 1% 2%;              
        }
        
        body {
                font-family: 'Inter', sans-serif;
            }

    </style>
    """

# Apply styles
st.markdown(style, unsafe_allow_html=True)

# Users upload audio file
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

    # Get audio data
    audio_data, sample_rate = get_sound_data(audio_path)

    # Create tabs after audio upload
    tab1, tab2 = st.tabs(["Waveform", "Prediction Result"])
    
    # Tab 1: Waveform
    with tab1:
        st.markdown("<h3 style='font-family: Bahnschrift;'>Waveform of Your Audio</h3>", unsafe_allow_html=True)

        with st.container(border=True):
            plot_animated_waveform(audio_data, sample_rate)
        
    # Tab 2: Prediction Result
    with tab2:
        # Extract features using MATLAB
        features = extract_features(audio_path)

        # Normalize the input features based on the training data statistics
        normalized_features = normalize_features(features) 

        # Predict class using the machine learning model
        prediction = predict_class(normalized_features)

        # Display the prediction
        if prediction == 0:
            st.markdown("<h3 style='font-family: Bahnschrift';>Spoof Detected</h3>", unsafe_allow_html=True)

            col1, col2 = st.columns([1, 5])
            # Image column
            with col1:
                st.image("https://i.imgur.com/ZhWCcT1.png", width=135)  

            # Text column
            with col2:
                st.write("")
                st.write("")
                spoof = """Uh-oh! This audio file seems to be crafted by a mischievous machine.
                Maybe a sneaky robot tried to trick us!"""
                st.markdown(f"<p style='text-align: justify; font-size: 17px;'>{spoof}</p>", unsafe_allow_html=True)

        else:
            st.markdown("<h3 style='font-family: Bahnschrift;'>Bona Fide Voice</h3>", unsafe_allow_html=True)
            st.balloons()

            col1, col2 = st.columns([1, 5])
            # Image column
            with col1:
                st.image("https://i.imgur.com/vRqhj7A.png", width=115) 

            # Text column
            with col2:
                st.write("")
                st.write("")
                bonafide = """Yay! Congratulations! This audio file is likely the sweet sound of a genuine human voice.
                It seems like a wonderful human serenade."""
                st.markdown(f"<p style='text-align: justify; font-size: 17px;'>{bonafide}</p>", unsafe_allow_html=True)

        # Remove the temporary audio file
        os.remove(audio_path)
        os.remove("features.mat")
