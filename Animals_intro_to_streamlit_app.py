pip install --upgrade streamlit

import numpy as np
import pandas as pd
import lasio
import matplotlib.pyplot as plt
import streamlit as st
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

# Define the global variables for the DataFrame and column names
well_df = None
columns = []

# Function to load data from an uploaded LAS file
def load_data(uploadedfile):
    if uploadedfile:
        uploadedfile.seek(0)
        string = uploadedfile.read().decode()
        las_file = lasio.read(string)
        well_data = las_file.df()
        return well_data
    else:
        return None

# Streamlit app
def main():
    global well_df, columns
    st.title("LAS File Viewer")

    uploaded_file = st.file_uploader("Upload a LAS file", type=["las", "LAS"])

    if uploaded_file is not None:
        well_data = load_data(uploaded_file)
        if well_data is not None:
            well_df = well_data
            columns = well_df.columns

            st.success("LAS file loaded successfully")
            st.write("Well Data:")
            st.write(well_df)

if __name__ == "__main__":
    main()

# Streamlit tabs
selected_tab = st.radio("Select a tab:", ["Data Loading", "Formation Evaluation", "Visualization"])

if selected_tab == "Data Loading":
    st.title("Data Loading Tab")
    
    if well_df is not None:
        st.write("Logs:")
        st.write(columns)
        st.write("Statistics:")
        st.write(well_df.describe())
elif selected_tab == "Formation Evaluation":
    st.title("Formation Evaluation Tab")
    # Add your content for this tab here
    st.write("Work in Progress... .  .  .   .    .")
elif selected_tab == "Visualization":
    st.title("Visualization Tab")
    
    if well_df is not None:
        st.title("Vshale Plot")
        gammaray = well_df['GR']
        c1, c2 = st.columns(2)
        max_val_per = c2.text_input("Percentile for max GR:", value="95")
        min_val_per = c1.text_input("Percentile for min GR:", value="5")

        if max_val_per.replace('.', '', 1).isdigit() and min_val_per.replace('.', '', 1).isdigit():
            max_val_per = float(max_val_per)
            min_val_per = float(min_val_per)

            if 0 <= min_val_per <= 100 and 0 <= max_val_per <= 100:
                pmax = gammaray.quantile(max_val_per / 100)
                pmin = gammaray.quantile(min_val_per / 100)
                Igr = (gammaray - pmin) / (pmax - pmin)
                Vsh_linear = Igr
                Vsh_Larinor_older = 0.33 * (2 ** (2 * Igr) - 1)
                Vsh_Larinor_tertiary = 0.083 * (2 ** (3.7 * Igr) - 1)
                Vsh_clavier = 1.7 - (3.38 - (Igr + 0.7) ** 2) ** 0.5
            else:
                st.error("Percentile values should be between 0 and 100.")
        else:
            st.error("Invalid input. Please enter valid percentile values (0-100).")

        vs = st.selectbox('Vshale type', ['Linear', 'Vsh_Larinor_older', 'Vsh_Larinor_tertiary', 'Vsh_clavier'])
        cold, cole = st.columns(2)

        def plot_vshale(vs):
            if vs == 'Linear':
                fig, ax = plt.subplots(figsize=(2, 5))
                ax.plot(Vsh_linear, well_df['DEPTH'], lw=0.5, color='teal')
                ax.set_xlabel('Vsh Linear')
                ax.set_ylabel('Depth (m)')
                ax.set_xlabel('Vsh Linear', color='black', fontsize=11)
                ax.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
                ax.invert_yaxis()
                cold.pyplot(fig)
            # Add other Vshale plot types here

        plot_vshale(vs)

        st.write('Work in Progress... .  .  .   .    .')


elif selected_tab == "Visualization":
    st.title("Visualization Tab")

    if well_df is not None:
        # Function to plot different types of charts
        def plot(well_df):
            cola, colb, colc = st.columns(3)
            a = cola.radio('Plot type:', ['Line', 'Scatter', 'Histogram', 'Cross-plot'])

            if a == 'Line':
                curves = st.multiselect('Select Curves To Plot', columns)

                if len(curves) <= 1:
                    st.warning('Please select at least 2 curves.')
                else:
                    curve_index = 1
                    fig = make_subplots(rows=1, cols=len(curves), subplot_titles=curves, shared_yaxes=True)
                    for curve in curves:
                        fig.add_trace(go.Scatter(x=well_df[curve], y=well_df['DEPTH'], mode='lines', name=curve), row=1, col=curve_index)
                        curve_index += 1

                    fig.update_layout(height=1000, showlegend=True, yaxis={'title': 'DEPTH', 'autorange': 'reversed'})
                    fig.update_layout(template='seaborn')
                    st.plotly_chart(fig, use_container_width=True)

            elif a == 'Scatter':
                curves = colb.multiselect('Select Curves To Plot', columns)

                if len(curves) <= 1:
                    st.warning('Please select at least 2 curves.')
                else:
                    curve_index = 1
                    fig = make_subplots(rows=1, cols=len(curves), subplot_titles=curves, shared_yaxes=True)
                    for curve in curves:
                        fig.add_trace(go.Scatter(x=well_df[curve], y=well_df['DEPTH']), row=1, col=curve_index)
                        curve_index += 1

                    fig.update_layout(height=1000, showlegend=False, yaxis={'title': 'DEPTH', 'autorange': 'reversed'})
                    fig.update_layout(template='seaborn')
                    st.plotly_chart(fig, use_container_width=True)

            elif a == 'Histogram':
                hist_curve = colb.selectbox('Select a Curve', columns)
                log_option = colb.radio('Select Linear or Logarithmic Scale', ('Linear', 'Logarithmic'))
                hist_col = colc.color_picker('Select Histogram Colour')

                if log_option == 'Linear':
                    log_bool = False
                elif log_option == 'Logarithmic':
                    log_bool = True

                histogram = px.histogram(well_df, x=hist_curve, log_x=log_bool)
                histogram.update_traces(marker_color=hist_col)
                histogram.update_layout(template='seaborn')
                st.plotly_chart(histogram, use_container_width=True)

            elif a == 'Cross-plot':
                xplot_x = colb.selectbox('X-Axis', columns)
                xplot_x_log = colb.radio('X Axis - Linear or Logarithmic', ('Linear', 'Logarithmic'))
                if xplot_x_log == 'Linear':
                    xplot_x_bool = False
                elif xplot_x_log == 'Logarithmic':
                    xplot_x_bool = True

                xplot_y = colc.selectbox('Y-Axis', columns)
                xplot_y_log = colc.radio('Y Axis - Linear or Logarithmic', ('Linear', 'Logarithmic'))
                if xplot_y_log == 'Linear':
                    xplot_y_bool = False
                elif xplot_y_log == 'Logarithmic':
                    xplot_y_bool = True

                xplot_col = st.selectbox('Colour-Bar', columns)
                xplot = px.scatter(well_df, x=xplot_x, y=xplot_y, color=xplot_col, log_x=xplot_x_bool, log_y=xplot_y_bool)
                xplot.update_layout(template='seaborn')
                st.plotly_chart(xplot, use_container_width=True)

        plot(well_df)
