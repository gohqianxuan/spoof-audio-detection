# Import library
import streamlit as st
from streamlit_extras.switch_page_button import switch_page

# Set Streamlit page configuration
st.set_page_config(layout="wide")

# Customize page title
st.markdown("<h1 style='font-family: Bahnschrift;'>Spoof Audio Detection (SpAD)</h1>", unsafe_allow_html=True)

# Customize the sidebar
aboutInfo = """
This project explores the use of machine learning in detecting both fully and partially spoofed audio. 
\nCheck if the audio is bona fide or spoofed with [SpAD](https://spoof-audio-detection.streamlit.app/Spoof_Audio_Detection_(SpAD))!"""

st.sidebar.markdown("<h1 style='font-family: Bahnschrift;'>About SpAD</h1>", unsafe_allow_html=True)
st.sidebar.info(aboutInfo)
st.sidebar.write("")
st.sidebar.caption("© Made by Goh Qian Xuan. All rights reserved.")

# Introduction section
intro = """Welcome to the forefront of audio authenticity in the digital age! In a world filled with awe-inspiring technological breakthroughs, the rise of 'deepfake' technology has sparked both marvel and concern.
        <br><br>
        Imagine a reality where audio recordings can be convincingly altered to make someone appear to say things they never did. Deepfake audio has reached a level where human detection capabilities struggle, with participants in a recent study correctly identifying deepfakes only 73% of the time.
        """
st.markdown(f"<p style='text-align: justify;'>{intro}</p>", unsafe_allow_html=True)
st.write("")

# Display Spoof vs. Bona Fide audios
with st.container(border=True):
    st.markdown("<h2 style='font-family: Bahnschrift; text-align: center;'>Bona Fide VS Spoof</h2>", unsafe_allow_html=True)

    # Read spoof audio file
    spoof_audio_file_path = "audio_sample/CON_T_0000001.wav"
    with open(spoof_audio_file_path, "rb") as spoof_audio_file:
        spoof_audio_bytes = spoof_audio_file.read()

    # Read bona fide audio file
    bona_fide_audio_file_path = "audio_sample/CON_T_0000002.wav"
    with open(bona_fide_audio_file_path, "rb") as bona_fide_audio_file:
        bona_fide_audio_bytes = bona_fide_audio_file.read()

    # Display audio players
    audio1, audio2 = st.columns([1, 1])

    with audio1:
        st.write("🎵 Play this audio: ")
        st.audio(spoof_audio_bytes, format='audio/wav')

    with audio2:
        st.write("🎵 Play this audio too: ")
        st.audio(bona_fide_audio_bytes, format='audio/wav')

    st.info("Can you guess which one is a partially spoofed audio? ")

    # Add three buttons for user guessing
    col1, col2, col3 = st.columns([1, 1, 1])
    st.write("")

    first_button = col1.button("The First One!")
    second_button = col2.button("The Second One!")
    no_idea = col3.button("No idea!")

    # Check user's guess
    if first_button or second_button or no_idea:
        st.error("""Awwww! Both of them are not bona fide audio :< 
                    \nBut don't worry, distinguishing between spoofed and bona fide audio can be tricky! 
                    That's why our Spoof Audio Detection (SpAD) is here for you. """)
        st.write("")

# Additional sections
st.write("")
st.markdown("""<p style='text-align: justify;'>
            The downside of deepfake audio are profound, as evidenced by cases of AI-driven voice cloning scams causing significant financial losses and emotional exploitation.
            <br><br>
            Enter our solution — a deepfake audio detection algorithm designed to empower you in the battle against fraud audio content.
            </p>""", unsafe_allow_html=True)

st.divider()

st.markdown("<h2 style='font-family: Bahnschrift;'>Why SpAD?</h2>", unsafe_allow_html=True)
st.markdown("Click on each **box** to learn more about SpAD.")
st.write("")

p1, p2, p3 = st.columns([1,1,1])
p1.markdown("<h5 style='font-family: Bahnschrift; text-align: center;'>Vast Database</h5>", unsafe_allow_html=True)
p2.markdown("<h5 style='font-family: Bahnschrift; text-align: center;'>Top-Performing Model</h5>", unsafe_allow_html=True)
p3.markdown("<h5 style='font-family: Bahnschrift; text-align: center;'>User-Friendly</h5>", unsafe_allow_html=True)
dataset = p1.button("SpAD enhances audio security by learning from a vast database of audio files, protecting you from fraud and scams.")
model = p2.button("SpAD leverages the power of machine learning to deliver a robust solution for accurate and reliable audio authentication.")
spad = p3.button("The SpAD web app brings audio authentication to your fingertips, making it easy for users to identify spoofed audio")

if dataset:
    switch_page("About Dataset")
if model:
    switch_page("About Model")
if spad:
    switch_page("Spoof_Audio_Detection_(SpAD)")

st.divider()

st.markdown("<h3 style='text-align: center; font-family: Georgia, serif; font-weight: 400'><i>Welcome to Spoof Audio Detection (SpAD), where the future of audio authenticity begins.</i></h3>", unsafe_allow_html=True)

# Styling
background = """
    <style>
        [data-testid="stAppViewContainer"] > .main {
            background-image: linear-gradient(rgba(255, 255, 255, 0.88), rgba(255, 255, 255, 0.88)), 
                              url("https://i.imgur.com/pcvge06.jpg");
            background-size: cover;  /* Use "cover" to maintain aspect ratio and cover the entire container */
            background-position: center;
            background-repeat: repeat;
        }
    </style>
    """

sidebarLogo = """
    <style>    
        [data-testid="stSidebarNav"] {
            background-image: url(https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmRscmdoZXdvY3VsbWg2ZzA2NzE2d3VhdHdtejJ6b2VkeTA2NmRkaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/ASBM73xrwXA7ij894w/giphy.gif);
            background-repeat: no-repeat;
            padding-top: 85px;
            background-position: 20px 20px;
            background-size: 280px;
            height: 48%;
        }
    </style>
    """

pageFont = """
    <style>          
        div.st-emotion-cache-5rimss.e1nzilvr5 {
            font-family: 'Inter', sans-serif;
        }

        div.st-emotion-cache-16idsys.e1nzilvr5 {
            font-family: 'Inter', sans-serif;
        }

        body {
            font-family: 'Inter', sans-serif;
        }
    </style>
    """

expanderBorder = """
    <style>          
        [data-testid="stExpander"] details {
            box-shadow: rgba(50, 50, 105, 0.15) 0px 2px 5px 0px, rgba(0, 0, 0, 0.05) 0px 1px 1px 0px;
            border-radius: 15px;
            border-style: none;
            background-color: white;      
        }
    </style>
    """
        
bonaFideVsSpoof = """
    <style>  
        [data-testid="baseButton-secondary"] {
            box-shadow: rgba(50, 50, 105, 0.15) 0px 2px 5px 0px, rgba(0, 0, 0, 0.05) 0px 1px 1px 0px;
            border-radius: 10px;
            border-style: none;
            background-color: white;
            width: 100%;  
        }

        div.st-emotion-cache-r421ms.e1f1d6gn0 {
            box-shadow: rgba(50, 50, 105, 0.15) 0px 2px 5px 0px, rgba(0, 0, 0, 0.05) 0px 1px 1px 0px;
            border-radius: 15px;
            border-style: none;
            background-color: white; 
            padding: 2% 4%;  
        }

        div.st-emotion-cache-keje6w.e1f1d6gn3 {
            padding: 1%;
        }  

       div.st-emotion-cache-1vbkxwb.e1nzilvr5 {
            padding: 3%;
            text-align: justify;
        }
    </style>
    """

# Apply styles
st.markdown(background, unsafe_allow_html=True)
st.markdown(sidebarLogo, unsafe_allow_html=True)
st.markdown(pageFont, unsafe_allow_html=True)
st.markdown(expanderBorder, unsafe_allow_html=True)
st.markdown(bonaFideVsSpoof, unsafe_allow_html=True)
