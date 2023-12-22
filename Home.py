import streamlit as st

st.set_page_config(layout="wide")

# Customize the sidebar
aboutInfo = """
This project attempts to explore the use of machine learning in detecting both fully and partially spoofed audio. 
\nCheck if the audio is bona fide or spoofed with SAD!"""

st.sidebar.title("About Us")
st.sidebar.info(aboutInfo)

# Customize page title
st.title("Spoof Audio Detection (SAD)")

st.write("Welcome to the forefront of audio authenticity in the digital age! In a world filled with awe-inspiring technological breakthroughs, the rise of 'deepfake' technology has sparked both marvel and concern.")
st.write("Imagine a reality where audio recordings can be convincingly altered to make someone appear to say things they never did. Deepfake audio has reached a level where human detection capabilities struggle, with participants correctly identifying deepfakes only 73% of the time (Mai et al., 2023).")

st.header("Bona Fide VS Spoof")

# Read spoof audio file
spoof_audio_file_path1 = "audio_sample/CON_T_0000001.wav"
with open(spoof_audio_file_path1, "rb") as spoof_audio_file1:
    spoof_audio_bytes1 = spoof_audio_file1.read()

spoof_audio_file_path2 = "audio_sample/CON_T_0000002.wav"
with open(spoof_audio_file_path2, "rb") as spoof_audio_file2:
    spoof_audio_bytes2 = spoof_audio_file2.read()

# Read bona fide audio file
bona_fide_audio_file_path = "audio_sample/LA_T_1007571.wav"
with open(bona_fide_audio_file_path, "rb") as bona_fide_audio_file:
    bona_fide_audio_bytes = bona_fide_audio_file.read()

audio1, audio2 = st.columns([1,1])

with audio1:
    # Display audio players
    st.write("🎵 Play this audio: ")
    st.audio(spoof_audio_bytes1, format='audio/wav')

with audio2:
    st.write("🎵 Play this audio too: ")
    st.audio(spoof_audio_bytes2, format='audio/wav')

st.info("Can you guess which one is a partially spoofed audio? ")

# Add three buttons for user guessing
col1, col2, col3 = st.columns([1,1,1])

first_button = col1.button("The First One!")
second_button = col2.button("The Second One!")
no_idea = col3.button("No idea!")

# Check user's guess
if first_button or second_button or no_idea:
    st.warning("""Awwww! Both of them are not bona fide audio :< 
                  \nBut don't worry, distinguishing between spoofed and bona fide audio can be tricky! 
                  That's why our Spoof Audio Detection (SAD) is here for you. """)

st.header("Partial Spoofed Audio")

markdown = """
How is the partial spoofed audio data generated?
1. Each partially spoofed audio in the database contains a mix of both spoofed and bona fide segments.
2. Each partially spoofed audio may contain audio segments generated using more than one text-to-speech or voice conversion method.
"""

st.markdown(markdown)
partialSpoofProcedure = "https://nii-yamagishilab.github.io/zlin-demo/IS2021/wavs/train/CON_T_0000001.png"
st.image(partialSpoofProcedure)
st.markdown("<div style='text-align: center;'><i>Procedure of data collection. (Example of CON_T_0000001.wav). (Zhang et al., 2022).</i></div>", unsafe_allow_html=True)

st.write("")
st.write("")
st.markdown("""The implications of deepfake audio are profound, as evidenced by cases of AI-driven voice cloning scams causing significant financial losses and emotional exploitation.
            Enter our solution — a deepfake audio detection algorithm designed to empower you in the battle against fraud audio content.""")
st.write("")

st.markdown("<div style='text-align: center; font-family: Georgia, serif; font-size: 20px;'><i>Welcome to Spoof Audio Detection (SAD), where the future of audio authenticity begins.</i></div>", unsafe_allow_html=True)
