import pandas as pd
import streamlit as st



# Create file uploader object
upload_file = st.file_uploader('Upload a file for prediction', type=['csv'])
rt0 = None  # Initialize rt0 as None

# Load the CSV file into a Pandas DataFrame
if upload_file is not None:
    rt0 = pd.read_csv(upload_file)
    rt0=rt0.dropna()

st.title('Data')

# Initialize selected_columns and selected_t to None
selected_columns = None
selected_t = None

# Check if rt0 is not None (file is uploaded)
if rt0 is not None:
    selected_columns = st.multiselect('Select columns to display:', rt0.columns)
    rt = rt0[selected_columns] if selected_columns else rt0

    st.write(rt.describe())
