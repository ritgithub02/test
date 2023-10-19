import numpy as np
import pandas as pd
import lasio
import matplotlib.pyplot as plt
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import missingno as msno

def load_data(uploadedfile):
    if uploadedfile:
        uploadedfile.seek(0)  # Reset buffer to the beginning each time
        string = uploadedfile.read().decode()
        las_file = lasio.read(string)
        # Create the DataFrame
        well_data = las_file.df()
        return las_file, well_data
    else:
        las_file = None
        well_data = None
    return las_file, well_data

# Create a Streamlit app
def main():
    st.title("LAS File Viewer")

    # Upload a LAS file
    uploaded_file = st.file_uploader("Upload a LAS file", type=["las", "LAS"])

    las_file, well_data = None, None  # Set default values

    if uploaded_file is not None:
        st.write("File Details:")
        st.write("Name:", uploaded_file.name)
        st.write("Type:", uploaded_file.type)
        st.write("Size:", uploaded_file.size, "bytes")

        # Call the load_data function
        las_file, well_data = load_data(uploaded_file)

        if las_file is not None:
            st.success("LAS file loaded successfully")
            st.write("Well Data:")
            st.write(well_data)

    return well_data

if __name__ == "__main__":
    well_data = main()
    if well_data is not None:
        well_data.reset_index(inplace=True)
        st.write(well_data)
        st.write(well_data.describe())
        st.write(well_data['DTCO'])
        well_data.to_csv('well_data.csv', index=False)

# Corrected tab names to match Streamlit
selected_tab = st.radio('Select Tab', ('Data Loading', 'Formation Evaluation', 'Visualization'))

if selected_tab == 'Data Loading':
    st.title("Data Loading Tab")
    well_df = pd.read_csv('well_data.csv')
    st.write('Logs:')
    st.write(well_df.columns)
    st.write('Statistics:')
    st.write(well_df.describe())

elif selected_tab == 'Formation Evaluation':
    st.title("Formation Evaluation Tab")
    # Add your formation evaluation code here

elif selected_tab == 'Visualization':
    st.title("Visualization Tab")

    def plot(well_df):
        fig, ax = plt.subplots(figsize=(6, 10))
        ax.plot(well_df['GR'], well_df['DEPTH'], lw=0.5, color='teal')
        ax.set_xlabel('GR')
        ax.set_ylabel('Depth (m)')
        ax.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
        ax.invert_yaxis()
        st.pyplot(fig)

    plot(well_df)
