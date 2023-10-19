import numpy as np
import pandas as pd
import lasio  # las files
import matplotlib.pyplot as plt

import streamlit as st
import streamlit as st
import pandas as pd
import lasio



# Create file uploader object
upload_file = st.file_uploader('Upload a file for prediction', type=['csv', 'las'])
rt0 = None  # Initialize rt0 as None

# Load the uploaded file into a Pandas DataFrame
if upload_file is not None:
    file_extension = upload_file.name.split('.')[-1].lower()
    if file_extension == 'csv':
        rt0 = pd.read_csv(upload_file)
    elif file_extension == 'las':
        las_file = lasio.read(upload_file)
        rt0 = las_file.df()
    rt0 = rt0.dropna()

st.title('Data')

# Initialize selected_columns and selected_t to None
selected_columns = None
selected_t = None

# Check if rt0 is not None (file is uploaded)
if rt0 is not None:
    selected_columns = st.multiselect('Select columns to display:', rt0.columns)
    rt = rt0[selected_columns] if selected_columns else rt0

    st.write(rt.describe())

    # Header for selecting a target column
    st.header("Choose Target")
    selected_t = st.selectbox("Select a Target", rt.columns)
    button6 = st.button("Submit")



































# import streamlit as st
# import pandas as pd
# import lasio
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go
# import plotly.express as px
# import numpy as np
# import plotly.subplots
# import matplotlib.pyplot as plt
# from PIL import Image
# import missingno as msno







# # ------------------------------------------------

# # Create file uploader object
# upload_file = st.file_uploader('Upload a file for prediction', type=['csv'])
# rt0 = None  # Initialize rt0 as None

# # Load the CSV file into a Pandas DataFrame
# if upload_file is not None:
#     well_data = pd.read_csv(upload_file)
#     well_df = well_data.df()
#     well_df=well_df.dropna()
#     well_df=well_df.reset_index()
#     columns= well_df.columns



# # --------------------------------------------------------------------


























# st.title('Formation Evaluation')
# image = Image.open("psd1.jpg")
# st.image(image, caption="", use_column_width=True)





# las_file_path = "Gorgonichthys_1_suite3_supercombo_log.las"
# well_data = lasio.read(las_file_path)
# # columns = well_data.keys()

# well_df = well_data.df()
# well_df=well_df.reset_index()

# columns= well_df.columns


# tab_a,tab_b, tab_c =st.tabs(['Data Loading', 'Formation Evaluation', 'Visualization' ])

# with tab_a:



#     st.subheader("Upload LAS File")
#     uploaded_file = st.file_uploader("Upload a LAS file", type=["las", "LAS"])
#     def display_las_data(uploaded_file):
#         if uploaded_file is not None:
#             las_data = lasio.read(uploaded_file)
#             st.header("LAS Header")
#             st.write(las_data.header)
    
#             st.header("LAS Data")
#             st.write(las_data.df())
    
#     # Check if a file has been uploaded
#     if uploaded_file:
#         display_las_data(uploaded_file)
#     else:
#         st.info("Please upload a LAS file.")
#     # st.write('Missing Ranges :')
#     # # st.write(msno.matrix(well_df))
#     # st.pyplot(msno.matrix(well_df))
    
#     st.write('Logs:')
#     st.write(well_df.columns)
#     st.write('Statistics:')
#     st.write(well_df.describe())

# if 'DEPTH' not in well_df.columns:
#     well_df['DEPTH'] = well_data['DEPTH']
#     # st.write(columns)



# with tab_b:
#     st.title("Vshale Plot")
#     gammaray=well_df['GR']
#     # st.write('Work in Progress... .  .  .   .    .')
#     # st.title("Work in Progress... .  .  .   .    .")
#     c1,c2= st.columns(2)
#     max_val_per = c2.text_input("Percentile for max GR:", value="95")
#     min_val_per = c1.text_input("Percentile for min GR:", value="5")


#     if max_val_per.replace('.', '', 1).isdigit() and min_val_per.replace('.', '', 1).isdigit():
#         max_val_per = float(max_val_per)
#         min_val_per = float(min_val_per)

#         if 0 <= min_val_per <= 100 and 0 <= max_val_per <= 100:
#             pmax = gammaray.quantile(max_val_per / 100)
#             pmin = gammaray.quantile(min_val_per / 100)

#             # Use the percentiles to calculate Vshale
#             Igr = (gammaray - pmin) / (pmax - pmin)
#             Vsh_linear=Igr
#             Vsh_Larinor_older=0.33*(2**(2*Igr)-1)
#             Vsh_Larinor_tertiary=0.083*(2**(3.7*Igr)-1)
#             Vsh_clavier = 1.7-(3.38-(Igr + 0.7)**2)** 0.5
            
#         else:
#             print("Percentile values should be between 0 and 100.")
#     else:
#         print("Invalid input. Please enter valid percentile values (0-100).")


    
#     # Create a selectbox for choosing the Vshale type
#     vs = st.selectbox('Vshale type', ('Linear', 'Vsh_Larinor_older', 'Vsh_Larinor_tertiary', 'Vsh_clavier'))
#     cold,cole=st.columns(2)
#     # Define a function to plot the selected Vshale type
#     def plot_vshale(vs):
#         if vs == 'Linear':
#             fig, ax = plt.subplots(figsize=(2, 5))
#             ax.plot(Vsh_linear, well_df.DEPTH, lw=0.5, color='teal')
#             ax.set_xlabel('Vsh Linear')
#             ax.set_ylabel('Depth (m)')
#             ax.set_xlabel('Vsh Linear', color='black', fontsize=11)
#             ax.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
#             ax.invert_yaxis()
#             cold.pyplot(fig)
    
#         elif vs == 'Vsh_Larinor_older':
#             fig, ax = plt.subplots(figsize=(2, 5))
#             ax.plot(Vsh_Larinor_older, well_df.DEPTH, lw=0.5, color='green')
#             ax.set_xlabel('Vsh Larinor Older')
#             ax.set_ylabel('Depth (m)')
#             ax.set_xlabel('Vsh Larinor Older', color='green', fontsize=11)
#             ax.invert_yaxis()
#             ax.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
#             cold.pyplot(fig)
    
#         elif vs == 'Vsh_Larinor_tertiary':
#             fig, ax = plt.subplots(figsize=(2, 5))
#             ax.plot(Vsh_Larinor_tertiary, well_df.DEPTH, lw=0.5, color='magenta')
#             ax.set_xlabel('Vsh Larinor Tertiary')
#             ax.set_ylabel('Depth (m)')
#             ax.set_xlabel('Vsh Larinor Tertiary', color='magenta', fontsize=14)
#             ax.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
#             ax.invert_yaxis()
#             cold.pyplot(fig)
    
#         elif vs == 'Vsh_clavier':
#             fig, ax = plt.subplots(figsize=(2, 5))
#             ax.plot(Vsh_clavier, well_df.DEPTH, lw=0.5, color='c')
#             ax.set_xlabel('Vsh Clavier')
#             ax.set_ylabel('Depth (m)')
#             ax.set_xlabel('Vsh Clavier', color='c', fontsize=11)
#             ax.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
#             ax.invert_yaxis()
#             cold.pyplot(fig)
    
#     # Call the function to display the selected plot
#     plot_vshale(vs)

#     st.write('Work in Progress... .  .  .   .    .')





































# with tab_c:
#     def plot(well_data):
#         cola, colb, colc = st.columns(3)
#         a = cola.radio('Plot type:',['Line','Scatter', 'Histogram', 'Cross-plot'])


        
#         if a == 'Line':
#             curves = st.multiselect('Select Curves To Plot', columns)

#             if len(curves) <= 1:
#                 st.warning('Please select at least 2 curves.')
#             else:
#                 curve_index = 1
#                 fig = make_subplots(rows=1, cols=len(curves), subplot_titles=curves, shared_yaxes=True)
#                 for curve in curves:
#                     fig.add_trace(go.Scatter(x=well_data[curve], y=well_data['DEPTH'], mode='lines', name=curve), row=1, col=curve_index)
#                     curve_index += 1
        
#                 fig.update_layout(height=1000, showlegend=True, yaxis={'title': 'DEPTH', 'autorange': 'reversed'})
#                 fig.update_layout(template='seaborn')
#                 st.plotly_chart(fig, use_container_width=True)

        
        
#         if a == 'Scatter':
#             curves = colb.multiselect('Select Curves To Plot', columns)
            
#             if len(curves) <= 1:
#                 st.warning('Please select at least 2 curves.')
#             else:
#                 curve_index = 1
#                 fig = make_subplots(rows=1, cols=len(curves), subplot_titles=curves, shared_yaxes=True)
#                 for curve in curves:
#                     fig.add_trace(go.Scatter(x=well_data[curve], y=well_data['DEPTH']), row=1, col=curve_index)
#                     curve_index += 1
    
#                 fig.update_layout(height=1000, showlegend=False, yaxis={'title': 'DEPTH', 'autorange': 'reversed'})
#                 fig.update_layout(template='seaborn')
#                 st.plotly_chart(fig, use_container_width=True)
                
                
#         if a == 'Histogram':
#             # col1_h, col2_h = st.columns(2)
#             # colb.header('Op')
#             hist_curve = colb.selectbox('Select a Curve', columns)
#             log_option = colb.radio('Select Linear or Logarithmic Scale', ('Linear', 'Logarithmic'))
#             hist_col = colc.color_picker('Select Histogram Colour')
#             # st.write('Color is ' + hist_col)
            
#             if log_option == 'Linear':
#                 log_bool = False
#             elif log_option == 'Logarithmic':
#                 log_bool = True
#             st.write(well_data)
#             histogram = px.histogram(well_df, x=hist_curve, log_x=log_bool)
#             histogram.update_traces(marker_color=hist_col)
#             histogram.update_layout(template='seaborn')
#             st.plotly_chart(histogram, use_container_width=True)
            
#         if a == 'Cross-plot':
#             colb.write('')
#             xplot_x = colb.selectbox('X-Axis', columns)
#             xplot_x_log = colb.radio('X Axis - Linear or Logarithmic', ('Linear', 'Logarithmic'))
#             if xplot_x_log == 'Linear':
#                 xplot_x_bool = False
#             elif xplot_x_log == 'Logarithmic':
#                 xplot_x_bool = True
        
#             colc.write('')
#             xplot_y = colc.selectbox('Y-Axis', columns)  # Change 'col1' to 'col2'
#             xplot_y_log = colc.radio('Y Axis - Linear or Logarithmic', ('Linear', 'Logarithmic'))  # Change 'col1' to 'col2'
#             if xplot_y_log == 'Linear':
#                 xplot_y_bool = False
#             elif xplot_y_log == 'Logarithmic':
#                 xplot_y_bool = True
        

#             xplot_col = st.selectbox('Colour-Bar', columns)
#             xplot = px.scatter(well_df, x=xplot_x, y=xplot_y, color=xplot_col, log_x=xplot_x_bool, log_y=xplot_y_bool)
#             xplot.update_layout(template='seaborn')
#             st.plotly_chart(xplot, use_container_width=True)

# # Ensure 'xplot_col' is defined outside of the 'if' block if needed elsewhere in your code.


#     plot(well_data)
