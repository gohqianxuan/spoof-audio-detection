# Import libraries
import streamlit as st
import os
import glob
import librosa
import numpy as np
import pandas as pd
import seaborn as sns
import librosa.display
import soundfile as sf
import plotly.express as px
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram

# Function to get audio data
def get_sound_data(path):
    data, sr = sf.read(path)
    return data, sr

# Function to plot waveform
def plot_waveform(data, title, ax):
    ax.set_title(title)
    librosa.display.waveshow(data[0], sr=data[1], color='r', alpha=0.7, ax=ax)

# Function to plot spectrogram
def plot_spectrogram(data, title, ax):
    ax.set_title(title)
    Sxx, f, t, im = ax.specgram(data[0], Fs=data[1])
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Frequency (Hz)')
    ax.figure.colorbar(im, ax=ax)

# Function to plot mel spectrogram
def plot_mel_spectrogram(data, title, ax):
    ax.set_title(title)
    S = librosa.feature.melspectrogram(y=data[0], sr=data[1], n_mels=128)
    log_S = librosa.amplitude_to_db(S, ref=np.max)
    im = librosa.display.specshow(log_S, sr=data[1], x_axis='time', y_axis='mel', ax=ax)
    ax.figure.colorbar(im, format='%+02.0f dB', ax=ax)

# Function to plot chroma
def plot_chroma(data, title, ax):
    ax.set_title(title)
    S = librosa.feature.chroma_cqt(y=data[0], sr=data[1])
    im = librosa.display.specshow(S, sr=data[1], x_axis='time', y_axis='chroma', vmin=0, vmax=1, ax=ax)
    ax.figure.colorbar(im, ax=ax)

# Streamlit app
st.title("Exploratory Data Analysis (EDA)")

# Customize the sidebar
aboutInfo = """
This project attempts to explore the use of machine learning in detecting both fully and partially spoofed audio. 
\nCheck if the audio is bona fide or spoofed with SAD!"""

st.sidebar.title("About Us")
st.sidebar.info(aboutInfo)

# File paths
spoof_path = 'audio_sample/CON_T_0000001.wav'
bona_fide_path = 'audio_sample/LA_T_1007571.wav'

# Visualization selection
visualization_option = st.selectbox(
    "Select Audio Visualization",
    ["Waveform", "Spectrogram", "Mel Spectrogram", "Chroma"]
)

# Load audio data
audio_data_spoof = get_sound_data(spoof_path)
audio_data_bona_fide = get_sound_data(bona_fide_path)

# Plot selected visualization
fig, ax = plt.subplots(1, 2, figsize=(13, 5))  
if visualization_option == "Waveform":
    plot_waveform(audio_data_spoof, "Spoof - Waveform", ax[0])
    plot_waveform(audio_data_bona_fide, "Bona Fide - Waveform", ax[1])
elif visualization_option == "Spectrogram":
    plot_spectrogram(audio_data_spoof, "Spoof - Spectrogram", ax[0])
    plot_spectrogram(audio_data_bona_fide, "Bona Fide - Spectrogram", ax[1])
elif visualization_option == "Mel Spectrogram":
    plot_mel_spectrogram(audio_data_spoof, "Spoof - Mel Spectrogram", ax[0])
    plot_mel_spectrogram(audio_data_bona_fide, "Bona Fide - Mel Spectrogram", ax[1])
elif visualization_option == "Chroma":
    plot_chroma(audio_data_spoof, "Spoof - Chroma", ax[0])
    plot_chroma(audio_data_bona_fide, "Bona Fide - Chroma", ax[1])

st.pyplot(fig)

# Header for partial spoof database distribution
st.header("PartialSpoof Database")

# Load GTCC-MFCC data
col_names = ['feature' + str(i) for i in range(1, 80)]
col_names.append('label')

train = pd.read_csv("extracted_features/GTCC-MFCC_train.csv", header=None, names=col_names)
val = pd.read_csv("extracted_features/GTCC-MFCC_val.csv", header=None, names=col_names)
test = pd.read_csv("extracted_features/GTCC-MFCC_test.csv", header=None, names=col_names)

# Combine datasets to show dataframe
data = pd.concat([train, val, test], ignore_index=True)

if st.checkbox('Show Raw Data (GTCCs & MFCCs)'):
    st.dataframe(data)

st.subheader("Distribution of Classes (After Feature Extraction)")

# Combine datasets and map labels to 'spoof' and 'bona fide'
data = pd.concat([train, val, test], ignore_index=True, keys=['Train', 'Validation', 'Test'], names=['Set'])
data = data.reset_index()
data['label'] = data['label'].map({0: 'Spoof (0)', 1: 'Bona fide (1)'})

# Sidebar for selecting the dataset
selected_set = st.selectbox("Select Dataset", ["All", "Train", "Validation", "Test"])

# Filter the data based on the selected dataset
if selected_set == "All":
    selected_data = data
else:
    selected_data = data[data['Set'] == selected_set]

# Count the number of samples for each class
class_counts = selected_data['label'].value_counts().reset_index()
class_counts.columns = ['label', 'count']

# Interactive distribution plot with Plotly
fig_class = px.bar(class_counts, x='label', y='count', color='label',
                #    title=f'Distribution of Classes ({selected_set} Set)',
                   labels={'label': 'Class', 'count': 'Number of Samples'},
                   category_orders={'label': ['Spoof (0)', 'Bona fide (1)']},
                   color_discrete_map={'Spoof (0)': 'red', 'Bona fide (1)': 'blue'})

# Show the Plotly figure
st.plotly_chart(fig_class, use_container_width=True)

# st.subheader("Distribution of Audio Duration")

# # Load audio duration data
# duration_path = "extracted_features/audioDuration.csv"
# duration_data = pd.read_csv(duration_path)

# # Create an interactive violin plot with Plotly for audio duration distribution
# fig_duration = px.violin(duration_data, x="Label", y="duration", box=True, points="all", hover_data=["duration"])

# # Display the Plotly figure in Streamlit
# st.plotly_chart(fig_duration, use_container_width=True)
