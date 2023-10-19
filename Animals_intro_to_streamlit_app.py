import numpy as np
import pandas as pd
import lasio 
import matplotlib.pyplot as plt
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import plotly.express as px
import plotly.subplots
from PIL import Image
import missingno as msno

def load_data(uploadedfile):
    if uploadedfile:
        uploadedfile.seek(0)
        string = uploadedfile.read().decode()
        las_file = lasio.read(string)
        well_data = las_file.df()
    else:
        las_file = None
        well_data = None
    return las_file, well_data

def main():
    st.title("LAS File Viewer")
    uploaded_file = st.file_uploader("Upload a LAS file", type=["las", "LAS"])
    las_file, well_data = None, None

    if uploaded_file is not None:
        st.write("File Details:")
        st.write("Name:", uploaded_file.name)
        st.write("Type:", uploaded_file.type)
        st.write("Size:", uploaded_file.size, "bytes")
        las_file, well_data = load_data(uploaded_file)

        if las_file is not None:
            st.success("LAS file loaded successfully")
            st.write("Well Data:")

    return well_data

if __name__ == "__main__":
    well_data = main()
    if well_data is not None:
        well_data.reset_index(inplace=True)
        well_data.to_csv('well_data.csv', index=False)

# Define your 'plot_vshale' function here

tab_a, tab_b, tab_c = st.columns(3)
selected_tab = tab_a.radio('Select a Tab', ['Data Loading', 'Formation Evaluation', 'Visualization'])

if selected_tab == 'Data Loading':
    st.title("Data Loading Tab")
    well_df = pd.read_csv('well_data.csv')
    st.write('Logs:')
    st.write(well_df.columns)
    st.write('Statistics:')
    st.write(well_df.describe())

elif selected_tab == 'Formation Evaluation':
    st.title("Formation Evaluation Tab")
    # Add your code for this tab

elif selected_tab == 'Visualization':
    st.title("Visualization Tab")

    # Add your code for visualization here
    # Define a function for plotting different types of charts

    def plot(well_df):
        chart_type = st.selectbox('Select Chart Type', ['Line Plot', 'Scatter Plot', 'Histogram', 'Cross-plot'])

        if chart_type == 'Line Plot':
            selected_curves = st.multiselect('Select Curves', well_df.columns)
            if len(selected_curves) >= 2:
                fig, ax = plt.subplots(figsize=(6, 6))
                for curve in selected_curves:
                    ax.plot(well_df[curve], well_df['DEPTH'], label=curve)
                ax.invert_yaxis()
                ax.set_xlabel('Values')
                ax.set_ylabel('Depth (m)')
                ax.legend()
                st.pyplot(fig)
            else:
                st.warning('Select at least 2 curves for line plot.')

        elif chart_type == 'Scatter Plot':
            selected_curves = st.multiselect('Select Curves', well_df.columns)
            if len(selected_curves) == 2:
                fig, ax = plt.subplots(figsize=(6, 6))
                ax.scatter(well_df[selected_curves[0]], well_df[selected_curves[1]])
                ax.set_xlabel(selected_curves[0])
                ax.set_ylabel(selected_curves[1])
                st.pyplot(fig)
            else:
                st.warning('Select exactly 2 curves for scatter plot.')

        elif chart_type == 'Histogram':
            selected_curve = st.selectbox('Select Curve', well_df.columns)
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.hist(well_df[selected_curve], bins=20)
            ax.set_xlabel(selected_curve)
            ax.set_ylabel('Frequency')
            st.pyplot(fig)

        elif chart_type == 'Cross-plot':
            x_curve = st.selectbox('X-Axis Curve', well_df.columns)
            y_curve = st.selectbox('Y-Axis Curve', well_df.columns)
            color_curve = st.selectbox('Color Curve', well_df.columns)
            fig = px.scatter(well_df, x=x_curve, y=y_curve, color=color_curve)
            st.plotly_chart(fig)

    plot(well_df)
