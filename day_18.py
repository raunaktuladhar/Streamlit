# st.file_uploader
'''
st.file_uploader displays a file uploader widget.
By default, uploaded files are limited to 200MB. 
You can configure this using the server.maxUploadSize config option. 
For more info on how to set config options, see.
'''

import streamlit as st
import pandas as pd

st.title("st.file_uploader")

st.subheader("Input CSV")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.subheader("Dataframe")
    st.write(df)
    st.subheader("Descriptive Statistics")
    st.write(df.describe())

else:
    st.info("Upload a CSV file")