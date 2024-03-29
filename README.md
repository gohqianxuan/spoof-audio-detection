# Spoof Audio Detection (SpAD)

_[Spoof Audio Detection App](https://spoof-audio-detection.streamlit.app/): Empower you in the battle against deepfake audio._ 

## Overview

This project explores the use of machine learning in detecting partially spoofed audio. Powered by robust machine learning models and wrapped in a Streamlit interface, SpAD helps you to differentiate between bona fide and spoofed audio.

## Database

The dataset used in this project is the labeled audio files from the [PartialSpoof database](https://zenodo.org/records/5766198) (Zhang et al., 2022). 

PartialSpoof is an open-source partially spoofed audio dataset constructed from ASVspoof 2019 LA database using some voice activity-detection (VAD) algorithms. Each partially spoofed utterance in the PartialSpoof database contains a mix of both spoofed and bona fide segments, and may contain audio segments generated using more than one TTS or VC method.

## Run SpAD Locally

1. Make sure [MATLAB](https://www.mathworks.com/help/install/install-products.html) is installed locally.
   
2. Clone the repository:

   ```bash
   git clone https://github.com/gohqianxuan/spoof-audio-detection.git
   ```

3. Navigate to the project directory:

   ```bash
   cd spoof-audio-detection
   ```

4. Install the dependencies:

   ```python
   pip install -r requirements.txt
   ```

5. Run the streamlit app:

   ```python
   streamlit run Home.py
   ```

6. Navigate to the provided local URL, and yay! Start identifying your audio.

## Contributions

Your valuable input can contribute to the improvement of this tool! Feel free to fork the project and make enhancements.
