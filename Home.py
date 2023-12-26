import streamlit as st

# Set Streamlit page configuration
st.set_page_config(layout="wide")

# Customize page title
st.markdown("<h1 style='font-family: Bahnschrift; font-size: 50px; font-weight: 700;'>Spoof Audio Detection (SpAD)</h1>", unsafe_allow_html=True)

# Customize the sidebar
aboutInfo = """
This project explores the use of machine learning in detecting both fully and partially spoofed audio. 
\nCheck if the audio is bona fide or spoofed with [SpAD](https://spoof-audio-detection.streamlit.app/Spoof_Audio_Detection_(SpAD))!"""

st.sidebar.markdown("<h1 style='font-family: Bahnschrift;'>About SpAD</h1>", unsafe_allow_html=True)
st.sidebar.info(aboutInfo)
st.sidebar.write("")
st.sidebar.caption("© Made by Goh Qian Xuan. All rights reserved.")

# Introduction section
intro = """
    Welcome to the forefront of audio authenticity in the digital age! In a world filled with awe-inspiring technological breakthroughs, the rise of 'deepfake' technology has sparked both marvel and concern.
    \n\nImagine a reality where audio recordings can be convincingly altered to make someone appear to say things they never did. Deepfake audio has reached a level where human detection capabilities struggle, with participants correctly identifying deepfakes only 73% of the time (Mai et al., 2023).
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
st.markdown("""The implications of deepfake audio are profound, as evidenced by cases of AI-driven voice cloning scams causing significant financial losses and emotional exploitation.
            \nEnter our solution — a deepfake audio detection algorithm designed to empower you in the battle against fraud audio content.""")

st.divider()

st.markdown("<h2 style='font-family: Bahnschrift;'>Why SpAD?</h2>", unsafe_allow_html=True)
st.markdown("""
    - **Security:** SpAD enhances audio security by learning from a vast database of audio files, ensuring accurate and reliable detection.

    - **Robustness:** GTCC (Gammatone Cepstral Coefficients) features make SpAD resilient in various environments, providing consistent performance even in challenging acoustic conditions.

    - **User-Friendly:** SpAD brings advanced audio authentication to your fingertips, making it easy for users to identify genuine audio.
    """)

st.divider()

st.markdown("<h2 style='font-family: Bahnschrift;'>How SpAD Works:</h2>", unsafe_allow_html=True)
st.markdown("""
            1. **Learning from Data:** SpAD learns from a diverse set of 25,380 audio files, making it adept at recognizing patterns and distinguishing between genuine and spoofed audio.

            2. **GTCC and MFCC Features:** By extracting GTCC (Gammatone Cepstral Coefficients) and MFCC (Mel-Frequency Cepstral Coefficients) features, SpAD captures the unique characteristics of audio signals, ensuring a robust and accurate authentication process.

            3. **User-Friendly Interface:** The SpAD web app provides an intuitive interface for users to analyze audio files and determine their authenticity.
            """)

st.divider()
st.markdown("<div style='text-align: center; font-family: Georgia, serif; font-size: 29px;'><i>Welcome to Spoof Audio Detection (SpAD), where the future of audio authenticity begins.</i></div>", unsafe_allow_html=True)

# Styling
background = """
    <style>  
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
    </style>
    """

sidebarLogo = """
    <style>    
        [data-testid="stSidebarNav"] {
            background-image: url(https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmRscmdoZXdvY3VsbWg2ZzA2NzE2d3VhdHdtejJ6b2VkeTA2NmRkaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/ASBM73xrwXA7ij894w/giphy.gif);
            background-repeat: no-repeat;
            padding-top: 90px;
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
            padding: 1% 2%;  
        }

        div.st-emotion-cache-keje6w.e1f1d6gn3 {
            padding: 1%;
        }         
    </style>
    """

# Apply styles
st.markdown(background, unsafe_allow_html=True)
st.markdown(sidebarLogo, unsafe_allow_html=True)
st.markdown(pageFont, unsafe_allow_html=True)
st.markdown(expanderBorder, unsafe_allow_html=True)
st.markdown(bonaFideVsSpoof, unsafe_allow_html=True)
