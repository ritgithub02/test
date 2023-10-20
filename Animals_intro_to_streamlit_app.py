import streamlit as st
import pandas as pd
import lasio
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
import plotly.subplots
import matplotlib.pyplot as plt
from PIL import Image
import missingno as msno


well_df=None
well_data=None
las_file=None

# Other code above

def main():
    well_data = None

    return well_data


st.title('Formation Evaluation')


t1, t2, t3 = st.tabs(['Data Loading', 'Formation Evaluation', 'Visualization'])

with t1:
    # st.title("Data Loading")

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
    
    # Create a Streamlit app
    def main():
        st.title("")
    
        # Upload a LAS file
        uploaded_file = st.file_uploader("Upload a LAS file", type=["las", "LAS"])

        if uploaded_file is not None:
                st.success("LAS file loaded successfully")
                # st.write(well_data)
    
        if uploaded_file is not None:
            st.write("---------------------------------------------------------")
            st.write("File Details:")
            st.write("Name:", uploaded_file.name)
            st.write("Type:", uploaded_file.type)
            st.write("Size:", uploaded_file.size, "bytes")
            st.write("---------------------------------------------------------")
            # Call the load_data function
            las_file, well_data = load_data(uploaded_file)
    
            # if las_file is not None:
            #     st.success("LAS file loaded successfully")
            #     # st.write(well_data)
    
        # Return well_data from the main function
        return well_data
    
    # if __name__ == "__main__":
    #     well_data = main()
    #     if well_data is not None:
    #         well_data.reset_index(inplace=True)
    #         well_df = pd.DataFrame(well_data)
    #         columns=well_df.columns
    #         st.write("Well Data:")
    #         st.write(well_df)
    #         st.write("Statistics:")
    #         st.write(well_df.describe())

    # #         well_data.to_csv('io.csv')


    # # well_df= pd.read_csv('io.csv')
    # # columns=well_df.columns
    # else:
    #     st.write("Well data is None")
    







    

    def main():
        # Your main function logic here
        return well_data
    
    if __name__ == "__main__":
        try:
            well_data = main()
            if well_data is not None:
                # Your Streamlit application code that may raise errors goes here
                st.write("Result:", well_data)
        except UnboundLocalError as e:
            st.error("An error occurred: UnboundLocalError")
            # Log the actual error to the application logs for debugging
            st.exception(e)



            
            # well_data.reset_index(inplace=True)
            # well_df = pd.DataFrame(well_data)
            # columns=well_df.columns
            # st.write("Well Data:")
            # st.write(well_df)
            # st.write("Statistics:")
            # st.write(well_df.describe())
    



















with t2:
    # st.title("Formation Evaluation")
    st.markdown("Vshale Plot")
    gammaray=well_df['GR']
    # st.write('Work in Progress... .  .  .   .    .')
    # st.title("Work in Progress... .  .  .   .    .")
    c1,c2= st.columns(2)
    max_val_per = c2.text_input("Percentile for max GR:", value="95")
    min_val_per = c1.text_input("Percentile for min GR:", value="5")


    if max_val_per.replace('.', '', 1).isdigit() and min_val_per.replace('.', '', 1).isdigit():
        max_val_per = float(max_val_per)
        min_val_per = float(min_val_per)

        if 0 <= min_val_per <= 100 and 0 <= max_val_per <= 100:
            pmax = gammaray.quantile(max_val_per / 100)
            pmin = gammaray.quantile(min_val_per / 100)

            # Use the percentiles to calculate Vshale
            Igr = (gammaray - pmin) / (pmax - pmin)
            Vsh_linear=Igr
            Vsh_Larinor_older=0.33*(2**(2*Igr)-1)
            Vsh_Larinor_tertiary=0.083*(2**(3.7*Igr)-1)
            Vsh_clavier = 1.7-(3.38-(Igr + 0.7)**2)** 0.5
            
        else:
            print("Percentile values should be between 0 and 100.")
    else:
        print("Invalid input. Please enter valid percentile values (0-100).")


    vs = st.selectbox('Vshale type', ('Linear', 'Vsh_Larinor_older', 'Vsh_Larinor_tertiary', 'Vsh_clavier'))
    cold,cole=st.columns(2)
    # Define a function to plot the selected Vshale type
    def plot_vshale(vs):
        if vs == 'Linear':
            fig, ax = plt.subplots(figsize=(2, 5))
            ax.plot(Vsh_linear, well_df.DEPTH, lw=0.5, color='teal')
            ax.set_xlabel('Vsh Linear')
            ax.set_ylabel('Depth (m)')
            ax.set_xlabel('Vsh Linear', color='black', fontsize=11)
            ax.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
            ax.invert_yaxis()
            cold.pyplot(fig)
    
        elif vs == 'Vsh_Larinor_older':
            fig, ax = plt.subplots(figsize=(2, 5))
            ax.plot(Vsh_Larinor_older, well_df.DEPTH, lw=0.5, color='green')
            ax.set_xlabel('Vsh Larinor Older')
            ax.set_ylabel('Depth (m)')
            ax.set_xlabel('Vsh Larinor Older', color='green', fontsize=11)
            ax.invert_yaxis()
            ax.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
            cold.pyplot(fig)
    
        elif vs == 'Vsh_Larinor_tertiary':
            fig, ax = plt.subplots(figsize=(2, 5))
            ax.plot(Vsh_Larinor_tertiary, well_df.DEPTH, lw=0.5, color='magenta')
            ax.set_xlabel('Vsh Larinor Tertiary')
            ax.set_ylabel('Depth (m)')
            ax.set_xlabel('Vsh Larinor Tertiary', color='magenta', fontsize=14)
            ax.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
            ax.invert_yaxis()
            cold.pyplot(fig)
    
        elif vs == 'Vsh_clavier':
            fig, ax = plt.subplots(figsize=(2, 5))
            ax.plot(Vsh_clavier, well_df.DEPTH, lw=0.5, color='c')
            ax.set_xlabel('Vsh Clavier')
            ax.set_ylabel('Depth (m)')
            ax.set_xlabel('Vsh Clavier', color='c', fontsize=11)
            ax.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
            ax.invert_yaxis()
            cold.pyplot(fig)

    plot_vshale(vs)

    st.write('Work in Progress... .  .  .   .    .')




with t3:
    # st.title("Visualization")

    def plot(well_data):
        cola, colb, colc = st.columns(3)
        a = cola.radio('Plot type:',['Line','Scatter', 'Histogram', 'Cross-plot'])


        
        if a == 'Line':
            curves = colb.multiselect('Select Curves To Plot', columns)

            if len(curves) <= 1:
                colc.warning('Please select at least 2 curves.')
            else:
                curve_index = 1
                fig = make_subplots(rows=1, cols=len(curves), subplot_titles=curves, shared_yaxes=True)
                for curve in curves:
                    fig.add_trace(go.Scatter(x=well_data[curve], y=well_data['DEPTH'], mode='lines', name=curve), row=1, col=curve_index)
                    curve_index += 1
        
                fig.update_layout(height=1000, showlegend=True, yaxis={'title': 'DEPTH', 'autorange': 'reversed'})
                fig.update_layout(template='seaborn')
                st.plotly_chart(fig, use_container_width=True)

        
        
        if a == 'Scatter':
            curves = colb.multiselect('Select Curves To Plot', columns)
            
            if len(curves) <= 1:
                st.warning('Please select at least 2 curves.')
            else:
                curve_index = 1
                fig = make_subplots(rows=1, cols=len(curves), subplot_titles=curves, shared_yaxes=True)
                for curve in curves:
                    fig.add_trace(go.Scatter(x=well_data[curve], y=well_data['DEPTH']), row=1, col=curve_index)
                    curve_index += 1
    
                fig.update_layout(height=1000, showlegend=False, yaxis={'title': 'DEPTH', 'autorange': 'reversed'})
                fig.update_layout(template='seaborn')
                st.plotly_chart(fig, use_container_width=True)
                
                
        if a == 'Histogram':
            # col1_h, col2_h = st.columns(2)
            # colb.header('Op')
            hist_curve = colb.selectbox('Select a Curve', columns)
            # log_option = colb.radio('Select Linear or Logarithmic Scale', ('Linear', 'Logarithmic'))
            hist_col = colc.color_picker('Select Histogram Colour')
            # st.write('Color is ' + hist_col)
            
            # if log_option == 'Linear':
            #     log_bool = False
            # elif log_option == 'Logarithmic':
            #     log_bool = True
            # st.write(well_data)
            histogram = px.histogram(well_df, x=hist_curve, log_x=False)
            histogram.update_traces(marker_color=hist_col)
            histogram.update_layout(template='seaborn')
            st.plotly_chart(histogram, use_container_width=True)
            
        if a == 'Cross-plot':
            colb.write('')
            xplot_x = colb.selectbox('X-Axis', columns)
            xplot_x_log = colb.radio('X Axis - Linear or Logarithmic', ('Linear', 'Logarithmic'))
            if xplot_x_log == 'Linear':
                xplot_x_bool = False
            elif xplot_x_log == 'Logarithmic':
                xplot_x_bool = True
        
            colc.write('')
            xplot_y = colc.selectbox('Y-Axis', columns)  # Change 'col1' to 'col2'
            xplot_y_log = colc.radio('Y Axis - Linear or Logarithmic', ('Linear', 'Logarithmic'))  # Change 'col1' to 'col2'
            if xplot_y_log == 'Linear':
                xplot_y_bool = False
            elif xplot_y_log == 'Logarithmic':
                xplot_y_bool = True
        

            xplot_col = st.selectbox('Colour-Bar', columns)
            xplot = px.scatter(well_df, x=xplot_x, y=xplot_y, color=xplot_col, log_x=xplot_x_bool, log_y=xplot_y_bool)
            xplot.update_layout(template='seaborn')
            st.plotly_chart(xplot, use_container_width=True)
    plot(well_data)
