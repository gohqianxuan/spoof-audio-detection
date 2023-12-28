# Import libraries
import streamlit as st
import librosa
import numpy as np
import pandas as pd
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
    
# Customize the sidebar
st.sidebar.markdown("<h1 style='font-family: Bahnschrift;'>Table of Contents</h1>", unsafe_allow_html=True)
st.sidebar.info("""
                [PartialSpoof Database](#partialspoof-database)\n
                [Exploratory Data Analysis](#exploratory-data-analysis)
                - [Audio Visualization](#audio-visualization)\n
                - [Distribution of Classes](#distribution-of-classes)
                """)
st.sidebar.write("")
st.sidebar.caption("© Made by Goh Qian Xuan. All rights reserved.")

# Customize page title
st.markdown("<h1 style='font-family: Bahnschrift; font-size: 50px; font-weight: 700;'>About Dataset</h1>", unsafe_allow_html=True)

# Intro to database
st.markdown("<h2 style='font-family: Bahnschrift;'>PartialSpoof Database</h2>", unsafe_allow_html=True)

st.markdown("<p style='text-align: justify;'>In the realm of deepfake audio, a distinct challenge arises known as '<strong>partial spoofing</strong>.' Unlike traditional deepfake content, partial spoofed audio merges genuine audio with synthesized speech segments, making it difficult to identify the fraudulent parts.</p>", unsafe_allow_html=True)

with st.expander("See how the partial spoofed audio is generated"):
    st.markdown("""
                #### How is the partial spoofed audio generated?
                1. **Normalization and VAD:** The waveform amplitudes of original and spoofed utterances are normalized to -26 dBov. Variable-length candidate segments are selected using three types of Voice Activity Detection (VAD), ensuring significant volume mismatches are mitigated.

                2. **Selection:** Candidate segments are chosen for replacement through a careful selection process. Conditions include selecting segments from different utterances of the same speaker, avoiding repetition, and ensuring original and substitute segments have similar durations.

                3. **Substitution and Concatenation:** Speech segments are substituted, and concatenation is performed using time-domain cross-correlation to find optimal concatenation points. Silent regions around speech are considered for a seamless waveform overlap-add method.

                4. **Labeling:** Each utterance is annotated with fine-grained segment labels, distinguishing between spoof and bona fide frames. Frames generated by Text-to-Speech/Voice Conversion (TTS/VC) are labeled as 'spoof,' while frames from genuine utterances are labeled as 'bona fide.'

                5. **Post-processing:** The database is balanced by quantizing intra-speech generated segment ratios into ten levels, ensuring equal representation of files with small and large ratios in each subset. Random sampling maintains consistency with the ASVspoof 2019 LA database.
                
                [Learn more about PartialSpoof Database](https://nii-yamagishilab.github.io/zlin-demo/IS2021/index.html)
                """, unsafe_allow_html=True) 

    partialSpoofProcedure = "https://nii-yamagishilab.github.io/zlin-demo/IS2021/wavs/train/CON_T_0000001.png"
    st.image(partialSpoofProcedure)
    st.markdown("<div style='text-align: center; font-size: 13px;'><i>Detail of audio substitution. (Example of CON_T_0000001.wav). (Zhang et al., 2022).</i></div>", unsafe_allow_html=True)
    st.write("")

# Styling
style = """
    <style>    
        [data-testid="stSidebarNav"] {
            background-image: url(https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmRscmdoZXdvY3VsbWg2ZzA2NzE2d3VhdHdtejJ6b2VkeTA2NmRkaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/ASBM73xrwXA7ij894w/giphy.gif);
            background-repeat: no-repeat;
            padding-top: 85px;
            background-position: 20px 20px;
            background-size: 280px;
            height: 48%;
        }

        div.st-emotion-cache-5rimss.e1nzilvr5 {
            font-family: 'Inter', sans-serif;
        }

        div.st-emotion-cache-16idsys.e1nzilvr5 {
            font-family: 'Inter', sans-serif;
        }

        [data-testid="stExpander"] details {
            box-shadow: rgba(50, 50, 105, 0.15) 0px 2px 5px 0px, rgba(0, 0, 0, 0.05) 0px 1px 1px 0px;
            border-radius: 15px;
            border-style: none;
            background-color: white;         
        }
    
        [data-testid="stAppViewContainer"] > .main {
            background-image: url("https://i.imgur.com/pcvge06.jpg");
            background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
            background-position: center;  
            background-repeat: no-repeat;
        }

        [data-testid="stAppViewContainer"] > .main::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(255, 255, 255, 0.88);  
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

st.divider()

# Exploratory data analysis
st.markdown("<h2 style='font-family: Bahnschrift;'>Exploratory Data Analysis</h2>", unsafe_allow_html=True)

# Plot audio visualization
with st.container(border=True):
    st.markdown("<h3 style='font-family: Bahnschrift;'>Audio Visualization</h3>", unsafe_allow_html=True)

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
        st.markdown("**Waveform** representation provides a visual of the audio signal over time, showcasing the amplitude variations in the audio file.")

    elif visualization_option == "Spectrogram":
        plot_spectrogram(audio_data_spoof, "Spoof - Spectrogram", ax[0])
        plot_spectrogram(audio_data_bona_fide, "Bona Fide - Spectrogram", ax[1])
        st.markdown("**Spectrogram** illustrates the frequency content of the audio signal across time, revealing patterns and characteristics in the audio spectrum.")

    elif visualization_option == "Mel Spectrogram":
        plot_mel_spectrogram(audio_data_spoof, "Spoof - Mel Spectrogram", ax[0])
        plot_mel_spectrogram(audio_data_bona_fide, "Bona Fide - Mel Spectrogram", ax[1])
        st.markdown("**Mel Spectrogram** highlights the distribution of energy in different frequency bands over time, offering insights into the audio's mel-frequency content.")

    elif visualization_option == "Chroma":
        plot_chroma(audio_data_spoof, "Spoof - Chroma", ax[0])
        plot_chroma(audio_data_bona_fide, "Bona Fide - Chroma", ax[1])
        st.markdown("**Chroma** representation captures the tonal content of the audio, emphasizing the presence of musical notes and harmonics throughout the recording.")

    st.write("")
    st.pyplot(fig)
    st.write("")

# Intro to MFCC&GTCC 
features_intro = """
    Even with visual representations, distinguishing genuine audio is still challenging for human. 
    This is where SpAD comes in! 
    SpAD leverages advanced machine learning algorithms trained on <strong>Mel-Frequency Cepstral Coefficients</strong> (MFCC) and <strong>Gammatone Cepstral Coefficients</strong> (GTCC) features. 
    These features are extracted from a diverse dataset of 25,380 audio files from the PartialSpoof Database.
    """
st.markdown(f"<p style='text-align: justify;'>{features_intro}</p>", unsafe_allow_html=True)

with st.expander("Learn more about **MFCC** and **GTCC**"):
    st.markdown(
        """
        <p style='text-align: justify;'>
            <h4>Mel-Frequency Cepstral Coefficients (MFCC)</h4>
            Think of MFCC as a translator for sound, enabling computers to understand the intricacies of audio. It breaks down sound into different components and captures its frequency content. This allows computers to analyze patterns and recognize unique characteristics in the audio signal.
            MFCCs can be calculated by conducting five consecutive processes, include signal framing, computing of the power spectrum, applying a Mel filter bank to the obtained power spectra, calculating the logarithm values, and finally applying the Discrete Cosine Transform (DCT).  
            <br><br>
            <h4>Gammatone Cepstral Coefficients (GTCC)</h4>
            GTCC takes MFCC a step further by mimicking how our ears hear. It employs Gammatone filters to capture the complexities of sound, making it robust even in noisy environments. GTCC features enhance SpAD's ability to identify patterns and nuances in audio, ensuring a reliable and secure audio authentication process.
            </p>
        """,
        unsafe_allow_html=True
    )
st.write("")

# Load GTCC-MFCC data
col_names = ['LogEnergy'] + [f'GTCC{i}' for i in range(13)] + ['LogEnergy_delta'] + [f'GTCC{i}_delta' for i in range(13)] + ['LogEnergy_delta-delta'] + [f'GTCC{i}_delta-delta' for i in range(13)] + [f'MFCC{i}' for i in range(13)] + [f'MFCC{i}_delta' for i in range(13)] + [f'MFCC{i}_delta-delta' for i in range(13)] + ['label']

train = pd.read_csv("extracted_features/GTCC-MFCC_train.csv", header=None, names=col_names)
val = pd.read_csv("extracted_features/GTCC-MFCC_val.csv", header=None, names=col_names)
test = pd.read_csv("extracted_features/GTCC-MFCC_test.csv", header=None, names=col_names)

# Show sample training data if toggled
if st.toggle('Show sample raw data after feature extraction (GTCC & MFCC)'):
    st.dataframe(train)
st.write("")

# Plot class distribution
with st.container(border=True):
    st.markdown("<h3 style='font-family: Bahnschrift;'>Distribution of Classes</h3>", unsafe_allow_html=True)

    # Combine datasets and map labels to 'spoof' and 'bona fide'
    data = pd.concat([train, val, test], keys=['Train', 'Validation', 'Test'], names=['Set'])
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
                    labels={'label': 'Class', 'count': 'Number of Samples'},
                    category_orders={'label': ['Spoof (0)', 'Bona fide (1)']},
                    color_discrete_map={'Spoof (0)': 'red', 'Bona fide (1)': 'blue'})

    # Show the Plotly figure
    st.plotly_chart(fig_class, use_container_width=True)

# Intro to smote 
smote = """
    Our class distribution bar chart reveals the imbalances between partial spoofed and bona fide audio data. 
    Fear not, for we've unleashed the power of <strong>SMOTE</strong> (Synthetic Minority Over-sampling Technique)!  
    This cutting-edge technique transforms our data distribution, oversampling the minority class, and harmonizing the symphony of our dataset.
    """
st.markdown(f"<p style='text-align: justify;'>{smote}</p>", unsafe_allow_html=True)
