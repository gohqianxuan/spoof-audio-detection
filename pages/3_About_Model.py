# Import library
import streamlit as st

# Customize the sidebar
st.sidebar.markdown("<h1 style='font-family: Bahnschrift;'>Table of Contents</h1>", unsafe_allow_html=True)
st.sidebar.info("""
                [Random Forest](#random-forest)\n
                [Extreme Gradient Boosting (XGBoost)](#extreme-gradient-boosting-xgboost)\n
                [Support Vector Machine (SVM)](#support-vector-machine-svm)\n
                [K-Nearest Neighbors (KNN)](#k-nearest-neighbors-knn)
                """)
st.sidebar.write("")
st.sidebar.caption("© Made by Goh Qian Xuan. All rights reserved.")

# Customize page title
st.markdown("<h1 style='font-family: Bahnschrift; font-size: 50px; font-weight: 700;'>About Model</h1>", unsafe_allow_html=True)

st.markdown("""<p style='text-align: justify;'>
            Dive into the realm of advanced audio classification with our <strong>machine learning</strong> models. 
            Explore the intricate stages of our architecture — from initial audio file input through feature extraction, strategic oversampling, model training, to the pinnacle of classification. 
            </p>""", unsafe_allow_html=True)

with st.expander("Check out the architecture of SpAD's audio classification model"):
    st.write("")
    st.image("https://i.imgur.com/0eKv4vS.png")
    st.markdown("<div style='text-align: center; font-size: 14px;'><i>Architecture of SpAD's audio classification model.</i></div>", unsafe_allow_html=True)
    st.write("")

st.markdown("""<p style='text-align: justify;'>
            Our four meticulously trained models are poised for comparison, each revealing its unique strengths, leading to the selection of the top performer — <strong>Random Forest</strong>.  
            </p>""", unsafe_allow_html=True)

st.divider()

# Styling
style = """
        <style>    
            [data-testid="stSidebarNav"] {
                background-image: url(https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdmRscmdoZXdvY3VsbWg2ZzA2NzE2d3VhdHdtejJ6b2VkeTA2NmRkaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/ASBM73xrwXA7ij894w/giphy.gif);
                background-repeat: no-repeat;
                padding-top: 90px;
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

            [data-testid="stExpander"] details {
                box-shadow: rgba(50, 50, 105, 0.15) 0px 2px 5px 0px, rgba(0, 0, 0, 0.05) 0px 1px 1px 0px;
                border-radius: 15px;
                border-style: none;
                background-color: white;      
            }

            div.st-emotion-cache-keje6w.e1f1d6gn3 {
                box-shadow: rgba(50, 50, 105, 0.15) 0px 2px 5px 0px, rgba(0, 0, 0, 0.05) 0px 1px 1px 0px;
                border-radius: 15px;
                border-style: none;
                background-color: white; 
                padding: 2% 2%;              
            }
            
            body {
                font-family: 'Inter', sans-serif;
            }
            </style>
            """

# Apply styles
st.markdown(style, unsafe_allow_html=True)

# Random Forest
st.markdown("<h2 style='font-family: Bahnschrift;'>Random Forest</h2>", unsafe_allow_html=True)
st.markdown("""<p style='text-align: justify;'>
            Harnessing the power of an ensemble of decision trees to discern between bona fide and spoofed audio with precision.
            </p>""", unsafe_allow_html=True)

st.markdown("""
    - **Accuracy:** 0.82
    - **F1 score (weighted):** 0.85
    - **Area under the ROC Curve:** 0.78
    """)
st.write("")

metric1, metric2 = st.columns([1,1])

with metric1:
    st.markdown("<p style='font-family: Bahnschrift; font-size: 18px;'>Confusion matrix</p>", unsafe_allow_html=True)
    st.image("https://i.imgur.com/jsRTexM.png")
with metric2:
    st.markdown("<p style='font-family: Bahnschrift; font-size: 18px;'>Receiver operating characteristic (ROC) curve</p>", unsafe_allow_html=True)
    st.image("https://i.imgur.com/oNVqY8t.png")

st.divider()

#XGBoost
st.markdown("<h2 style='font-family: Bahnschrift;'>Extreme Gradient Boosting (XGBoost)</h2>", unsafe_allow_html=True)
st.markdown("""<p style='text-align: justify;'>
            A boosted approach to audio authenticity detection, leveraging gradient boosting for superior discrimination between bona fide and spoofed audios.
            </p>""", unsafe_allow_html=True)

st.markdown("""
    - **Accuracy:** 0.80
    - **F1 score (weighted):** 0.83
    - **Area under the ROC Curve:** 0.77
    """)
st.write("")

metric1, metric2 = st.columns([1,1])

with metric1:
    st.markdown("<p style='font-family: Bahnschrift; font-size: 18px;'>Confusion matrix</p>", unsafe_allow_html=True)
    st.image("https://i.imgur.com/O2GdL4A.png")
with metric2:
    st.markdown("<p style='font-family: Bahnschrift; font-size: 18px;'>Receiver operating characteristic (ROC) curve</p>", unsafe_allow_html=True)
    st.image("https://i.imgur.com/9hl884Z.png")

st.divider()

#SVM
st.markdown("<h2 style='font-family: Bahnschrift;'>Support Vector Machine (SVM)</h2>", unsafe_allow_html=True)
st.markdown("""<p style='text-align: justify;'>
            Merging mathematical elegance with discerning power, Support Vector Machine crafts a symphony of precision to differentiate between bona fide and spoofed audio.
            </p>""", unsafe_allow_html=True)

st.markdown("""
    - **Accuracy:** 0.79
    - **F1 score (weighted):** 0.83
    - **Area under the ROC Curve:** 0.73
    """)
st.write("")

metric1, metric2 = st.columns([1,1])

with metric1:
    st.markdown("<p style='font-family: Bahnschrift; font-size: 18px;'>Confusion matrix</p>", unsafe_allow_html=True)
    st.image("https://i.imgur.com/D0J1qjX.png")
with metric2:
    st.markdown("<p style='font-family: Bahnschrift; font-size: 18px;'>Receiver operating characteristic (ROC) curve</p>", unsafe_allow_html=True)
    st.image("https://i.imgur.com/zJNP7qp.png")

st.divider()

#KNN
st.markdown("<h2 style='font-family: Bahnschrift;'>K-Nearest Neighbors (KNN)</h2>", unsafe_allow_html=True)
st.markdown("""<p style='text-align: justify;'>
            Navigating audio landscapes with proximity-based intuition, K-Nearest Neighbors model weaves a tapestry of accuracy to pinpoint bona fide audio amidst the noise.
            </p>""", unsafe_allow_html=True)

st.markdown("""
    - **Accuracy:** 0.67
    - **F1 score (weighted):** 0.73
    - **Area under the ROC Curve:** 0.67
    """)
st.write("")

metric1, metric2 = st.columns([1,1])

with metric1:
    st.markdown("<p style='font-family: Bahnschrift; font-size: 18px;'>Confusion matrix</p>", unsafe_allow_html=True)
    st.image("https://i.imgur.com/T3O0kX0.png")
with metric2:
    st.markdown("<p style='font-family: Bahnschrift; font-size: 18px;'>Receiver operating characteristic (ROC) curve</p>", unsafe_allow_html=True)
    st.image("https://i.imgur.com/sYNkfad.png")
