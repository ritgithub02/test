import streamlit as st
import plotly.graph_objects as go
import plotly.subplots as sp
import streamlit.components.v1 as components
import pandas as pd
from plotly.subplots import make_subplots
import lasio 
import zipfile
import tarfile
import io
import os
from sklearn.linear_model import LinearRegression
import plotly.express as px
import numpy as np
import plotly.subplots
import matplotlib.pyplot as plt
from PIL import Image
import missingno as msno
import requests
from io import BytesIO
# import welly
# import welly.quality as wq
# import seaborn as sns
from tempfile import NamedTemporaryFile
import tempfile
# from fpdf import FPDF  
import itertools
import openpyxl
import random
import pandas as pd
import numpy as np
# Machine learning libraries
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale
from sklearn.decomposition import FactorAnalysis
from sklearn.cluster import KMeans
# Visualization libraries
# import seaborn as sns
# import matplotlib as mpl
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from sklearn.preprocessing import scale
from plotly_click_show import plotly_events
import time
start_time = time.time()







# st.set_page_config(
#     page_title="PetroHarrit",
#     page_icon="🌏",
#     layout="wide",
#     initial_sidebar_state='collapsed'
# )






# if 'button' not in st.session_state:
#     st.session_state.button = False


# sta = 'collapsed' if st.session_state.button else 'expanded'

st.set_page_config(
    page_title="PetroHarrit",
    page_icon="🌏",
    layout="wide",
    initial_sidebar_state='expanded'
)



# def toggle():
#     st.session_state.button = not st.session_state.button

# st.button("Toggle Sidebar", on_click=toggle)




## web---------------*

def clone_github_repository(github_repo_url, destination_directory):
    # Get the repository name from the URL
    repository_name = github_repo_url.split('/')[-1]

    # Check if the destination directory exists, and create it if not
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    # Download the repository as a zip archive
    zip_url = f'{github_repo_url}/archive/main.zip'
    response = requests.get(zip_url)
    if response.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(response.content), 'r') as zip_ref:
            zip_ref.extractall(destination_directory)
        print(f'Repository cloned to {destination_directory}/{repository_name}')
    else:
        print(f'Failed to download the repository. Status code: {response.status_code}')


git_url = 'https://github.com/ritgithub02/pfiles'
dest_dir = "files"
clone_github_repository(git_url, dest_dir)






# github_repo_url = 'https://github.com/ritgithub02/pd_f'
# destination_directory = "exp"
# clone_github_repository(github_repo_url, destination_directory)

# _component_func = components.declare_component(
#     "plotly1",
#     path="./exp/pd_f-main"
# )


# def plotly_events(fig: go.Figure):
#     spec = fig.to_json()
#     component_value = _component_func(spec=spec, default=None)
#     return component_value





def display_image_from_url(image_url,pos):
    response = requests.get(image_url)
    
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        pos.image(image, caption='')
    else:
        pos.write(f"Failed to fetch the image. Status code: {response.status_code}")

display_image_from_url("https://raw.githubusercontent.com/ritgithub02/data/main/dhippng.png",st)

pt1,pt2,pt3=st.columns(3)
display_image_from_url("https://raw.githubusercontent.com/ritgithub02/data/main/output-onlinepngtools.png",pt1)



# def create_linkedIn_profile_link(profile_url, image_url):
#     markdown_text = f'<a href="{profile_url}"><img src="{image_url}" alt="LinkedIn Profile" width=30 height=30></a>'
#     return markdown_text
# def create_gmail_profile_link(profile_email, image_url):
#     markdown_text = f'<a href="mailto:{profile_email}"><img src="{image_url}" alt="Gmail Profile" width=35 height=25></a>'
#     return markdown_text


# lin="https://raw.githubusercontent.com/ritgithub02/data/main/LinkedIn_icon_circle.svg.png"
# gml="https://raw.githubusercontent.com/ritgithub02/data/main/download%20(1).png"


## -------------------------*

# #  local-------------*



# #@st.cache_data(experimental_allow_widgets=True)
# def plotly_events(fig: go.Figure):
#     spec = fig.to_json()
#     component_value = _component_func(spec=spec, default=None)
#     return component_value

# # Declare the custom component
# _component_func = components.declare_component(
#     "plotly1",
#     path="./plotly1"
# )


# def display_image_from_loc(file_location, pos):
#     try:
#         image = Image.open(file_location)
#         pos.image(image, caption='')
#     except Exception as e:
#         st.write(f"Failed to open the image. Error: {str(e)}")

# display_image_from_loc("./files/img/ship.png", st)

# pt1,pt2,pt3=st.columns(3)
# display_image_from_loc("./files/img/petroharrit.png", pt1)


# def create_linkedIn_profile_link(profile_url, image_location):
#     image_url = st.image(image_location, width=30, caption="LinkedIn Profile Image")
#     markdown_text = f'<a href="{profile_url}">{image_url}</a>'
#     return markdown_text

# def create_gmail_profile_link(profile_email, image_location):
#     image_url = st.image(image_location, width=35, caption="Gmail Profile Image")
#     markdown_text = f'<a href="mailto:{profile_email}">{image_url}</a>'
#     return markdown_text


# lin="./files/img/linkd.png"
# gml="./files/img/gmail_icon.png"

# #-----------------------------*
# ---------------------------------------------------------------------------------LOADING-------

css = """
<style>
.stTabs {
  width: 100%;
  margin-bottom: 2rem;
}

.stTabs [data-baseweb="tab-list"] {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem 1.5rem;
  background-color: #f8f9fa;
  border-radius: 0.5rem;
}

.stTabs [data-baseweb="tab-list"] button {
  font-size: 2rem;
  padding: 0.5rem 1rem;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 0.5rem;
  cursor: pointer;
  transition: all 0.3s ease-in-out;
}

.stTabs [data-baseweb="tab-list"] button:hover,
.stTabs [data-baseweb="tab-list"] button:active,
.stTabs [data-baseweb="tab-list"] button.is-selected {
  background-color: #f0f0f0;
  border-color: #ccc;
}

.stTabs [data-baseweb="tab-pane"] {
  padding: 2rem 1.5rem;
  border-radius: 0.5rem;
  background-color: #fff;
}
</style>
"""

st.markdown(css, unsafe_allow_html=True)

t1, t2, t3 = st.tabs(['Data Loading', 'Basic Visualization' ,'Formation Evaluation with Visulization'])

def curvename(df_unit,column_names):
    column_units = []
    for name in column_names:
        selected_rows = df_unit[df_unit[0] == name]
        column_units.append(str(selected_rows[1].iloc[0]))
        curve_name=[]
    for i in range(len(column_names)):
        s=column_names[i]+" ("+column_units[i]+")"
        curve_name.append(s)
    return curve_name
def unitchanger(df_unit,column_name,new_unit):
    df_unit.loc[df_unit[0] == column_name,1]=new_unit
    return df_unit

def unitshower(df_unit,column_name):
    selected_row = df_unit[df_unit[0] == column_name]
    column_unit=str(selected_row[1].iloc[0])
    return column_unit

def unitadder(df_unit,colunm_name,unit):
    df_unit.loc[len(df_unit)] = [colunm_name,unit]
    return df_unit

def convert_units(log_name, factor, unit):
    if unit == "Multiply":
        return well_df[log_name] * factor
    elif unit == "Divide":
        return well_df[log_name] / factor
    return well_df[log_name]  # If no conversion is selected
            
#--------------Mneomenic file ----------------------------#

# Make sure file should be in same folder or in place as the streamlit_app

# dfMN = pd.read_excel('Mnemonics_of_logdata.xlsx')
dfMN = pd.read_excel("./files/pfiles-main/Mnemonics_of_logdata.xlsx")

# ----------------------------------------------------------------------------------TAB 1--

####################################################################################
#                             Loading the data                                     #
####################################################################################
with t1:
    lsf,fmf,cmf=st.columns(3)

    lsf.subheader('Las File')
    file = lsf.file_uploader('Upload the LAS file')
    dfle=st.checkbox('Use demo file')

    # with st.spinner('Wait for it...'):
    #     time.sleep(time.time() - start_time)
    # wait for it 
    if file is not None and (file.name.lower().endswith('.las') or file.name.lower().endswith('.LAS')):
    # if file is not None:
        
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(file.read())
        las_file = lasio.read(tfile.name,engine='normal')


        if las_file is not None:
            lsf.success('Las File Uploaded Successfully')
        else:            
            lsf.warning('Warning message')

        
        # well = welly.Well.from_lasio(las_file)
        
        df1=las_file.df()
        df1.reset_index(inplace=True)
        
        well_data=las_file.df()
        well_data.reset_index(inplace=True)
        well_df = pd.DataFrame(well_data)



        datau = []
        for curve in las_file.curves:
            unit = curve.unit
            xx=curve.mnemonic
            datau.append([xx,unit])
        df_unit = pd.DataFrame(datau)



        st.sidebar.subheader('Depth Selction')
    
        default_column1 = 'DEPTH' if 'DEPTH' in well_df.columns else ('DEPT' if 'DEPT' in well_df.columns else well_df.columns[1])

        
        deps = st.sidebar.selectbox("DEPTH log",well_df.columns, index=well_df.columns.get_loc(default_column1))

        well_df.rename(columns={deps: 'DEPTH'}, inplace=True)
        unitadder(df_unit,'DEPTH',las_file.curves[0].unit)


       
        min_depth = st.sidebar.text_input('Enter Minimum Depth', well_df['DEPTH'].min())
        max_depth = st.sidebar.text_input('Enter Maximum Depth', well_df['DEPTH'].max())
        
        min_depth = float(min_depth)
        max_depth = float(max_depth)
        
        well_df = well_df[(well_df['DEPTH'] >= min_depth) & (well_df['DEPTH'] <= max_depth)]
        st.title("")
        st.subheader("LAS File Header Information")
        with st.expander("Curves Information"):
            header_info = las_file.header

            
            for key, value in header_info.items():
                st.write(f"{key}: {value}")
            
            if 'well' in header_info:
                st.subheader("Well Information")
                well_info = header_info['well']
                for key, value in well_info.items():
                    st.write(f"{key}: {value}")
            
            if 'curves' in header_info:
                st.subheader("Curves Information")
                curves_info = header_info['curves']
                for curve in curves_info:
                    st.write(f"Curve Name: {curve['mnemonic']}")
                    st.write(f"Unit: {curve['unit']}")
                    st.write(f"Description: {curve['descr']}")
                    st.write(f"API Code: {curve['API_code']}")
                    st.title("")
                    st.title("")
        st.title("")        
        st.subheader("Well Log Unit Conversion")
        with st.expander('Unit Conversion'):

            
            selected_logs = st.multiselect("Select logs for conversion", well_df.columns)
            
            if selected_logs:
                conversion_factors = {}
            
                for log in selected_logs:
                    aal,laa,al,la= st.columns([0.5,1,1,1])
                    aal.subheader(unitshower(df_unit,log) + '       to')
                    new_unit=laa.text_input(' Enter the new unit: ',key=f"{log}_factor1")
                    factor = al.number_input(f"Enter conversion factor for {log}", value=1.0, key=f"{log}_factor")
                    unit = la.selectbox("Select conversion method", ["Multiply", "Divide", "None"], key=f"{log}_unit")
                    conversion_factors[log] = (factor, unit)
                    if st.checkbox('Convert '+ log):
                        # st."Converted Well Data")
                        well_df[log] = convert_units(log, factor, unit)
                        unitchanger(df_unit,log,new_unit)
                        # st.write(well_df)
                    else:
                        st.write('Unit Convesion has to be done')





    


        
        columns = well_df.columns
        st.title("")
        with lsf.expander("View Data"):
            st.write(well_df)
        st.subheader("Well Data:")
        with st.expander("View"):
            st.write(well_df)
            # st.title("")
        st.title("")
        st.subheader("Statistics:")
        with st.expander("View"):
            st.write(well_df.describe())


    elif dfle:
        def gorg():
            file_l = "./files/pfiles-main/Gorgonichthys_1_suite3_supercombo_log.las"
            las_file = lasio.read(file_l)
            # well = welly.Well.from_lasio(las_file)
            df1=las_file.df()
            df1.reset_index(inplace=True)
            well_data=las_file.df()
            well_data.reset_index(inplace=True)
            well_df = pd.DataFrame(well_data)
            # return las_file,file_l,well, well_data, well_df
            return las_file,file_l, well_data, well_df
        # las_file,file_l,well, well_data, well_df = gorg()
        las_file,file_l, well_data, well_df = gorg()
           

        datau = []
        for curve in las_file.curves:
            unit = curve.unit
            xx=curve.mnemonic
            datau.append([xx,unit])
        df_unit = pd.DataFrame(datau)





        st.sidebar.subheader('Depth Selction')
    
        default_column1 = 'DEPTH' if 'DEPTH' in well_df.columns else ('DEPT' if 'DEPT' in well_df.columns else well_df.columns[1])
        
        
        deps = st.sidebar.selectbox("DEPTH log",well_df.columns, index=well_df.columns.get_loc(default_column1))

        well_df.rename(columns={deps: 'DEPTH'}, inplace=True)

       
        min_depth = st.sidebar.text_input('Enter Minimum Depth', well_df['DEPTH'].min())
        max_depth = st.sidebar.text_input('Enter Maximum Depth', well_df['DEPTH'].max())
        
        min_depth = float(min_depth)
        max_depth = float(max_depth)
        
        well_df = well_df[(well_df['DEPTH'] >= min_depth) & (well_df['DEPTH'] <= max_depth)]
        # st.write(filtered_df)
        st.title("")
        st.subheader("LAS File Header Information")
        with st.expander("Curves Information"):
            header_info = las_file.header
            # st.title("")
            
            for key, value in header_info.items():
                st.write(f"{key}: {value}")
            
            if 'well' in header_info:
                st.subheader("Well Information")
                well_info = header_info['well']
                for key, value in well_info.items():
                    st.write(f"{key}: {value}")
            
            if 'curves' in header_info:
                st.subheader("Curves Information")
                curves_info = header_info['curves']
                for curve in curves_info:
                    st.write(f"Curve Name: {curve['mnemonic']}")
                    st.write(f"Unit: {curve['unit']}")
                    st.write(f"Description: {curve['descr']}")
                    st.write(f"API Code: {curve['API_code']}")
                    st.title("")
                    st.title("")
        st.title("")        
        st.subheader("Well Log Unit Conversion")
        with st.expander('Unit Conversion'):


            selected_logs = st.multiselect("Select logs for conversion", well_df.columns)
            
            if selected_logs:
                conversion_factors = {}
            
                for log in selected_logs:
                    aal,laa,al,la= st.columns([0.5,1,1,1])
                    aal.subheader(unitshower(df_unit,log) + '       to')
                    new_unit=laa.text_input(' Enter the new unit: ',key=f"{log}_factor1")
                    factor = al.number_input(f"Enter conversion factor for {log}", value=1.0, key=f"{log}_factor")
                    unit = la.selectbox("Select conversion method", ["Multiply", "Divide", "None"], key=f"{log}_unit")
                    conversion_factors[log] = (factor, unit)
                    if st.checkbox('Convert '+ log):
                        # st."Converted Well Data")
                        well_df[log] = convert_units(log, factor, unit)
                        unitchanger(df_unit,log,new_unit)
                        # st.write(well_df)
                    else:
                        st.write('Unit Convesion has to be done')





    


        
        columns = well_df.columns
        st.title("")
        with lsf.expander("View Data"):
            st.write(well_df)
        st.subheader("Well Data:")
        with st.expander("View"):
            st.write(well_df)
            # st.title("")
        st.title("")
        st.subheader("Statistics:")
        with st.expander("View"):
            st.write(well_df.describe())




    else:
        lsf.error('LAS File Upload is Required')













        
        
    st.sidebar.header('')
    st.sidebar.header('')








    with st.sidebar.expander('Our motive'):
        st.markdown("Welcome to PetroHarrit \n\nThank you for exploring our interface created by IITISM students for a petrophysical analysis and visualization assignment. PetroHarrit offers an interactive platform for comprehensive analysis, providing a range of features for your petrophysical needs. \n\nStay tuned for our upcoming user manual to guide you through the functionalities. We're continually working on adding more features to enhance your experience. We hope you find PetroHarrit valuable for your work. Your feedback is important to us as we strive to improve and bring you the latest updates. \n\nEnjoy your analysis journey with PetroHarrit!")
        st.markdown('Thanks:')
        st.markdown("[WAPIMS](https://wapims.dmp.wa.gov.au/WAPIMS/)", unsafe_allow_html=True)
        st.markdown('For demo data, including LAS files, formation top data, and core data')



    with st.sidebar.expander('About us'):
        st.write("For queries:")
        aun1,aun2=st.columns(2)
        lg1,lg2,lg3,lg4,lg5,lg6=st.columns(6)

        aun1.markdown("[Harsh Prajapati](https://www.linkedin.com/in/harsh-prajapati-682b63287/)", unsafe_allow_html=True)
        
        aun2.markdown("[Ritesh Gond](https://www.linkedin.com/in/ritesh-gond-bb853928b/)", unsafe_allow_html=True)


        lg1.markdown("[📧](mailto:22mc0044@iitism.ac.in)", unsafe_allow_html=True)
        lg4.markdown("[📧](mailto:rgaur7052@gmail.com)", unsafe_allow_html=True)



        lg2.markdown("[🔗](https://www.linkedin.com/in/harsh-prajapati-682b63287/)", unsafe_allow_html=True)
        lg5.markdown("[🔗](https://www.linkedin.com/in/ritesh-gond-bb853928b/)", unsafe_allow_html=True)

        ## for now
        # profile1 = "https://www.linkedin.com/in/harsh-prajapati-682b63287/"
        # markdown_text = create_linkedIn_profile_link(profile1, lin)
        # lg1.markdown(markdown_text, unsafe_allow_html=True)


        # profile2 = "https://www.linkedin.com/in/ritesh-gond-bb853928b/"
        # markdown_text = create_linkedIn_profile_link(profile2, lin)
        # lg4.markdown(markdown_text, unsafe_allow_html=True)


        # profile3 = "22mc0041@iitism.ac.in"
        # markdown_text = create_gmail_profile_link(profile3,gml)
        # lg2.markdown(markdown_text, unsafe_allow_html=True)



        # profile4 = "22mc0071@iitism.ac.in"
        # markdown_text = create_gmail_profile_link(profile4,gml)
        # lg5.markdown(markdown_text, unsafe_allow_html=True)



        st.markdown("")
        st.markdown("Under guidence of:")

        st.markdown("[Dr. Partha Pratim Mandal](https://iitism.irins.org/profile/328364)", unsafe_allow_html=True)
        st.markdown("[Founder of SRCG](https://www.linkedin.com/company/subsurface-resource-charecterization-lab-iit-ism-dhanbad/)", unsafe_allow_html=True)



        st.write("Assistant Professor  \nDepartment of Applied Geophysics  \nIIT(ISM) Dhanbad")

        # lg01,lg02,lg03,lg04,lg05,lg06=st.columns(6)
        qlg1,qlg2,qlg3,qlg4,qlg5,qlg6=st.columns(6)


        qlg2.markdown("[🔗](https://www.linkedin.com/in/ppmcurtin/)", unsafe_allow_html=True)
        qlg1.markdown("[📧](mailto:partham@iitism.ac.in)", unsafe_allow_html=True)




    with st.sidebar.expander("Merge and Edit LAS Files"):
        st.markdown("""
        *Note:* This app currently supports processing a single LAS file as input. If you need to work with multiple LAS files,
        you can use the following link to merge and edit them:

        [LAS File Merge and Edit App](https://lasmastereditor.streamlit.app/)

        Additionally, if your calculations require a subset of logs, consider reducing the number of logs to speed up the process.
        """)


    # with st.sidebar.expander('Download exe version'):

    #     st.markdown('[Download](https://drive.google.com/drive/folders/1x84JjnHposE5fy1Cav8wB0OpofzSF4oO?usp=sharing)')

        ## for now
        # profile9 = "https://www.linkedin.com/in/ppmcurtin/"
        # markdown_text = create_linkedIn_profile_link(profile9, lin)
        # qlg1.markdown(markdown_text, unsafe_allow_html=True)

        # profile10 = "partham@iitism.ac.in"
        # markdown_text = create_gmail_profile_link(profile10,gml)
        # qlg2.markdown(markdown_text, unsafe_allow_html=True)

        
    fmf.subheader('Formation Tops')
    with fmf.expander("Upload"):
        uploaded_file1 = st.file_uploader("Upload a CSV or XLSX file ", type=["csv", "xlsx"])
        dftfc = st.checkbox('Use demo file ')
        if uploaded_file1 is not None and (uploaded_file1.name.lower().endswith('.xlsx') or uploaded_file1.name.lower().endswith('.csv')):
            if uploaded_file1.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                f_df = pd.read_excel(uploaded_file1, engine="openpyxl")
            else:
                f_df = pd.read_csv(uploaded_file1)
            st.success('File Uploaded Successfully')
    
            st.write("Dataset:")
            st.write(f_df)
        elif dftfc:
            file_f = "./files/pfiles-main/Grid Export.xlsx"
            f_df = pd.read_excel(file_f, engine="openpyxl")
            st.success('File Uploaded Successfully')
    
            st.write("Dataset:")
            st.write(f_df)
        else:
            st.error('csv/xlsx File Upload is Required')
    st.title("")
    cmf.subheader('Core Data')    
    with cmf.expander("Upload"):    
        uploaded_file2 = st.file_uploader("Upload a CSV or XLSX file", type=["csv", "xlsx"])
        dftcc= st.checkbox('Use demo file  ')
        if uploaded_file2 is not None and (uploaded_file2.name.lower().endswith('.xlsx') or uploaded_file2.name.lower().endswith('.csv')):
            if uploaded_file2.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
                c_df = pd.read_excel(uploaded_file2, engine="openpyxl")
            else:
                c_df = pd.read_csv(uploaded_file2)
            st.success('File Uploaded Successfully')
    
            st.write("Core Data:")
            st.write(c_df)

        elif dftcc:
            file_f = "./files/pfiles-main/Core_data.xlsx"
            c_df = pd.read_excel(file_f, engine="openpyxl")
            st.success('File Uploaded Successfully')
    
            st.write("Dataset:")
            st.write(c_df)
        else:
            st.error('csv/xlsx File Upload is Required')
   
    



    # ##########################################################################
    # #                          Visualization                                 #
    # ##########################################################################            
if file is not None and (file.name.lower().endswith('.las') or file.name.lower().endswith('.LAS')) or dfle:           
    with t2:
            

        # with st.spinner('Wait for it...'):
        #     time.sleep(time.time() - start_time)



            st.subheader('Interactive Plot')
             # st.title("Visualization")
            
            # @st.cache_data(experimental_allow_widgets=True)
            def plot(well_df):
                cola, colb  = st.columns(2)

                with cola.expander("Line Plot"):
                    colc, cold  = st.columns(2)
                    curves = colc.multiselect('Select Curves To Plot', well_df.columns , key="multiselect1")
                    semilog_col = dfMN['Rxo'].to_list() + dfMN['Rt'].to_list() +['RT20','RT50','RT30','RT60','RT20','RT50','RT60']+['AT20','AT30','AT50','AT60','AT20','AT50','AT60']+['AF10','AF20','AF30','AF50','AF60','AF20','AF50','AF60']+['AO10','AO20','AO30','AO50','AO60','AO20','AO50','AO60']
                    matched_mnemonics_semilog_columns = [curve_item for curve_item in curves if curve_item in semilog_col]
                    LG= cold.multiselect('Log Scale for:',curves, key="multiselect2",default=matched_mnemonics_semilog_columns)

                    if len(curves) < 1:
                        st.warning('Please select at least 1 curve.')
                    else:
                        curve_index = 1
                        if st.checkbox("Submit"):
                            fig = make_subplots(rows=1, cols=len(curves), subplot_titles=curvename(df_unit,curves), shared_yaxes=True)
                            for curve in curves:
                                if curve in LG:
                                    log_bool = 'log'
                                else:
                                    log_bool = 'linear'
                                fig.add_trace(go.Scatter(x=well_df[curve], y=well_df['DEPTH'], mode='lines'), row=1, col=curve_index)
                                # Set x-axis to log scale
                                fig.update_xaxes(type=log_bool, row=1, col=curve_index)
                                curve_index += 1
                            fig.update_layout(height=1000, showlegend=False, yaxis={'title': curvename(df_unit,[deps])[0], 'autorange': 'reversed'})
                            # Change the plot style family (template)
                            fig.update_layout(template='plotly_dark')  # Change to 'plotly_dark' template, or use any other available template
                            st.plotly_chart(fig, use_container_width=True)
                        else:
                            st.write('Please complete your selections for the line plot')
                with colb.expander(" Scatter Plot"):
                    colc, cold  = st.columns(2)
                    curves = colc.multiselect('Select Curves To Plot', well_df.columns , key="multiselect1O")
                    #semilog_col = dfMN['Rxo'].to_list() + dfMN['Rt'].to_list() +['RT20','RT50','RT30','RT60','RT20','RT50','RT60']+['AT20','AT30','AT50','AT60','AT20','AT50','AT60']
                    matched_mnemonics_semilog_columns = [curve_item for curve_item in curves if curve_item in semilog_col]
                    LG= cold.multiselect('Log Scale for:',curves, key="multiselect2O",default=matched_mnemonics_semilog_columns)

                    if len(curves) < 1:
                        st.warning('Please select at least 1 curve.')
                    else:
                        curve_index = 1
                        if st.checkbox("Submit "):
                            fig = make_subplots(rows=1, cols=len(curves), subplot_titles=curvename(df_unit,curves), shared_yaxes=True)
                            for curve in curves:
                                if curve in LG:
                                    log_bool = 'log'
                                else:
                                    log_bool = 'linear'
                                fig.add_trace(go.Scatter(x=well_df[curve], y=well_df['DEPTH'], mode='markers', marker={'size': 2}), row=1, col=curve_index)
                                fig.update_xaxes(type=log_bool, row=1, col=curve_index)
                                curve_index += 1
                            fig.update_layout(height=1000, showlegend=False, yaxis={'title': curvename(df_unit,[deps])[0], 'autorange': 'reversed'})
                            fig.update_layout(template='plotly_dark')  # Change to 'plotly_dark' template, or use any other available template
                            st.plotly_chart(fig, use_container_width=True)
                        else:
                                st.write('Please complete selections for the Scatter plot')            
                with cola.expander(" Histogram"):
                    colc,colk, cold  = st.columns(3)
                    hist_curve = colc.selectbox('Select a Curve', well_df.columns, index=2)
                    if hist_curve is not None:
                        bin_size = colk.number_input("Bin size", value=(well_df[hist_curve].mean())/60)
                    # log_option = colb.radio('Select Linear or Logarithmic Scale', ('Linear', 'Logarithmic'))
                    hist_col = cold.color_picker('Select Histogram Colour', value='#1aa2aa')
                    # colc.write('Color:  ' + hist_col)

                    # if log_option == 'Linear':
                    #     log_bool = False
                    # elif log_option == 'Logarithmic':
                    #     log_bool = True
                    # st.write(df_fill)
                    if st.checkbox("Submit  "):
                        histogram = px.histogram(well_df, x=hist_curve, log_x=False, nbins=int((well_df[hist_curve].max() - well_df[hist_curve].min()) / bin_size))
                        histogram.update_traces(marker_color=hist_col)
                        histogram.update_xaxes(title_text=curvename(df_unit,[hist_curve])[0])
                        histogram.update_layout(template='plotly_dark')
                        st.plotly_chart(histogram, use_container_width=True)     
                with colb.expander("Cross Plot"):
                    colc, cold  = st.columns(2)
                    st.write('')
                    xplot_x = colc.selectbox('X-Axis', well_df.columns,index=1)
                    xplot_x_log = cold.radio('X Axis - Linear or Logarithmic', ('Linear', 'Logarithmic'))
                    if xplot_x_log == 'Linear':
                        xplot_x_bool = False
                    elif xplot_x_log == 'Logarithmic':
                        xplot_x_bool = True
                    st.write('')
                    xplot_y = colc.selectbox('Y-Axis', well_df.columns,index=2)  # Change 'col1' to 'col2'
                    xplot_y_log = cold.radio('Y Axis - Linear or Logarithmic', ('Linear', 'Logarithmic'))  # Change 'col1' to 'col2'
                    if xplot_y_log == 'Linear':
                        xplot_y_bool = False
                    elif xplot_y_log == 'Logarithmic':
                        xplot_y_bool = True
                    custom_color_scale = ["red","orange", "blue",  "purple"]

                    xplot_col = cold.selectbox('Colour-Bar', well_df.columns, index=0)
                    if st.checkbox("Completed the Selection for the cross plot"):
                        xplot = px.scatter(
                            well_df,
                            x=xplot_x,
                            y=xplot_y,
                            color=xplot_col,
                            log_x=xplot_x_bool,
                            log_y=xplot_y_bool,
                            color_continuous_scale=custom_color_scale
                        )
                        xplot.update_layout(template='plotly_dark')
                        xplot.update_xaxes(title_text=curvename(df_unit,[xplot_x])[0])
                        xplot.update_yaxes(title_text=curvename(df_unit,[xplot_y])[0])
                        xplot.update_coloraxes(colorbar_title=curvename(df_unit,[xplot_col])[0])
                        st.plotly_chart(xplot, use_container_width=True)
            plot(well_df)
            st.subheader('Formation Tops Plot')
            with st.expander("View"):
                if uploaded_file1 is not None and (uploaded_file1.name.lower().endswith('.xlsx') or uploaded_file1.name.lower().endswith('.csv')) or dftfc:
                    ftd,fbd,ffn=st.columns(3)


                    
                                         
                     

                    
                    selected_column_top_depth = ftd.selectbox('Select top depth',f_df.columns, index=f_df.columns.get_loc('Top depth (m)') if 'Top depth (m)' in f_df.columns else 1)
                    selected_column_base_depth = fbd.selectbox('Select base depth',f_df.columns, index=f_df.columns.get_loc('Base depth (m)') if 'Base depth (m)' in f_df.columns else 1)
                    selected_column_formation_name = ffn.selectbox('Select Formation',f_df.columns,index=f_df.columns.get_loc('Formation name') if 'Formation name' in f_df.columns else 1)
                    if (
                        selected_column_top_depth is not None
                        and selected_column_formation_name is not None
                        and selected_column_base_depth is not None
                        and not isinstance(f_df[selected_column_top_depth][0], str)
                        and not isinstance(f_df[selected_column_base_depth][0], str)
                    ):
                        combined_depth = f_df[selected_column_top_depth].tolist() + f_df[selected_column_base_depth].tolist()
                        maximum_value = max(combined_depth)
                        depth_for_formation_plot = np.arange(0, maximum_value, 0.15)
                        def get_cmap(n, name='hsv'):
                            return plt.cm.get_cmap(name, n)
                        # fig, ax = plt.subplots(1, 2, figsize=(8, 12), sharex=True)
                        fig, ax = plt.subplots(1, 2, figsize=(5, 10), sharex=True, gridspec_kw={'width_ratios': [1, 0.1]})
                        fig.subplots_adjust(top=0.85)
                        ax[0].set_title('Formation Tops', fontsize=10, fontweight='bold')
                        cmap = get_cmap(len(f_df[selected_column_top_depth]))
                        for form_num in range(len(f_df[selected_column_top_depth])):
                            condition = (f_df[selected_column_top_depth][form_num] < depth_for_formation_plot) & (depth_for_formation_plot < f_df[selected_column_base_depth][form_num])
                            ax[0].fill_betweenx(depth_for_formation_plot, 0, 1, where=condition, facecolor=cmap(form_num), alpha=0.5)
                        #ax.set_ylim([max(well_df['DEPTH']), min(well_df['DEPTH'])])
                        ax[0].set_ylabel('Depth')
                        for i in range(len(f_df[selected_column_base_depth])):
                            ax[0].axhline(y=f_df[selected_column_top_depth][i], color='r', alpha=1)
                            ax[0].axhline(y=f_df[selected_column_base_depth][i], color='r', alpha=1)
                            ax[0].text(0.2, (f_df[selected_column_top_depth][i]+f_df[selected_column_base_depth][i])/2, f_df[selected_column_formation_name][i],fontsize=9,color='k')
                        ax[0].set_xlim([0, 1])
                        ax[0].set_yticks(np.arange(0,5000, 500))
                        # ax[0].set_yticklabels(ax[0].get_yticks(), fontsize=4)
                        ax[0].set_xlabel('Formations')
                        ax[0].set_ylabel('Depth')
                        # Hide x-axis ticks
                        ax[0].set_xticks([])
                        # ax[1].set_title('Selected Formations', fontsize=14, fontweight='bold')
                        ax[1].set_title('Selected\nFormations', fontsize=10, fontweight='bold')
                        cmap = get_cmap(len(f_df[selected_column_top_depth]))
                        for form_num in range(len(f_df[selected_column_top_depth])):
                            condition = (f_df[selected_column_top_depth][form_num] < well_df['DEPTH']) & (well_df['DEPTH'] < f_df[selected_column_base_depth][form_num])
                            ax[1].fill_betweenx(well_df.DEPTH, 0, 1, where=condition, facecolor=cmap(form_num), alpha=0.5)
                        #ax.set_ylim([max(well_df['DEPTH']), min(well_df['DEPTH'])])
                        ax[1].set_ylabel('Depth')
                        for i in range(len(f_df[selected_column_base_depth])):
                            ax[1].axhline(y=f_df[selected_column_top_depth][i], color='r', alpha=1)
                            ax[1].axhline(y=f_df[selected_column_base_depth][i], color='r', alpha=1)
                            # ax[1].text(0.2, (f_df[selected_column_top_depth][i]+f_df[selected_column_base_depth][i])/2, f_df[selected_column_formation_name][i],fontsize=12,color='k')
                        ax[1].set_xlim([0, 1])
                        # ax[1].set_xlabel('Formations')
                        ax[1].set_ylabel("")
                        ax[1].set_xticks([])
                        ax[1].set_yticks(np.arange(0,5000, 500))
                        ax[0].invert_yaxis()
                        ax[1].invert_yaxis()
                        ax[1].set_yticks([])
                        jkkl,lkkj=st.columns(2)
                        jkkl.pyplot(fig)
                else:
                     st.warning("Upload Formation Tops file in Data Loading Tab")










    ####################################################################################
    #                             Checking for the default mneomenic                   #
    ####################################################################################

    #1 Bit Size
    matched_mnemonics_BS = [curve_item for curve_item in las_file.keys() if curve_item in dfMN['BitSize'].values]

    default_column_BS = matched_mnemonics_BS[0] if matched_mnemonics_BS else 'BS'

    #2 Caliper

    matched_mnemonics_CALI = [curve_item for curve_item in las_file.keys() if curve_item in dfMN['Caliper'].values]

    default_column_CALI = matched_mnemonics_CALI[0] if matched_mnemonics_CALI else 'CALI'

    #3 Gamma ray

    matched_mnemonics_GR = [curve_item for curve_item in las_file.keys() if curve_item in dfMN['GR'].values]

    default_column_GR = matched_mnemonics_GR[0] if matched_mnemonics_GR else 'GR'

    #4 Neutron Porosity

    matched_mnemonics_NPHI = [curve_item for curve_item in las_file.keys() if curve_item in dfMN['NPHI'].values]

    default_column_NPHI = matched_mnemonics_NPHI[0] if matched_mnemonics_NPHI else 'NPHI'

    #5 Density Porosity

    matched_mnemonics_DPHI = [curve_item for curve_item in las_file.keys() if curve_item in dfMN['PHIT'].values]

    default_column_DPHI = matched_mnemonics_DPHI[0] if matched_mnemonics_DPHI else 'DPHI'

    #6 Density 

    matched_mnemonics_RHOB = [curve_item for curve_item in las_file.keys() if curve_item in dfMN['RHOB'].values]

    default_column_RHOB = matched_mnemonics_RHOB[0] if matched_mnemonics_RHOB else 'RHOB'

    #7 Deep Resistivity 

    matched_mnemonics_RESD = [curve_item for curve_item in las_file.keys() if curve_item in dfMN['Rt'].values]

    default_column_RESD = matched_mnemonics_RESD[0] if matched_mnemonics_RESD else 'AT90'

    #8 Shallow Resistivity

    matched_mnemonics_RESS = [curve_item for curve_item in las_file.keys() if curve_item in dfMN['Rxo'].values]

    default_column_RESS = matched_mnemonics_RESS[0] if matched_mnemonics_RESS else 'AT10'

    # ----------------------------------------------------------------------------------TAB 2--

####################################################################################
#                             Quality check                                        #
####################################################################################

# if file is not None and (file.name.lower().endswith('.las') or file.name.lower().endswith('.LAS')):
if file is not None and (file.name.lower().endswith('.las') or file.name.lower().endswith('.LAS')) or dfle:
    with t3:
        st.subheader('Data Preparation')
        ex=st.expander("Quality Control")
        with ex:

            btc1s = st.checkbox("View Availability", key='krj2')
            if btc1s:
                fig, ax = plt.subplots()
                msno.matrix(well_df, ax=ax)
                cj,jc=st.columns([1,2])
                jc.pyplot(fig)




            # @st.cache_data(experimental_allow_widgets=True)
            # def checks():

            #     st.subheader("Checks:")



            #     sa1, sa2, sa3= st.columns(3)
            #     sa2.subheader("Quality Check")

            #     # Dictionary 'tests' containing quality control checks for different categories of data
            #     tests = {
            #         'Each': [
            #             wq.no_flat,  # Check for no flat curves
            #             wq.no_gaps,  # Check for no gaps in the data
            #             wq.not_empty  # Check if the data is not empty
            #         ],
            #         'GR': [
            #             wq.all_positive,  # Check if all values are positive
            #             wq.all_between(0, 250),  # Check if all values are between 0 and 250
            #             wq.check_units(['API', 'GAPI'])  # Check if units are either 'API' or 'GAPI'
            #         ],
            #         'RHOB': [
            #             wq.all_positive,  # Check if all values are positive
            #             wq.all_between(1.5, 3),  # Check if all values are between 1.5 and 3
            #             wq.check_units(['G/CC', 'g/cm3'])  # Check if units are either 'G/CC' or 'g/cm3'
            #         ]
            #     }

            #     data_qc_table = well.qc_table_html(tests)

            #     btc = sa2.checkbox("View Table", key='k1')
            #     if btc:
            #         st.markdown(data_qc_table, unsafe_allow_html=True)



            #     sa3.subheader("NaN Value Checks")
            #      # Check the fraction of NaN values
            #     tests_nans = {
            #         'Each': [wq.fraction_not_nans] 
            #     }

            #     # Generate an HTML table for quality control checks on NaN values using 'well' data and the 'tests_nans' dictionary
            #     data_nans_qc_table = well.qc_table_html(tests_nans)



            #     btc1s = sa3.checkbox("View Plot", key='krj2')
            #     if btc1s:


            #         fig, ax = plt.subplots()
            #         msno.matrix(well_df, ax=ax)
            #         cj,jc=st.columns([1,2])
            #         jc.pyplot(fig)


            #     btc1 = sa3.checkbox("View Table", key='k2')
            #     if btc1:
            #         st.write(data_nans_qc_table, unsafe_allow_html=True)

            # checks()


            
            ##########################################################################
            #                             Bad bore hole data                         #
            ##########################################################################            
  

            def badwd():        
                st.title("")
                st.title("")
                st.subheader("Bad well Data:")

                a1, a2, a3 = st.columns([3,2,2])
                bit_size_curve_availibility_question = a1.radio("Is there a bit size curve available?", ('No', 'Yes'))


                if bit_size_curve_availibility_question == 'Yes':
                    # Working as the dropdown menu for selecting the Bit size curve

                    column_choice_BS = a2.selectbox('Choose the Bit Size column', well_df.columns, index=well_df.columns.get_loc(default_column_BS) if default_column_BS in well_df.columns else 1)
                    selected_column_BS=column_choice_BS

                    matched_mnemonics_CALI = [curve_item for curve_item in las_file.keys() if curve_item in dfMN['Caliper'].values]

                    default_column_CALI = matched_mnemonics_CALI[0] if matched_mnemonics_CALI else 'CALI'

                    # Working as the dropdown menu for selecting the Caliper curve

                    column_choice_CALI = a2.selectbox('Choose the Caliper column', well_df.columns, index=well_df.columns.get_loc(default_column_CALI) if default_column_CALI in well_df.columns else 1)

                    selected_column_CALI=column_choice_CALI
                    # a3.write("")    
                    # a3.write(f"Selected column: {selected_column_CALI}.")

                    tol_val = a3.number_input("Enter the tolerance value for borehole diameter deviation:",value=float("2.0"))
                    condition_bad = abs(well_df[selected_column_BS] - well_df[selected_column_CALI]) > tol_val
                    condition_good = abs(well_df[selected_column_BS] - well_df[selected_column_CALI]) <= tol_val

                    # Create a new DataFrame for bad data
                    df_bad_data = well_df[condition_bad]

                    # Print or display the bad data DataFrame
                    st.text("Bad Dataset:")
                    st.write(df_bad_data)

                else:
                    bit_size = a2.number_input("Enter the Bit size value:", value=float("8.5"))

                    matched_mnemonics_CALI = [curve_item for curve_item in las_file.keys() if curve_item in dfMN['Caliper'].values]

                    default_column_CALI = matched_mnemonics_CALI[0] if matched_mnemonics_CALI else 'CALI'

                    column_choice_CALI = a2.selectbox('Choose the Caliper column', well_df.columns, index=well_df.columns.get_loc(default_column_CALI) if default_column_CALI in well_df.columns else 1)

                    selected_column_CALI=column_choice_CALI
                    # st.write(f"You selected column: {selected_column_CALI} for Caliper.")

                    selected_column_BS='bit_size'
                    well_df[selected_column_BS]=[bit_size] * len(well_df['DEPTH'])
                    tol_val = a3.number_input("Enter the tolerance value for borehole diameter deviation:",value=float("2.0"))
                    condition_bad = abs(bit_size - well_df[selected_column_CALI]) > tol_val
                    condition_good = abs(bit_size - well_df[selected_column_CALI]) <= tol_val

                    # Create a new DataFrame for bad data
                    df_bad_data = well_df[condition_bad]

                    # Print or display the bad data DataFrame
                    st.subheader("Bad Data:")
                    st.write(df_bad_data)
                return  selected_column_CALI,condition_bad,condition_good,df_bad_data,selected_column_BS, tol_val,well_df

            selected_column_CALI,condition_bad,condition_good,df_bad_data,selected_column_BS, tol_val,well_df = badwd()
            df_fill=well_df.copy()
            out,nanr,patc=st.columns(3)  
            # Radio button for outlier_operation
            outlier_operation = out.radio('Outlier Removal', ['Not Selected','Selected'])
            # Radio button for nanremovel
            nanremoval_zone_operation = nanr.radio('NaN removal', ['Not Selected','Selected'])
            # R adio for the Patching
            Patchinng_operation=patc.radio('Patching', ['Not Selected','Selected'])


            if outlier_operation =='Not Selected':
                out.warning('Outlier removal not applied')

            if nanremoval_zone_operation=='Not Selected':
                nanr.warning('NaN removal not applied')

            if Patchinng_operation=='Not Selected':
                patc.warning('Patching not applied')


                ##########################################################################
                #                     Outlier using histogram                            #
                ##########################################################################    
            if outlier_operation=='Selected':
                # with st.spinner('Wait for it...'):
                #     time.sleep(time.time() - start_time)
                def outlr(well_df):
                    #st.write(well_df)                
                    st.subheader("Outlier Removal")

                    ot= st.radio('Outlier Removal',['Interquartile range (IQR) method','Using Histogram'])
                    if ot == 'Using Histogram':
                        selected_logs = st.multiselect("Select Logs to Display", well_df.columns)
                        vla=st.number_input('Choose window',value=40)

                        slider_values = {log: (0, 100) for log in selected_logs}
                        filtered_data = {log: well_df[log] for log in selected_logs}

                        num_bins = 300
                        figure_height = 400
                        figure_width=500
                        columns_per_row = 3
                        num_rows = len(selected_logs) // columns_per_row + (len(selected_logs) % columns_per_row > 0)

                        st.subheader("Original:")
                        for row in range(num_rows):
                            cols = st.columns(columns_per_row)
                            for i in range(row * columns_per_row, min((row + 1) * columns_per_row, len(selected_logs))):
                                log = selected_logs[i]
                                with cols[i % columns_per_row]:
                                    st.text(f"Log: {log}")
                                    slider_values[log] = st.slider(f"Select {log} Percentile", min_value=0, max_value=100, value=slider_values[log], key=f'key={log}')
                                    selected_values = np.percentile(well_df[log], slider_values[log])
                                    fig = go.Figure(data=[go.Histogram(x=well_df[log], nbinsx=num_bins)])
                                    fig.update_layout(height=figure_height, width=figure_width)
                                    for value in selected_values:
                                        fig.add_shape(
                                            type="line",
                                            x0=value,
                                            x1=value,
                                            y0=0,
                                            y1=1,
                                            xref="x",
                                            yref="paper",
                                            line=dict(color="red", width=2)
                                        )
                                    st.plotly_chart(fig)


                        # Added            
                        def remove_outliers(dfol, col,lower_bound,upper_bound,window):

                            # Create a mask for the outliers
                            outlier_mask = (dfol[col] < lower_bound) | (dfol[col] > upper_bound)

                            # Calculate the rolling mean with the specified window size
                            rolling_mean = dfol[col].rolling(window=window, min_periods=1).mean()

                            # Replace values outside the cutoff with the rolling mean
                            dfol.loc[outlier_mask, col] = rolling_mean[outlier_mask]

                            return dfol

                        filtered_df=well_df.copy()
                        if selected_logs:
                            for curve_name in selected_logs:
                                filtered_df=remove_outliers(filtered_df, curve_name,slider_values[log][0],slider_values[log][1],vla)




                        st.subheader("Filtered:")
                        for row in range(num_rows):
                            cols = st.columns(columns_per_row)
                            for i in range(row * columns_per_row, min((row + 1) * columns_per_row, len(selected_logs))):
                                log = selected_logs[i]
                                with cols[i % columns_per_row]:
                                    st.text(f"Log: {log} (Filtered)")
                                    filtered_df = well_df[(well_df[log] >= slider_values[log][0]) & (well_df[log] <= slider_values[log][1])]
                                    fig = go.Figure(data=[go.Histogram(x=filtered_df[log], nbinsx=num_bins)])
                                    fig.update_layout(height=figure_height, width=figure_width)
                                    st.plotly_chart(fig)

                        if st.checkbox('Apply filter'):
                            df_fill = filtered_df.copy()
                        else:
                            df_fill = well_df.copy()

                    if ot=='Interquartile range (IQR) method':
                        def remove_outliers(dfol, col, window, threshold=3):
                            q1 = np.percentile(dfol[col], 25)
                            q3 = np.percentile(dfol[col], 75)
                            iqr = q3 - q1
                            lower_bound = q1 - threshold * iqr
                            upper_bound = q3 + threshold * iqr

                            # Create a mask for the outliers
                            outlier_mask = (dfol[col] < lower_bound) | (dfol[col] > upper_bound)

                            # Calculate the rolling mean with the specified window size
                            rolling_mean = dfol[col].rolling(window=window, min_periods=1).mean()

                            # Replace values outside the cutoff with the rolling mean
                            dfol.loc[outlier_mask, col] = rolling_mean[outlier_mask]

                            return dfol
                        selected_curves = st.multiselect("Select log curves", well_df.columns, default=[well_df.columns[1]])
                        vla=st.number_input('Choose window',value=40)
                        filtered_df=well_df.copy()
                        if selected_curves:
                            for curve_name in selected_curves:
                                filtered_df=remove_outliers(filtered_df, curve_name,vla,threshold=3)
                                # Display the cleaned data
                                # st.dataframe(well_df[[curve_name]])
                        # st.subheader('Box Plots')
                        num_plots_per_row = 3
                        num_columns = len(selected_curves)
                        num_rows = (num_columns - 1) // num_plots_per_row + 1
                        fig = sp.make_subplots(rows=num_rows, cols=num_plots_per_row, subplot_titles=selected_curves)
                        # Add box plots for both DataFrames to the subplot
                        for i, col in enumerate(selected_curves):
                            row = i // num_plots_per_row + 1
                            col_num = i % num_plots_per_row + 1
                            box_original = go.Box(y=well_df[col], name=f'Original {col}')
                            box_filtered = go.Box(y=filtered_df[col], name=f'Filtered {col}')
                            fig.add_trace(box_original, row=row, col=col_num)
                            fig.add_trace(box_filtered, row=row, col=col_num)
                        # Update subplot layout and title
                        fig.update_layout(title_text="Box Plots Comparison", showlegend=True)
                        # Show the subplot
                        st.plotly_chart(fig)
                        if st.checkbox('Apply filter '):
                            df_fill = filtered_df.copy()
                        else:
                            df_fill = well_df.copy()
                    return df_fill
                df_fill = outlr(well_df)
            if nanremoval_zone_operation=='Selected':
                    # with st.spinner('Wait for it...'):
                    #     time.sleep(time.time() - start_time)

                    st.subheader("NaN value Filling with:")
                    clm = st.multiselect('Select Curve', df_fill.columns, key="multiselect5", default=[df_fill.columns[1]])

                    if st.checkbox("View Plot NaN filling"):
                        fig, ax = plt.subplots()
                        msno.matrix(df_fill, ax=ax)
                        st.pyplot(fig)

                    aw = st.radio('Fill type:', ['Mean', 'Linear Interpolation'])
                    nanc = st.checkbox('Finish   ')
                    if aw == 'Mean':
                        if nanc:
                            for column in clm:
                                mean_value = df_fill[column].mean()
                                df_fill[column].fillna(mean_value, inplace=True)
                    if aw == 'Linear Interpolation':
                        if nanc:
                            for column in clm:
                                df_fill[column] = df_fill[column].interpolate(method='linear', limit_direction='both')
                    if nanc:
                        st.write(df_fill)
                        num_columns = len(clm)
                        optimal_width = 120 * num_columns
                        fig = make_subplots(rows=1, cols=num_columns, shared_yaxes=True, horizontal_spacing=0.03)
                        for i, column in enumerate(clm, 1):
                            fig.add_trace(go.Scatter(x=df_fill[column], y=df_fill['DEPTH'], line=dict(width=1, color='red'), name=column + ' After'), row=1, col=i)
                            fig.add_trace(go.Scatter(x=df_fill[column], y=df_fill['DEPTH'], line=dict(width=1, color='green'), name=column + ' Before'), row=1, col=i)


                        for i, column in enumerate(clm, 1):
                            fig.update_xaxes(title_text=column, row=1, col=i)

                        fig.update_yaxes(title_text='Depth (m)', autorange='reversed', gridwidth=0.8)
                        fig.update_layout(width=optimal_width, height=800)
                        st.plotly_chart(fig)
                        
                # -----------------------------------------------------------------------------------------------------------Pacthing--    

                ##########################################################################
                #                             Patching                                   #
                ##########################################################################
            if Patchinng_operation =='Selected':


                # with st.spinner('Wait for it...'):
                #     time.sleep(time.time() - start_time)
                st.subheader("Patching")        

                df_fill = df_fill.copy()

                clicked_points = []

                selected_columns = st.multiselect("Select columns to plot", df_fill.columns)

                patch_option = st.radio("Select Input Type for the patching", ["Picking from plot","Mannual Input"])

                if patch_option== "Picking from plot":
                  if len(selected_columns) > 0:
                      fig = make_subplots(rows=1, cols=len(selected_columns), shared_yaxes=True)

                      colors_patch = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']

                      scatter_plots = []
                      for i, column in enumerate(selected_columns):
                          scatter_plot = go.Scatter(x=df_fill[column], y=df_fill['DEPTH'], mode='lines', name=column, line=dict(color=colors_patch[i % len(colors_patch)]))
                          scatter_plots.append(scatter_plot)

                      for i, scatter_plot in enumerate(scatter_plots):
                          fig.add_trace(scatter_plot, row=1, col=i + 1)

                      for i in range(len(selected_columns)):
                          fig.update_yaxes(autorange='reversed', row=1, col=i + 1)
                      fig.update_layout(width=600, height=800)


                      end_time = time.time()  
                      elapsed_time = end_time - start_time

                    #   with st.spinner('Wait for it...'):
                    #       time.sleep(elapsed_time)
                    #   st.title(f"Time taken: {elapsed_time} seconds")

                      component_value = plotly_events(fig)

                      # Display the chart
                      # st.write(component_value)

                      # Display the clicked data points
                      if component_value:
                          st.subheader("Clicked Data Points:")
                          clicked_data_with_names = []
                          for point in component_value:
                              st.write(f"X: {point['x']:.2f}, Y: {point['y']:.2f}, Curve: {point['name']}")
                              clicked_data_with_names.append({"X": point['x'], "Y": point['y'], "Curve": point['name']})

                          # Append the clicked data to the list
                          clicked_points.extend(clicked_data_with_names)

                      # Add a "Finish" button to clear and display the clicked data
                      if st.checkbox("Finish"):
                          # Create a DataFrame from the list of clicked data
                          clicked_points = pd.DataFrame(clicked_points)

                          name_of_columns = set(clicked_points['Curve'])
                          name_of_columns = list(name_of_columns)

                          # Iterate over each column
                          for col in name_of_columns:
                              points = clicked_points[clicked_points['Curve'] == col][['X', 'Y']]
                              num_points = len(points)
                              if num_points >= 2 and num_points % 2 == 0:
                                  for i in range(num_points // 2):
                                      i1 = 2 * i
                                      i2 = 2 * i + 1
                                      if i2 < num_points:  # Check if the indices are within bounds
                                          # Calculate the slope
                                          dx = points['X'].iloc[i2] - points['X'].iloc[i1]  # curve value (y)
                                          dy = points['Y'].iloc[i2] - points['Y'].iloc[i1]  # depth value (x)
                                          slope = dx / dy
                                          intercept = points['X'].iloc[i2] - slope * points['Y'].iloc[i2]
                                          # Determine the range of depths to replace
                                          a = max([points['Y'].iloc[i2], points['Y'].iloc[i1]])
                                          b = min([points['Y'].iloc[i2], points['Y'].iloc[i1]])
                                          # Select the rows in the DataFrame where 'DEPTH' is within the specified range
                                          selected_rows = (df_fill['DEPTH'] >= b) & (df_fill['DEPTH'] <= a)
                                          # Calculate the values to replace the NaN values in 'col' (the current column)
                                          NaN_replace_val = slope * df_fill.loc[selected_rows, 'DEPTH'] + intercept
                                          # Update the 'col' with the calculated values
                                          df_fill.loc[selected_rows, col] = NaN_replace_val
                          # Create a new Figure with subplots based on the updated data in df_fill
                          updated_fig = make_subplots(rows=1, cols=len(selected_columns), shared_yaxes=True)

                          # Create Scatter plots for the selected columns using the updated data
                          updated_scatter_plots = []
                          for column in selected_columns:
                              updated_scatter_plot = go.Scatter(x=df_fill[column], y=df_fill['DEPTH'], mode='lines', name=column)
                              updated_scatter_plots.append(updated_scatter_plot)

                          # Add the Scatter plots to the subplots in the updated figure
                          for i, updated_scatter_plot in enumerate(updated_scatter_plots):
                              updated_fig.add_trace(updated_scatter_plot, row=1, col=i + 1)

                          # Update the y-axes in the updated figure
                          for i in range(len(selected_columns)):
                              updated_fig.update_yaxes(autorange='reversed', row=1, col=i + 1)
                          updated_fig.update_layout(width=450, height=600)

                          st.plotly_chart(updated_fig)
                  else:
                      st.warning("Please select at least one column to plot.")  
                elif patch_option== "Mannual Input":
                    def manual_patch(df_fill, selected_columns):
                      df_patch=df_fill.copy()
                      patchplot=st.columns(len(selected_columns))
                      for j in range(len(selected_columns)):
                        column=selected_columns[j] 
                        fig=make_subplots(rows=1,cols=5)
                        trace= go.Scatter(x=df_patch[column], y=df_patch['DEPTH'], mode='lines', name=column, line=dict(color='#1f77b4'))
                        fig.add_trace(trace)
                        fig.update_yaxes(title_text='DEPTH', autorange='reversed', gridwidth=0.8)
                        fig.update_xaxes(title_text=column)
                        patchplot[j].plotly_chart(fig)
                        num_patch = patchplot[j].number_input('Enter the number of Patch to be applied for '+column+':', min_value=0, step=1)
                        patchplot[j].write(f'Depth ranges values to enter for patching: {num_patch}')
                        patch_zones_boundary = []
                        for i in range(2*num_patch):
                            if i%2==0:
                                deptype='top'
                                pat_num=int(i/2+1)
                                key = f"_{column}top{pat_num}" 
                            else:
                                deptype='bottom'
                                pat_num=int((i-1)/2+1)
                                key = f"_{column}bottom{pat_num}"
                            depth =patchplot[j].number_input(f"Enter the "+ deptype +f" depth for the patch {pat_num}:",min_value=0.0 if i%2==0 else patch_zones_boundary[-1], step=0.001,key=key )
                            patch_zones_boundary.append(depth)
                        if patch_zones_boundary:
                            patch_zones_value=[]
                            depth_value=[]
                            for i in range(len(patch_zones_boundary)):
                                nearest_index = (df_patch['DEPTH'] - patch_zones_boundary[i]).abs().idxmin()
                                nearest_depth = float(df_patch['DEPTH'].loc[nearest_index])
                                depth_value.append(nearest_depth)
                                patch_zones_value.append(float(df_patch[column].loc[df_patch['DEPTH'] == nearest_depth]))
                            clicked_points = pd.DataFrame({
                                    'X': patch_zones_value,
                                    'Y': patch_zones_boundary
                                })
                            for i in range(int(len(clicked_points)/2)):
                                # Calculate the slope
                                # Note: here the equation of the line is x = slope * y + intercept since the curve is on the x-axis and depth is on the y-axis
                                dx = clicked_points['X'].iloc[2*i+1] - clicked_points['X'].iloc[2*i]  # curve value (y)
                                dy = clicked_points['Y'].iloc[2*i+1] - clicked_points['Y'].iloc[2*i]  # depth value (x)
                                slope = dx / dy
                                intercept = clicked_points['X'].iloc[2*i+1] - slope * clicked_points['Y'].iloc[2*i+1]
                                # Determine the range of depths to replace
                                a = max([clicked_points['Y'].iloc[2*i+1], clicked_points['Y'].iloc[2*i]])
                                b = min([clicked_points['Y'].iloc[2*i+1], clicked_points['Y'].iloc[2*i]])
                                # Select the rows in the DataFrame where 'DEPTH' is within the specified range
                                selected_rows = (df_patch['DEPTH'] >= b) & (df_patch['DEPTH'] <= a)
                                # Calculate the values to replace the NaN values in 'selected_column'
                                NaN_replace_val = slope * df_patch.loc[selected_rows, 'DEPTH'] + intercept
                                # Update the 'selected_column' with the calculated values
                                df_patch.loc[selected_rows,column] = NaN_replace_val
                            fig=make_subplots(rows=1,cols=5)
                            trace= go.Scatter(x=df_patch[column], y=df_patch['DEPTH'], mode='lines', name=column, line=dict(color='#1f77b4'))
                            fig.add_trace(trace)
                            fig.update_yaxes(title_text='DEPTH', autorange='reversed', gridwidth=0.8)
                            fig.update_xaxes(title_text=column)
                            patchplot[j].plotly_chart(fig)
                            if patchplot[j].checkbox("Apply Patch and Update DataFrame for "+ column ):
                              df_fill = df_patch.copy()
                      return df_fill
                    if selected_columns:
                        df_fill=manual_patch(df_fill, selected_columns)
        
                # ----------------------------------------------------------------------------FE--
        ##########################################################################
        #                  petrophysical properties                              #
        ##########################################################################                   
        l_df = []
        max_val_per=[]
        min_val_per=[]
        
        st.subheader('Petrophysical properties Evaluation') 
        with st.expander("Vshale Calculation"):
            ##########################################################################
            #                  Volume of the shale                                   #
            ##########################################################################      
            cc1,cc2=st.columns(2)
            c1,c2,c3,c4= st.columns(4)
            ca1,ca2,ca3,ca4,ca5=st.columns(5)
            c1W,c2W= st.columns(2)
            vs1,vs2=st.columns(2)
            def vshle():
                cc1.subheader("Vshale calculation and Plot")
        
                column_choice_GR = cc2.selectbox('Gamma Ray', well_df.columns, index=well_df.columns.get_loc(default_column_GR) if default_column_GR in well_df.columns else 1)

                selected_column_GR=column_choice_GR

                gammaray=df_fill[selected_column_GR]
                # selected_column_GR =df_fill['gammaray']
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
                st.title('')
                vs = ca1.selectbox('Vshale type', ('Linear', 'Vsh_Larinor_older', 'Vsh_Larinor_tertiary', 'Vsh_clavier'))
                #cold,cole=st.columns(2)

                def plot_vshale(vs):
                    if vs == 'Linear':
                        fig = plotly.subplots.make_subplots(rows=1, cols=2, subplot_titles=(curvename(df_unit,[selected_column_GR])[0], "Vsh Linear (V/V)"))
                        fig.add_trace(go.Scatter(x=df_fill[selected_column_GR], y=df_fill.DEPTH, mode='lines', name=curvename(df_unit,[selected_column_GR])[0], line=dict(color='blue')), row=1, col=1)
                        quantile= [pmax, pmin]  # Adjust these values as per your requirement
                        lincol=['#808080','#FFFF00']

                        for i in range(len(quantile)):
                            fig.add_shape(
                                go.layout.Shape(
                                    type="line",
                                    x0=quantile[i],
                                    x1=quantile[i],
                                    y0=min(df_fill.DEPTH),
                                    y1=max(df_fill.DEPTH),
                                    line=dict(color=lincol[i], width=4),
                                ),
                                row=1, col=1  # Specify the subplot (row and column)
                            )
                        fig.update_xaxes(dict(tickfont=dict(color='black', size=11),showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True), row=1, col=1)
                        fig.update_yaxes(dict(showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True),row=1, col=1)
    
                        fig.update_xaxes(dict(tickfont=dict(color='black', size=11),showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True), row=1, col=2)
                        fig.update_yaxes(dict(showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True),row=1, col=2)
                        fig.add_trace(go.Scatter(x=Vsh_linear, y=df_fill.DEPTH, mode='lines', name='Vsh Linear (V/V)', line=dict(color='blue')), row=1, col=2)

                        fig.update_yaxes(title_text=curvename(df_unit,[deps])[0], autorange='reversed', gridwidth=0.8)
                        fig.update_traces(line=dict(color='teal'))
                        fig.update_layout(
                            plot_bgcolor='white',
                            width=600, 
                            height=800,
                        )
                        fig.update_layout(
                            title_text='<b>Volume of shale (linear)</b>',
                            title_font=dict(size=25, family='Arial', color='black'),
                            width=600,
                        )
                        c1W.plotly_chart(fig)
                        df_fill['Vsh'] = Vsh_linear
                        df_fill['Vsh'] = df_fill['Vsh'].interpolate(method='linear', limit_direction='both')
                        unitadder(df_unit,'Vsh','V/V')


                    if vs == 'Vsh_Larinor_older':
                        fig = plotly.subplots.make_subplots(rows=1, cols=2, subplot_titles=(curvename(df_unit,[selected_column_GR])[0], "Vsh_Larinor_older(V/V)"))
                        fig.add_trace(go.Scatter(x=df_fill[selected_column_GR], y=df_fill.DEPTH, mode='lines', name=curvename(df_unit,[selected_column_GR])[0], line=dict(color='blue')), row=1, col=1)
                        quantile= [pmax, pmin]  # Adjust these values as per your requirement
                        lincol=['#808080','#FFFF00']

                        for i in range(len(quantile)):
                            fig.add_shape(
                                go.layout.Shape(
                                    type="line",
                                    x0=quantile[i],
                                    x1=quantile[i],
                                    y0=min(df_fill.DEPTH),
                                    y1=max(df_fill.DEPTH),
                                    line=dict(color=lincol[i], width=4),
                                ),
                                row=1, col=1  # Specify the subplot (row and column)
                            )
                        fig.update_xaxes(dict(tickfont=dict(color='black', size=11),showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True), row=1, col=1)
                        fig.update_yaxes(dict(showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True),row=1, col=1)
    
                        fig.update_xaxes(dict(tickfont=dict(color='black', size=11),showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True), row=1, col=2)
                        fig.update_yaxes(dict(showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True),row=1, col=2)
                        fig.add_trace(go.Scatter(x=Vsh_Larinor_older, y=df_fill.DEPTH, mode='lines', name='Vsh_Larinor_older (V/V)', line=dict(color='blue')), row=1, col=2)

                        fig.update_yaxes(title_text=curvename(df_unit,[deps])[0], autorange='reversed', gridwidth=0.8)
                        fig.update_traces(line=dict(color='magenta'))
                        fig.update_layout(
                            plot_bgcolor='white',
                            width=600, 
                            height=800,
                        )

                        fig.update_layout(
                            title_text='<b>Volume of shale (Larinor_older)</b>',
                            title_font=dict(size=25, family='Arial', color='black'),
                            width=600,
                        )
                        c1W.plotly_chart(fig)
                        df_fill['Vsh'] = Vsh_Larinor_older
                        df_fill['Vsh'] = df_fill['Vsh'].interpolate(method='linear', limit_direction='both')
                        unitadder(df_unit,'Vsh','V/V')
                    if vs == 'Vsh_Larinor_tertiary':
                        fig = plotly.subplots.make_subplots(rows=1, cols=2, subplot_titles=(curvename(df_unit,[selected_column_GR])[0], "Vsh_Larinor_tertiary(V/V)"))
                        fig.add_trace(go.Scatter(x=df_fill[selected_column_GR], y=df_fill.DEPTH, mode='lines', name=curvename(df_unit,[selected_column_GR])[0], line=dict(color='blue')), row=1, col=1)
                        quantile= [pmax, pmin]  # Adjust these values as per your requirement
                        lincol=['#808080','#FFFF00']

                        for i in range(len(quantile)):
                            fig.add_shape(
                                go.layout.Shape(
                                    type="line",
                                    x0=quantile[i],
                                    x1=quantile[i],
                                    y0=min(df_fill.DEPTH),
                                    y1=max(df_fill.DEPTH),
                                    line=dict(color=lincol[i], width=4),
                                ),
                                row=1, col=1  # Specify the subplot (row and column)
                            )
                        fig.update_xaxes(dict(tickfont=dict(color='black', size=11),showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True), row=1, col=1)
                        fig.update_yaxes(dict(showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True),row=1, col=1)
    
                        fig.update_xaxes(dict(tickfont=dict(color='black', size=11),showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True), row=1, col=2)
                        fig.update_yaxes(dict(showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True),row=1, col=2)
                        fig.add_trace(go.Scatter(x=Vsh_Larinor_tertiary, y=df_fill.DEPTH, mode='lines', name='Vsh_Larinor_tertiary (V/V)', line=dict(color='blue')), row=1, col=2)

                        fig.update_yaxes(title_text=curvename(df_unit,[deps])[0], autorange='reversed', gridwidth=0.8)
                        fig.update_traces(line=dict(color='blue'))
                        fig.update_layout(
                            plot_bgcolor='white',
                            width=600, 
                            height=800,
                        )

                        fig.update_layout(
                            title_text='<b>Volume of shale (Larinor_tertiary)</b>',
                            title_font=dict(size=25, family='Arial', color='black'),
                            width=600,
                        )
                        c1W.plotly_chart(fig)
                        df_fill['Vsh'] = Vsh_Larinor_tertiary
                        df_fill['Vsh'] = df_fill['Vsh'].interpolate(method='linear', limit_direction='both')
                        unitadder(df_unit,'Vsh','V/V')

                    if vs == 'Vsh_clavier':
                        fig = plotly.subplots.make_subplots(rows=1, cols=2, subplot_titles=(curvename(df_unit,[selected_column_GR])[0], "Vsh_clavier(V/V)"))
                        fig.add_trace(go.Scatter(x=df_fill[selected_column_GR], y=df_fill.DEPTH, mode='lines', name=curvename(df_unit,[selected_column_GR])[0], line=dict(color='blue')), row=1, col=1)
                        quantile= [pmax, pmin]  # Adjust these values as per your requirement
                        lincol=['#808080','#FFFF00']

                        for i in range(len(quantile)):
                            fig.add_shape(
                                go.layout.Shape(
                                    type="line",
                                    x0=quantile[i],
                                    x1=quantile[i],
                                    y0=min(df_fill.DEPTH),
                                    y1=max(df_fill.DEPTH),
                                    line=dict(color=lincol[i], width=4),
                                ),
                                row=1, col=1  # Specify the subplot (row and column)
                            )
                        fig.update_xaxes(dict(tickfont=dict(color='black', size=11),showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True), row=1, col=1)
                        fig.update_yaxes(dict(showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True),row=1, col=1)
    
                        fig.update_xaxes(dict(tickfont=dict(color='black', size=11),showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True), row=1, col=2)
                        fig.update_yaxes(dict(showgrid=True, gridwidth=0.8, gridcolor='black', zeroline=False, showline=True),row=1, col=2)
                        fig.add_trace(go.Scatter(x=Vsh_clavier, y=df_fill.DEPTH, mode='lines', name='Vsh_clavier (V/V)', line=dict(color='blue')), row=1, col=2)
                        fig.update_yaxes(title_text=curvename(df_unit,[deps])[0], autorange='reversed', gridwidth=0.8)

                        fig.update_traces(line=dict(color='brown'))
                        fig.update_layout(
                            plot_bgcolor='white',
                            width=600, 
                            height=800,
                        )

                        fig.update_layout(
                            title_text='<b>Volume of shale (Vsh_clavier)</b>',
                            title_font=dict(size=25, family='Arial', color='black'),
                            width=600,
                        )
                        c1W.plotly_chart(fig)
                        df_fill['Vsh'] = Vsh_clavier
                        df_fill['Vsh'] = df_fill['Vsh'].interpolate(method='linear', limit_direction='both')
                        unitadder(df_unit,'Vsh','V/V')

                plot_vshale(vs)
                if st.checkbox('Shale identified zone'):
    
                    default_column = 'NPHI' if 'NPHI' in df_fill.columns else (
                        'NEUT' if 'NEUT' in df_fill.columns else (
                            'TNPH' if 'TNPH' in df_fill.columns else df_fill.columns[1]
                        )
                    )

                    selected_column_NPHI = vs2.selectbox('Property2:', df_fill.columns, index=df_fill.columns.get_loc(default_column) if default_column in df_fill.columns else 1)
                    # tot_val=2

                    default_column2 = 'RESD' if 'RSED' in df_fill.columns else (
                        'RT' if 'RT' in df_fill.columns else (
                            'AT90' if 'AT90' in df_fill.columns else df_fill.columns[1]
                        )
                    )
                    selected_column_RESD = vs1.selectbox('Property1:',df_fill.columns, index=df_fill.columns.get_loc(default_column2) if default_column2 in df_fill.columns else 1)
                    if selected_column_NPHI is not None and selected_column_RESD is not None:
                        max_value=df_fill["DEPTH"].min()
                        min_value=df_fill["DEPTH"].max()
                        fig = plt.figure(figsize=(22, 10))                
                        # Define grid layout
                        grid = plt.GridSpec(8, 7, wspace=0.4, hspace=0.3)
                        # Create the individual subplots
                        ax1 = plt.Subplot(fig, grid[0:8, 0])
                        ax3 = plt.Subplot(fig, grid[0:8, 1])
                        ax4 = plt.Subplot(fig, grid[0:8, 2])
                        ax5 = plt.Subplot(fig, grid[0:8, 3])
                        ax6 = plt.Subplot(fig, grid[0:2, 4:7])
                        ax7 = plt.Subplot(fig, grid[3:5, 4:7])
                        ax8 = plt.Subplot(fig, grid[6:8, 4:7])
                        # Add subplots to the figure
                        fig.add_subplot(ax1)
                        fig.add_subplot(ax3)
                        fig.add_subplot(ax4)
                        fig.add_subplot(ax5)
                        fig.add_subplot(ax6)
                        fig.add_subplot(ax7)
                        fig.add_subplot(ax8)
                        ax1.plot(df_fill[selected_column_CALI], df_fill.DEPTH, lw=0.9, color='blue')
                        ax1.fill_betweenx(df_fill.DEPTH, df_fill[selected_column_BS], df_fill[selected_column_CALI], facecolor='yellow')
                        ax1.set_xlabel(curvename(df_unit,[selected_column_CALI])[0], color='b', fontsize=18)
                        ax1.set_ylabel(curvename(df_unit,[deps])[0])
                        ax1.set_ylim(max_value, min_value)  # Reversed the y-axis limits
                        ax1.set_xlim(5, 15)
                        ax1.tick_params(axis='x', colors='b',labeltop=True)
                        ax1.spines['top'].set_edgecolor('b')
                        ax1.xaxis.set_label_position('top')
                        ax1.grid(which='both', color='black', axis='both', alpha=0.5, linestyle='--', linewidth=0.8)
                        ax11 = ax1.twiny()
                        ax11.plot(df_fill[selected_column_BS], df_fill.DEPTH, lw=0.9, color='red', linestyle='dashed')
                        ax11.set_xlim(5, 15)
                        ax11.tick_params(axis='x', colors='r')
                        ax11.spines['top'].set_edgecolor('r')
                        ax11.spines['top'].set_position(("axes", 1.06))
                        ax11.set_xlabel('Bit size', color='r', fontsize=18)
                        ax11.xaxis.set_label_position('top')
                        ax1.xaxis.set_ticks_position('top')

                        for depth, is_condition_met in zip(df_fill.DEPTH, condition_bad):
                            if is_condition_met:
                                ax1.axhline(y=depth, color='red', alpha=0.05)
                        ax3.plot(df_fill.Vsh, df_fill.DEPTH, lw=0.9, color='b')
                        ax3.set_xlabel(curvename(df_unit,['Vsh'])[0], color='b', fontsize=18)
                        ax3.set_ylim(max_value, min_value) 
                        ax3.tick_params(axis='x', colors='b', top=True,labeltop=True)
                        ax3.spines['top'].set_edgecolor('b')
                        ax3.xaxis.set_label_position('top')
                        ax3.grid(which='both', color='black', axis='both', alpha=0.5, linestyle='--', linewidth=0.8)
                        # Rshc calculation
                        Vshc=df_fill['Vsh']
                        x = np.percentile(Vshc, 95)
                        Rshc = []
                        Dshc = []
                        NPsh=[]
                        for i in Vshc.index:
                            if Vshc.loc[i] >= x and condition_good.loc[i]:
                                Rshc.append(df_fill[selected_column_RESD].loc[i])
                                Dshc.append(df_fill['DEPTH'].loc[i])
                                NPsh.append(df_fill[selected_column_NPHI].loc[i])
                        Rshc = np.array(Rshc)
                        Rshc_mean = Rshc.mean()
                        ax4.plot(df_fill[selected_column_RESD], df_fill['DEPTH'], lw=1, color='black', label=selected_column_RESD)
                        ax4.scatter(Rshc, Dshc, s=30, color='red', label='Rsh')
                        ax4.set_xlabel(curvename(df_unit,[selected_column_RESD])[0], color='black', fontsize=18)
                        ax4.set_ylim(max_value, min_value) 
                        ax4.tick_params(axis='x', colors='k', top=True,labeltop=True)
                        ax4.spines['top'].set_edgecolor('k')
                        ax4.xaxis.set_label_position('top')
                        ax4.grid(which='both', color='black', axis='both', alpha=0.5, linestyle='--', linewidth=0.8)
                        ax4.set_xscale('log')
                        ax5.plot(df_fill[selected_column_NPHI], df_fill['DEPTH'], lw=1, color='black', label=selected_column_RESD)
                        ax5.scatter(NPsh, Dshc, s=30, color='b', label='Rsh')
                        ax5.set_xlabel(curvename(df_unit,[selected_column_NPHI])[0], color='k', fontsize=18)
                        ax5.set_ylim(max_value, min_value) 
                        ax5.tick_params(axis='x', colors='k', top=True,labeltop=True)
                        ax5.spines['top'].set_edgecolor('k')
                        ax5.xaxis.set_label_position('top')
                        ax5.grid(which='both', color='black', axis='both', alpha=0.5, linestyle='--', linewidth=0.8)
                        max_value_depth=max(df_fill['DEPTH'].iloc[0],df_fill['DEPTH'].iloc[-1])
                        min_value_depth=min(df_fill['DEPTH'].iloc[0],df_fill['DEPTH'].iloc[-1])
                        ax1.set_ylim(max_value_depth,min_value_depth)
                        ax3.set_ylim(max_value_depth,min_value_depth)
                        ax4.set_ylim(max_value_depth,min_value_depth)
                        ax5.set_ylim(max_value_depth,min_value_depth)
                        # Define your data
                        data_gr = df_fill[selected_column_GR]
                        data_rshc = Rshc
                        data_nphi_shale = NPsh
                        # Plot histograms
                        ax6.hist(data_gr, bins=30, color='green', alpha=0.7, edgecolor='black')
                        ax6.set_xlabel(curvename(df_unit,[selected_column_GR])[0], fontsize=18)
                        ax6.set_ylabel('Frequency', fontsize=16)
                        ax6.set_title('GR Histogram', fontsize=20)
                        ax7.hist(data_rshc, bins=30, color='red', alpha=0.7, edgecolor='black')
                        ax7.set_xlabel(curvename(df_unit,[selected_column_RESD])[0], fontsize=18)
                        ax7.set_ylabel('Frequency', fontsize=16)
                        ax7.set_title(selected_column_RESD +' Shale-zone Histogram', fontsize=20)
                        ax8.hist(data_nphi_shale, bins=30, color='blue', alpha=0.7, edgecolor='black')
                        ax8.set_xlabel('NPHIshale', fontsize=18)
                        ax8.set_ylabel('Frequency', fontsize=16)
                        ax8.set_title(selected_column_NPHI +' Shale-Zone Histogram', fontsize=20)
                        # Add percentile lines and mean line
                        percentiles_gr = np.percentile(data_gr, [5, 50, 95])
                        percentiles_rshc = np.percentile(data_rshc, [5, 50, 95])
                        percentiles_nphi_shale = np.percentile(data_nphi_shale, [5, 50, 95])
                        ax6.axvline(percentiles_gr[0], color='purple', linestyle='--', label='5th Percentile', lw = 3)
                        ax6.axvline(percentiles_gr[1], color='orange', linestyle='--', label='50th Percentile (Mean)', lw = 3)
                        ax6.axvline(percentiles_gr[2], color='blue', linestyle='--', label='95th Percentile', lw = 3)
                        ax7.axvline(percentiles_rshc[0], color='purple', linestyle='--', label='5th Percentile', lw = 3)
                        ax7.axvline(percentiles_rshc[1], color='orange', linestyle='--', label='50th Percentile (Mean)', lw = 3)
                        ax7.axvline(percentiles_rshc[2], color='blue', linestyle='--', label='95th Percentile', lw = 3)
                        ax8.axvline(percentiles_nphi_shale[0], color='purple', linestyle='--', label='5th Percentile', lw = 3)
                        ax7.axvline(percentiles_rshc[2], color='blue', linestyle='--', label='95th Percentile', lw = 3)
                        ax8.axvline(percentiles_nphi_shale[0], color='purple', linestyle='--', label='5th Percentile', lw = 3)
                        ax8.axvline(percentiles_nphi_shale[1], color='orange', linestyle='--', label='50th Percentile (Mean)', lw = 3)
                        ax8.axvline(percentiles_nphi_shale[1], color='orange', linestyle='--', label='50th Percentile (Mean)', lw = 3)
                        ax8.axvline(percentiles_nphi_shale[2], color='blue', linestyle='--', label='95th Percentile', lw = 3)
                        # Add legend to ax6 (you can add it to other subplots as needed)
                        # Adjust parameters like rowspan, colspan, and sizes as needed.
                        plt.suptitle("Volume of shale Calculation", fontsize=40, y=1.01)
                        st.pyplot(fig)
                    else:
                        st.write('Complete the selection for properties')
                return df_fill,selected_column_GR
            df_fill,selected_column_GR = vshle()    
        l_df=pd.DataFrame()
        g_df=pd.DataFrame()
            
             # ---------------------------------------------------------------------LITH LOG
  
        ##########################################################################
        #                  Lithology Identification                              #
        ########################################################################## 
        st.write('-------------------------------------------------------------------------------------------------------------------------------------')

        # container1 = st.container(border=True)
        css_code = """
            <style>
                div[data-testid="stHorizontalBlock"] div[data-testid="stContainer"] {
                    border: 2px solid red; /* Change 'red' to the desired color */
                    border-radius: 5px; /* Optional: add border-radius for rounded corners */
                    padding: 10px; /* Optional: add padding for better visibility */
                }
            </style>
        """

        # Display the custom CSS using Markdown
        st.markdown(css_code, unsafe_allow_html=True)


        lith,gas=st.columns(2)  
        # Radio button for lithology identification
        lithology_operation = lith.radio('Lithology Identification Operation', ['Not Selected','Selected'])
        # Radio button for gas bearing zone identification
        gas_zone_operation = gas.radio('Gas-bearing Zone Identification Operation', ['Not Selected','Selected'])    
        if lithology_operation == 'Selected':
            with st.expander("Lithogy Identification"):

                # @st.cache_data(experimental_allow_widgets=True)
                # def lithi():
                lt1,lt2=st.columns(2)
                with lt1:
                    # def toggle():
                    #     st.session_state.button = not st.session_state.button

                    # st.write('For improved visibility: collapses sidebar ')
                    # st.button("Click here",key='sidebar_callapse_key', on_click=toggle)


                    st.subheader("Lithology ") 
                    lith_col = dfMN['NPHI'].to_list() + dfMN['GR'].to_list() + dfMN['PEF'].to_list() + dfMN['RHOB'].to_list()
                    matched_mnemonics_lith_columns = [curve_item for curve_item in las_file.keys() if curve_item in lith_col]

                    default_selection = matched_mnemonics_lith_columns if matched_mnemonics_lith_columns else df_fill.columns[1]

                    valid_default_selection = [item for item in default_selection if item in df_fill.columns]
                    column_name = st.multiselect('Choose', df_fill.columns, default=valid_default_selection)
                    if lt1.checkbox('Completed the selection for the lithology log',key='whoknows'):
                        if column_name and column_name[0] is not None:
                            num_lithlog =len(column_name)
                            curve_name= curvename(df_unit,column_name)
                            clicked_data = []   
                            depth_boundary=[]
                            fig = make_subplots(rows=1, cols=num_lithlog+1, shared_yaxes=True, subplot_titles=curvename(df_unit,[selected_column_CALI])+curve_name)
                            fig.add_trace(go.Scatter(x=df_fill[selected_column_CALI], y=df_fill['DEPTH'], line=dict(width=1, color='blue'),name=curvename(df_unit,[selected_column_CALI])[0]), row=1, col=1)
                            for depth, is_condition_met in zip(df_fill.DEPTH, condition_bad):
                                    if is_condition_met:
                                        fig.add_trace(go.Scatter(
                                            x=[df_fill[selected_column_CALI].min(), df_fill[selected_column_CALI].max()],
                                            y=[depth, depth],
                                            mode='lines',
                                            line=dict(width=0.3, color='red', dash='solid'),
                                            name=f'Condition - Depth: {depth}',
                                            showlegend=False
                                        ), row=1, col=1)
                            fig.update_xaxes(title_text=selected_column_CALI, row=1, col=1)
                            subplot_colors = ['green', 'blue', 'red', 'purple', 'orange']  # Add more colors if needed
                            color_iterator = itertools.cycle(subplot_colors)
                            for i in range(len(column_name)):
                                scatter_plot = go.Scatter(x=df_fill[column_name[i]], y=df_fill['DEPTH'], mode='lines', name=curve_name[i], line=dict(color=subplot_colors[i]))
                                fig.add_trace(scatter_plot, row=1, col=i + 2)
                                fig.update_yaxes(autorange='reversed', row=1, col=i + 2)
                                fig.update_xaxes(title_text=curve_name[i], row=1, col=i + 2)
                            fig.update_layout(width=450, height=900)
                            fig.update_yaxes(autorange='reversed', gridwidth=0.8)
                            fig.update_layout(
                                # title_text='<b>Lithology Identification</b>',
                                title_text='Lithology Identification',
                                title_font=dict(size=30, family='Arial', color='black'),
                                width=800,
                            )
                            l_df = pd.DataFrame({"Y": []})
                            aq=st.radio('Boundary picking method',['Picking from Plot','Mannual Input'])
                            if aq=='Picking from Plot':


                                # with st.spinner('Wait for it...'):
                                #     time.sleep(time.time() - start_time)
                                    component_value = plotly_events(fig)
                                    if component_value:
                                        st.subheader("Clicked Points:")
                                        for point in component_value:
                                            st.write(f"X: {point['x']:.2f}, Y: {point['y']:.2f}")
                                            clicked_data.append({"X": point['x'], "Y": point['y']})
                                    l_df = pd.DataFrame(clicked_data)
                            if aq=='Mannual Input':


                                # with st.spinner('Wait for it...'):
                                #     time.sleep(time.time() - start_time)
                                    st.plotly_chart(fig)
                                    hg,gh=st.columns(2)
                                    num_zones = hg.number_input("How many depth zones do you want to define?", min_value=1, step=1)
                                    l_df = pd.DataFrame({"Y": []})
                                    depth_values = []
                                    for i in range(num_zones - 1):
                                        bottom_boundary = gh.number_input(f"Enter bottom boundary for Zone {i + 1}:", min_value=df_fill['DEPTH'].min() if i == 0 else depth_values[-1], step=0.1)
                                        depth_values.append(bottom_boundary)
                                    l_df = pd.DataFrame({"Y": depth_values})
                            if st.button("Finish  ",key='hyn'):
                                depth_boundary_inner = np.array(l_df['Y'])
                                end1 = df_fill["DEPTH"].iloc[-1]
                                end2 = df_fill["DEPTH"].iloc[0]
                                depth_boundary =np.concatenate(([end1, end2], depth_boundary_inner))
                                depth_boundary = np.sort(depth_boundary)
                                fig = make_subplots(rows=1, cols=num_lithlog+1, shared_yaxes=True, subplot_titles=[selected_column_CALI]+column_name)
                                fig.add_trace(go.Scatter(x=df_fill[selected_column_CALI], y=df_fill['DEPTH'], line=dict(width=1, color='blue'), showlegend=False), row=1, col=1)
                                for depth, is_condition_met in zip(df_fill.DEPTH, condition_bad):
                                        if is_condition_met:
                                            fig.add_trace(go.Scatter(
                                                x=[df_fill[selected_column_CALI].min(), df_fill[selected_column_CALI].max()],
                                                y=[depth, depth],
                                                mode='lines',
                                                line=dict(width=0.3, color='red', dash='solid'),
                                                name=f'Condition - Depth: {depth}',
                                                showlegend=False
                                            ), row=1, col=1)
                                fig.update_xaxes(title_text=selected_column_CALI, row=1, col=1)
                                #colors = ['red', 'blue', 'green', 'purple', 'orange']
                                subplot_colors = ['green', 'blue', 'red', 'purple', 'orange']  # Add more colors if needed
                                color_iterator = itertools.cycle(subplot_colors)
                                for i in range(len(column_name)):
                                    scatter_plot = go.Scatter(x=df_fill[column_name[i]], y=df_fill['DEPTH'], mode='lines', name=column_name[i], line=dict(color=subplot_colors[i]))
                                    fig.add_trace(scatter_plot, row=1, col=i + 2)
                                    fig.update_yaxes(autorange='reversed', row=1, col=i + 2)
                                    for depth_value in depth_boundary:
                                        fig.add_shape(
                                            go.layout.Shape(
                                                type='line',
                                                x0=df_fill[column_name[i]].min(),
                                                x1=df_fill[column_name[i]].max(),
                                                y0=depth_value,
                                                y1=depth_value,
                                                line=dict(color='magenta', width=2),
                                                xref=f'x{i + 2}',
                                                yref='y'
                                            )
                                        )
                                    for j in range(len(depth_boundary) - 1):
                                        lower_boundary = depth_boundary[j]
                                        upper_boundary = depth_boundary[j + 1]
                                        section_data = df_fill[(df_fill['DEPTH'] > lower_boundary) & (df_fill['DEPTH'] < upper_boundary)]
                                        mean_value = section_data[column_name[i]].mean()
                                        fig.add_shape(
                                            go.layout.Shape(
                                                type='line',
                                                x0=mean_value,
                                                x1=mean_value,
                                                y0=section_data['DEPTH'].min(),
                                                y1=section_data['DEPTH'].max(),
                                                line=dict(color='orange', width=1.7),
                                                xref=f'x{i + 2}',
                                                yref='y'
                                            )
                                        )
                                fig.update_layout(width=400, height=800)
                                fig.update_layout(
                                    # title_text='<b>Lithology Identification</b>',
                                    title_text='Lithology Identification',
                                    title_font=dict(size=30, family='Arial', color='black'),
                                    width=800,
                                )
                                st.plotly_chart(fig)





                        @st.cache_data()
                        def make_facies_log_plot(df_fill, col_lith,n_cc):
                            # n_cc = st.slider('Enter the number for the clusters:', min_value=2, max_value=10, value=5)

                            def get_cmap(n, name='hsv'):
                                return plt.cm.get_cmap(name, n)

                            facies_colors = get_cmap(n_cc, name='hsv')

                            logs = df_fill[col_lith]

                            logs.interpolate(method='linear', limit_direction='both', axis=0, inplace=True)
                            # Standardize the data
                            scaled_data = StandardScaler().fit_transform(logs)

                            # Factor Analysis
                            fa_model = FactorAnalysis(n_components=n_cc)
                            factor_data = fa_model.fit_transform(scaled_data)

                            # K-Means clustering
                            kmeans = KMeans(n_clusters=n_cc, random_state=0)
                            kmeans.fit(factor_data)

                            # Assign cluster labels to the logs
                            logs['Cluster'] = kmeans.labels_

                            cmap_facies = plt.cm.get_cmap('tab20', n_cc)

                            ztop = df_fill.DEPTH.min()
                            zbot = df_fill.DEPTH.max()

                            cluster = np.repeat(np.expand_dims(logs['Cluster'].values, 1), 100, 1)

                            f, ax = plt.subplots(nrows=1, ncols=len(col_lith) + 1, figsize=(8, 10))

                            for i in range(len(col_lith)):
                                log_name = col_lith[i]
                                color = f'C{i}'
                                ax[i].plot(logs[log_name], df_fill.DEPTH, color=color, label=log_name)

                            im = ax[len(col_lith)].imshow(cluster, interpolation='none', aspect='auto',
                                                           cmap=cmap_facies, vmin=0, vmax=n_cc - 1)

                            divider = make_axes_locatable(ax[len(col_lith)])
                            cax = divider.append_axes("right", size="20%", pad=0.05)
                            cbar = plt.colorbar(im, cax=cax, ticks=range(n_cc))

                            clusti = [f'Clust {i + 1}' for i in range(n_cc)]
                            cbar.set_label((10 * ' ').join(clusti), fontsize=14)

                            for i in range(len(ax) - 1):
                                ax[i].set_ylim(ztop, zbot)
                                ax[i].invert_yaxis()
                                ax[i].grid()
                                ax[i].locator_params(axis='x', nbins=3)
                                ax[i].set_xlabel(col_lith[i], fontsize=16)

                                if i != 0:
                                    ax[i].set_yticklabels([])

                            if df_fill['DEPTH'].iloc[0] > df_fill['DEPTH'].iloc[-1]:
                                ax[len(col_lith)].invert_yaxis()
                            else:
                                pass
                            ax[len(col_lith)].set_xlabel('Facies', fontsize=16)
                            ax[len(col_lith)].set_yticklabels([])
                            ax[len(col_lith)].set_xticklabels([])

                            st.pyplot(f)






                        with lt2:
                            st.title('')
                            st.title('')
                            st.title('')
                            st.title('')
                            st.title('')
                            st.title('')
                            st.title('')
                            # st.title(''   )
                            # st.title('')
                            st.subheader("Unsupervised Clustering Guide")
                            with st.spinner('Wait for it...'):
                                time.sleep(time.time() - start_time)
                            if column_name and column_name[0] is not None:
                                n_cc = st.number_input('Enter the number for the clusters:', value=10)
                
                                f = make_facies_log_plot(df_fill, column_name,n_cc)
                    else:
                        st.warning('Please selection of the columns.')

                    st.write("")
                    st.write("")






                # return l_df
                # l_df = lithi()                

            ##########################################################################
            #                  Gas bearing zone identication                         #
            ##########################################################################  
            g_df = []
        if gas_zone_operation == 'Selected':
            with st.expander("Gas Bearing Zone And Triple Combo"):


                # def toggle():
                #     st.session_state.button = not st.session_state.button
                # st.write('For improved visibility: collapses sidebar ')
                # st.button("Click here ",key='sidebar_callapse_key_gas', on_click=toggle)
                tcg,tcr,tcd,tcn=st.columns(4)
                gb1,gb2=st.columns(2)
                with gb1:

                    st.subheader("Gas Bearing Zone")

                    selected_column_GR=tcg.selectbox('Gamma Ray', df_fill.columns, index=well_df.columns.get_loc(default_column_GR) if default_column_GR in well_df.columns else 1)

                    selected_column_RESD=tcr.selectbox('Resistivity:',df_fill.columns, index=well_df.columns.get_loc(default_column_RESD) if default_column_RESD in well_df.columns else 1)

                    selected_column_RHOB=tcd.selectbox('RHOB', df_fill.columns, index=well_df.columns.get_loc(default_column_RHOB) if default_column_RHOB in well_df.columns else 1)

                    selected_column_NPHI=tcn.selectbox('NPHI', df_fill.columns, index=well_df.columns.get_loc(default_column_NPHI) if default_column_NPHI in well_df.columns else 1)

                    # @st.cache_data(experimental_allow_widgets=True)
                    # def gzone()
                    #data = df_fill.copy()
                    #selected_column_RHOB = st.selectbox('RHOB', data.columns, index=data.columns.get_loc('RHOB') if 'RHOB' in data.columns else 1)
                    if selected_column_NPHI is not None and selected_column_RESD is not None and selected_column_GR is not None and selected_column_RHOB is not None:
                        clicked_data = []
                        fig = make_subplots(rows=1, cols=4, shared_yaxes=True, horizontal_spacing=0.053,subplot_titles=[curvename(df_unit,[selected_column_CALI])[0],curvename(df_unit,[selected_column_GR])[0],'          '+curvename(df_unit,[selected_column_RHOB])[0]+' cross ' + curvename(df_unit,[selected_column_NPHI])[0]])
                        fig.add_trace(go.Scatter(x=df_fill[selected_column_CALI], y=df_fill['DEPTH'], line=dict(width=1, color='blue'),showlegend=False), row=1, col=1)
                        for depth, is_condition_met in zip(df_fill.DEPTH,condition_bad):
                                if is_condition_met:
                                    fig.add_trace(go.Scatter(
                                        x=[df_fill[selected_column_CALI].min(), df_fill[selected_column_CALI].max()],  
                                        y=[depth, depth],  
                                        mode='lines',
                                        line=dict(width=0.3, color='red', dash='solid'),  
                                        name=f'Condition - Depth: {depth}',  
                                        showlegend=False  
                                    ), row=1, col=1)
                        fig.add_trace(go.Scatter(x=df_fill[selected_column_GR], y=df_fill['DEPTH'], line=dict(width=0.5, color='green'),name=selected_column_GR), row=1, col=2)
                        # Add the first trace (TNPH) with X and Y swapped
                        trace1 = go.Scatter(x=3 - df_fill[selected_column_NPHI]*(15/6), y=df_fill['DEPTH'], line=dict(width=0.8, color='blue'), name=selected_column_NPHI+'')
                        fig.add_trace(trace1,row=1, col=3)
                        # Add the second trace (RHOB) with X and Y swapped
                        trace2 = go.Scatter(x=df_fill[selected_column_RHOB], y=df_fill['DEPTH'], line=dict(width=0.8, color='brown'), name=selected_column_RHOB)
                        fig.add_trace(trace2,row=1, col=3)
                        fig.update_yaxes(autorange='reversed', gridwidth=0.8)
                        fig.update_layout(title='Overlay plot of NPHI & RHOB',width=800, height=900)  # Adjust width and height as needed
                        fig.update_layout(
                            title_text='<b>Overlay plot of NPHI & RHOB</b>',
                            title_font=dict(size=30, family='Arial', color='black'),
                            width=800,
                        )
                        baq = st.radio("Select Input Type", ["Picking from plot","Mannual Input"])
                        g_df = pd.DataFrame({"Y": []})
                        if baq == "Picking from plot":
                        # if st.checkbox('Auto Pick '):
                            component_value = plotly_events(fig)
                            if component_value:
                                st.subheader("Clicked Points:")
                                for point in component_value:
                                    st.write(f"X: {point['x']:.2f}, Y: {point['y']:.2f}")
                                    # Append the clicked data to the list
                                    clicked_data.append({"X": point['x'], "Y": point['y']})
                            g_df = pd.DataFrame(clicked_data)

                        if baq == "Mannual Input":
                            st.plotly_chart(fig)
                            num_gas_zones = st.number_input("How many gas bearing zones do you want to define?", min_value=1, step=1)
                            depth_values = []
                            kl,lk=st.columns(2)
                            for i in range(num_gas_zones):
                                top_boundary = kl.number_input(f"Enter top boundary for Gas Zone {i + 1}:", min_value=df_fill['DEPTH'].min() if i == 0 else depth_values[-1], step=0.1)
                                bottom_boundary = lk.number_input(f"Enter bottom boundary for Gas Zone {i + 1}:", min_value=top_boundary, step=0.1)
                                depth_values.append(top_boundary)
                                depth_values.append(bottom_boundary)
                            Y = depth_values  # Save depth values in the variable Y
                            g_df = pd.DataFrame({"Y": Y})
                        if st.button("Finish "):
                            clicked_data = []
                            gas_zones_boundary = np.array(g_df['Y'])
                            gas_zones_boundary = np.sort(gas_zones_boundary)
                            fig = make_subplots(rows=1, cols=4, shared_yaxes=True, horizontal_spacing=0.053,subplot_titles=[curvename(df_unit,[selected_column_CALI])[0],curvename(df_unit,[selected_column_GR])[0],'          '+curvename(df_unit,[selected_column_RHOB])[0]+' cross ' + curvename(df_unit,[selected_column_NPHI])[0]])
                            fig.add_trace(go.Scatter(x=df_fill[selected_column_CALI], y=df_fill['DEPTH'], line=dict(width=1, color='blue'),showlegend=False), row=1, col=1)
                            for depth, is_condition_met in zip(df_fill.DEPTH,condition_bad):
                                    if is_condition_met:
                                        fig.add_trace(go.Scatter(
                                            x=[df_fill[selected_column_CALI].min(),df_fill[selected_column_CALI].max()],  
                                            y=[depth, depth],  
                                            mode='lines',
                                            line=dict(width=0.3, color='red', dash='solid'),  
                                            name=f'Condition - Depth: {depth}',  
                                            showlegend=False  
                                        ), row=1, col=1)
                            fig.add_trace(go.Scatter(x=df_fill[selected_column_GR], y=df_fill['DEPTH'], line=dict(width=0.5, color='green'),name=selected_column_GR), row=1, col=2)
                            # Add the first trace (TNPH) with X and Y swapped
                            trace1 = go.Scatter(x=3 - df_fill[selected_column_NPHI]*(15/6), y=df_fill['DEPTH'], line=dict(width=1.5, color='blue'), name=selected_column_NPHI)
                            fig.add_trace(trace1,row=1, col=3)
                            # Add the second trace (RHOB) with X and Y swapped
                            trace2 = go.Scatter(x=df_fill[selected_column_RHOB], y=df_fill['DEPTH'], line=dict(width=1.5, color='brown'), name=selected_column_RHOB)
                            fig.add_trace(trace2,row=1, col=3)
                            for depth_value in g_df['Y']:
                                fig.add_shape(
                                    go.layout.Shape(
                                        type='line',
                                        x0=df_fill[selected_column_GR].min(),
                                        x1=df_fill[selected_column_GR].max(),
                                        y0=depth_value,
                                        y1=depth_value,
                                        line=dict(color='magenta', width=2),
                                        xref='x2',
                                        yref='y'
                                    )
                                )
                                fig.add_shape(
                                    go.layout.Shape(
                                        type='line',
                                        x0=min(df_fill[selected_column_RHOB].min(),min(3 - df_fill[selected_column_NPHI]*(15/6))),
                                        x1=max(df_fill[selected_column_RHOB].max(),max(3 - df_fill[selected_column_NPHI]*(15/6))),
                                        y0=depth_value,
                                        y1=depth_value,
                                        line=dict(color='magenta', width=2),
                                        xref='x3',
                                        yref='y'
                                    )
                                )
                            num_gas_zones=int(len((gas_zones_boundary ))/2)
                            for j in range(num_gas_zones):
                                    lower_boundary = gas_zones_boundary [2*j]
                                    upper_boundary = gas_zones_boundary [2*j + 1]
                                    section_data = df_fill[(df_fill['DEPTH'] > lower_boundary) & (df_fill['DEPTH'] < upper_boundary)]
                                    min_value = min(df_fill[selected_column_RHOB].min(),min(3 - df_fill[selected_column_NPHI]*(15/6)))
                                    max_value = max(df_fill[selected_column_RHOB].max(),max(3 - df_fill[selected_column_NPHI]*(15/6)))
                                    fig.add_shape(
                                        go.layout.Shape(
                                            type='line',
                                            x0=min_value,
                                            x1=min_value,
                                            y0=section_data['DEPTH'].min(),
                                            y1=section_data['DEPTH'].max(),
                                            line=dict(color='magenta', width=1),
                                            xref='x3',
                                            yref='y'
                                        )
                                    )
                                    fig.add_shape(
                                        go.layout.Shape(
                                            type='line',
                                            x0=max_value,
                                            x1=max_value,
                                            y0=section_data['DEPTH'].min(),
                                            y1=section_data['DEPTH'].max(),
                                            line=dict(color='magenta', width=1.5),
                                            xref='x3',
                                            yref='y'
                                        )
                                    )
                                    min_value = df_fill[selected_column_GR].min()
                                    max_value = df_fill[selected_column_GR].max()
                                    fig.add_shape(
                                        go.layout.Shape(
                                            type='line',
                                            x0=max_value,
                                            x1=max_value,
                                            y0=section_data['DEPTH'].min(),
                                            y1=section_data['DEPTH'].max(),
                                            line=dict(color='magenta', width=1.5),
                                            xref='x2',
                                            yref='y'
                                        )
                                    )
                                    min_value = df_fill[selected_column_GR].min()
                                    max_value = df_fill[selected_column_GR].max()
                                    fig.add_shape(
                                        go.layout.Shape(
                                            type='line',
                                            x0=min_value,
                                            x1=min_value,
                                            y0=section_data['DEPTH'].min(),
                                            y1=section_data['DEPTH'].max(),
                                            line=dict(color='magenta', width=1.5),
                                            xref='x2',
                                            yref='y'
                                        )
                                    )
                            fig.update_yaxes(autorange='reversed', gridwidth=0.8)
                            fig.update_layout(title='Overlay plot of NPHI & RHOB',width=800, height=900)  # Adjust width and height as needed
                            fig.update_layout(
                                title_text='<b>Overlay plot of NPHI & RHOB</b>',
                                title_font=dict(size=30, family='Arial', color='black'),
                                width=800,
                                )
                            gb1.plotly_chart(fig)

                    ##########################################################################
                        #                          Triple Combo plot                             #
                    ########################################################################## 
                
                with gb2:
                    st.subheader("")
                    st.title("")
                    st.title("")
                    st.title("")    
                    st.title("")
                    st.write("")
                    st.subheader('Triple Combo Plot')
    
                    @st.cache_data(experimental_allow_widgets=True)
                    def create_triple_combo_plot(selected_column_NPHI,selected_column_RESD,selected_column_GR,selected_column_RHOB):
                        top_depth = df_fill['DEPTH'].min()
                        bot_depth = df_fill['DEPTH'].max()
                        plot_h, plot_w, title_size, title_height, line_width = 16 ,12, 12, 1.0, 1
                        # Define track parameters
                        gr_params = {'color': 'teal', 'trackname': curvename(df_unit,[selected_column_GR])[0], 'left': 0, 'right': 200, 'cutoff': 60, 'base': 0,
                                     'sand_color': 'gold', 'shale_color': 'lightslategray', 'div': 5}
                        res_params = {'color': 'darkorange', 'trackname': curvename(df_unit,[selected_column_RESD])[0], 'left': 0.2, 'right': 20000, 'cutoff': 100, 'shading_color': 'navajowhite'}
                        den_params = {'color': 'brown', 'trackname': curvename(df_unit,[selected_column_RHOB])[0], 'left': 1.95, 'right': 2.95}
                        neu_params = {'color': 'darkslategray', 'trackname': curvename(df_unit,[selected_column_NPHI])[0], 'mean': np.nanmean(df_fill[selected_column_NPHI]),
                                      'left1': 0.45, 'right1': -0.15, 'left2': 45, 'right2': -15}
                        den_neu_params = {'div': 5, 'xover_color': 'gold', 'sep_color': 'lightslategray'}
                        # Plot setup
                        fig, axes = plt.subplots(1, 3, figsize=(plot_w, plot_h))
                        axes = axes.flatten()
                        for ax in axes:
                            ax.minorticks_on()
                            ax.grid(which='major', color='silver', linestyle='-')
                            ax.grid(which='minor', color='lightgrey', linestyle=':', axis='y')
                            ax.xaxis.set_ticks_position("top")
                            ax.xaxis.set_label_position("top")
                        ax1 = axes[0]
                        ax1.plot(selected_column_GR, "DEPTH", data=df_fill, color=gr_params['color'], lw=line_width)
                        ax1.set_xlabel(gr_params['trackname'])
                        ax1.set_xlim(gr_params['left'], gr_params['right'])
                        ax1.set_ylim(bot_depth, top_depth)
                        ax1.fill_betweenx(df_fill['DEPTH'], gr_params['base'], df_fill[selected_column_GR], where=(gr_params['cutoff'] >= df_fill[selected_column_GR]),
                                          interpolate=True, color=gr_params['sand_color'], linewidth=0, alpha=0.8)
                        ax1.fill_betweenx(df_fill['DEPTH'], gr_params['base'], df_fill[selected_column_GR], where=(gr_params['cutoff'] <= df_fill[selected_column_GR]),
                                          interpolate=True, color=gr_params['shale_color'], linewidth=0, alpha=0.8)
                        ax2 = axes[1]
                        ax2.plot(selected_column_RHOB, "DEPTH", data=df_fill, color=den_params['color'], lw=line_width)
                        ax2.set_xlabel(den_params['trackname'], color='brown')
                        ax2.set_xlim(den_params['left'], den_params['right'])
                        ax2.set_ylim(bot_depth, top_depth)
                        ax4 = ax2.twiny()
                        ax4.plot(selected_column_NPHI, "DEPTH", data=df_fill, color=neu_params['color'], lw=line_width)
                        ax4.set_xlabel(neu_params['trackname'], color='darkslategray')
                        ax4.spines['top'].set_position(("axes", 1.04))
                        ax4.set_xlim(neu_params['left1'] if neu_params['mean'] < 1 else neu_params['left2'],
                                     neu_params['right1'] if neu_params['mean'] < 1 else neu_params['right2'])
                        ax2.xaxis.tick_top()
                        ax4.xaxis.tick_top()
                        ax2.tick_params(axis='x', colors='brown')
                        ax2.spines['top'].set_edgecolor('brown')
    
                        ax4.tick_params(axis='x', colors='darkslategray')
                        ax4.spines['top'].set_edgecolor('darkslategray')
                        ax2.xaxis.labelpad = 14
                        ax4.xaxis.labelpad = 10
                        ax2.xaxis.set_label_coords(0.5, 1.02)
                        ax4.xaxis.set_label_coords(0.5, 1.06)
                        ax2.xaxis.set_tick_params(pad=5)
                        ax4.xaxis.set_tick_params(pad=5)
                        x1, x2 = df_fill[selected_column_RHOB],df_fill[selected_column_NPHI]
                        x, z = np.array(ax2.get_xlim()), np.array(ax4.get_xlim())
                        nz = ((x2 - np.max(z)) / (np.min(z) - np.max(z))) * (np.max(x) - np.min(x)) + np.min(x)
                        ax2.fill_betweenx(df_fill['DEPTH'], x1, nz, where=x1 >= nz, interpolate=True, color=den_neu_params['sep_color'],
                                          linewidth=0, alpha=0.8)
                        ax2.fill_betweenx(df_fill['DEPTH'], x1, nz, where=x1 <= nz, interpolate=True, color=den_neu_params['xover_color'],
                                          linewidth=0, alpha=0.8)
    
                        ax3 = axes[2]
                        ax3.plot(selected_column_RESD, "DEPTH", data=df_fill, color=res_params['color'], lw=line_width)
                        ax3.set_xlabel(res_params['trackname'])
                        ax3.set_xlim(res_params['left'], res_params['right'])
                        ax3.set_ylim(bot_depth, top_depth)
                        ax3.semilogx()
                        ax3.fill_betweenx(df_fill['DEPTH'], res_params['cutoff'],df_fill[selected_column_RESD], where=(df_fill[selected_column_RESD] >= res_params['cutoff']),
                                          interpolate=True, color=res_params['shading_color'], linewidth=0)
                        plt.tight_layout()
                        return fig
                    if selected_column_NPHI is not None and selected_column_RESD is not None and selected_column_GR is not None and selected_column_RHOB is not None:
                        fig=create_triple_combo_plot(selected_column_NPHI,selected_column_RESD,selected_column_GR,selected_column_RHOB)
                        st.pyplot(fig)
                #     return g_df,selected_column_RHOB
                # g_df,selected_column_RHOB= gzone()
    
        if lithology_operation == 'Not Selected':
            lith.warning('lithology identification skipped.')

        if gas_zone_operation == 'Not Selected':
            gas.warning('gas-bearing zone identification skipped.')










        # container2 = st.container(border=True)
        st.write('-------------------------------------------------------------------------------------------------------------------------------------')

        st.markdown('#####  Evaluation Property')
        all_op = st.radio('Choose Operation',['NPHI Matrix & Shale correction','Total porosity Calculation','Water Saturation','Reservoir flag & NTG'])



        ###############################################################################################################################
        #    Nuetron Porosity shale correction Density Porosity calculation and plot and total porosity calculation and plot          #
        ###############################################################################################################################  
        op,po=st.columns(2)

# -------------------------------------------------------------------SHALE CORR
            ##########################################################################
            #                  Nuetron Porosity shale correction                     #
            ##########################################################################  



        if all_op in ['NPHI Matrix & Shale correction', 'Total porosity Calculation', 'Water Saturation', 'Reservoir flag & NTG']:

            with op.expander("NPHI Matrix & Shale correction:"):
                st.subheader("NPHI Matrix & Shale correction:")
                Vsh = df_fill['Vsh']
                np1,np2=st.columns(2)
                # selected_column_NPHI = st.selectbox('NPHI', df_fill.columns, index=df_fill.columns.get_loc('TNPH') if 'TNPH' in df_fill.columns else 1)  #OLD
    
                
                selected_column_NPHI = np1.selectbox('NPHI log:', df_fill.columns, index=well_df.columns.get_loc(default_column_NPHI) if default_column_NPHI in well_df.columns else 1)
                # st.cache_data
                def NPHI_matrix_correction(df_fill, selected_column_NPHI, correction, operation):
                
                    if operation == 'Addition':
                        df_fill[selected_column_NPHI] = df_fill[selected_column_NPHI] + correction
                    if operation == 'Subtraction':
                        df_fill[selected_column_NPHI] = df_fill[selected_column_NPHI] - correction
                    if operation == 'None':
                        df_fill[selected_column_NPHI] = df_fill[selected_column_NPHI]
                    return df_fill
    
                # Example usage:
                # selected_column_NPHI = 'TNPH'
                # df_fill = dfsw
                # operation = 'addition'
                # c4.write("Matrix Correction")
    
                operation = np2.selectbox("Matrix correction method:", ["None","Addition", "Substraction"], key="dfgu")
    
                if operation != 'None':
                    correction =np2.number_input("Correction", value=0.4)
                else:
                    correction=0
    
                df_fill = NPHI_matrix_correction(df_fill, selected_column_NPHI, correction, operation)
    
    
                def effective_phi(Vsh, PHI, percentile, condition_good):
                    PHIshc = []
                    x = np.percentile(Vsh, percentile)
    
                    for i in Vsh.index:
                        if Vsh.loc[i] >= x and condition_good.loc[i]:
                            PHIshc.append(PHI[i])
    
                    if not PHIshc:
                        return PHI  # No correction if PHIshc is empty
    
                    PHIshc = np.array(PHIshc)
                    PHIshc_mean = PHIshc.mean()
                    phi_correction = Vsh * PHIshc_mean
                    PHI_shale_corrected = PHI - phi_correction
    
                    return PHI_shale_corrected
                NPHI_shale_corrected = effective_phi(Vsh, df_fill[selected_column_NPHI],95, condition_good)
                # Create a figure with subplots
                fig = make_subplots(rows=1, cols=2, shared_yaxes=True, horizontal_spacing=0.03,subplot_titles=(curvename(df_unit,[selected_column_NPHI])[0],curvename(df_unit,[selected_column_NPHI])[0]+' shale_corr' ))
                
                # Add traces to the subplots
                fig.add_trace(go.Scatter(x=df_fill[selected_column_NPHI], y=df_fill['DEPTH'], line=dict(width=1.5, color='green'), name=selected_column_NPHI + ' Without shale_corr'), row=1, col=1)
                fig.add_trace(go.Scatter(x=NPHI_shale_corrected, y=df_fill['DEPTH'], line=dict(width=1.5, color='cyan'), name=selected_column_NPHI + ' After shale_corr'), row=1, col=2)
                
                fig.update_yaxes(title_text=curvename(df_unit,[deps])[0], autorange='reversed', gridwidth=0.8)
                
                # Update layout and show the figure
                fig.update_layout(width=600, height=800)  # Adjust width and height as needed
                fig.update_layout(
                            title_text='<b>Neutron Porosity Shale correction</b>',
                            title_font=dict(size=30, family='Arial', color='black'),
                            width=600,
                        )
                st.plotly_chart(fig)
                df_fill['NPHIE']=NPHI_shale_corrected
                unitadder(df_unit,'NPHIE','V/V')
    
            
            def gas_correction(DPHI, DPHI_shale_corrected, g_df, data, selected_column_NPHI):
                if not g_df.empty and len(g_df) % 2 == 0:
                    gas_zones_boundary = np.sort(g_df['Y'])
                    data['TPHI'] = np.nan  # Initialize the column with NaN
                    condition_boundary_list = []
    
                    for i in range(int(len(gas_zones_boundary) / 2)):
                        condition_boundary = (data['DEPTH'] >= gas_zones_boundary[2 * i]) & (data['DEPTH'] < gas_zones_boundary[2 * i + 1])
                        condition_boundary_list.append(condition_boundary)
                        TPHI = np.zeros(len(data['DEPTH']))
                        for j in range(len(data['DEPTH'])):
                            if condition_boundary.iloc[j]:
                                TPHI[j] = ((df_fill[selected_column_NPHI].iloc[j] ** 2 + 0.8 *DPHI.iloc[j] ** 2) / 2) ** 0.5
                                DPHI.iloc[j]=0.8 *DPHI.iloc[j]
                                DPHI_shale_corrected.iloc[j]=0.8 *DPHI_shale_corrected.iloc[j]
                            else:
                                TPHI[j] = (df_fill[selected_column_NPHI].iloc[j] + DPHI.iloc[j]) / 2
                                DPHI.iloc[j]=DPHI.iloc[j]
                                DPHI_shale_corrected.iloc[j]=DPHI_shale_corrected.iloc[j]
                else:
                    st.write("Select the Gas zone boundary properly; gas correction can't be applied")
                    TPHI = (data[selected_column_NPHI] + DPHI) / 2
                    DPHI=DPHI
                    DPHI_shale_corrected
    
                return DPHI,DPHI_shale_corrected,TPHI




        if all_op in ['Total porosity Calculation', 'Water Saturation', 'Reservoir flag & NTG']:
        
            with po.expander("Total Porosity"):
            
                st.subheader("DPHI Calculation")


                def d_phi():
                
                    cvv,vcc,cvc=st.columns(3)
                    abn = cvv.radio('Method:',['Using Values','DPHI Log'])
                    gas_correction_option = cvc.radio('Gas Correction:',['No','Yes'])

                    if abn =="DPHI Log":
                        selected_column_DPHI= vcc.selectbox('Choose DPHI Log' , df_fill.columns,index=well_df.columns.get_loc(default_column_DPHI) if default_column_DPHI in well_df.columns else 1)
                        DPHI = df_fill[selected_column_DPHI]   
                        DPHI_shale_corrected=effective_phi(Vsh, df_fill[selected_column_DPHI],95, condition_good)
                        if gas_correction_option == 'Yes':
                            gas_corrected_data=gas_correction(DPHI, DPHI_shale_corrected, g_df, df_fill, selected_column_NPHI)
                            df_fill['DPHI']=gas_corrected_data[0]
                            unitadder(df_unit,'DPHI','V/V') 
                            df_fill['DPHIE']=gas_corrected_data[1]
                            unitadder(df_unit,'DPHIE','V/V')       
                            # Assign values to the 'TPHI' column
                            df_fill.loc[:, 'TPHI'] = gas_corrected_data[2]
                            unitadder(df_unit,'TPHI','V/V')
                        else:
                            TPHI = (DPHI + df_fill[selected_column_NPHI]) / 2
                            df_fill['DPHI']=DPHI
                            unitadder(df_unit,'DPHI','V/V') 
                            df_fill['DPHIE']=DPHI_shale_corrected
                            unitadder(df_unit,'DPHIE','V/V')       
                            df_fill['TPHI']=TPHI
                            unitadder(df_unit,'TPHI','V/V')


                    if abn =="Using Values":
                        selected_column_RHOB=vcc.selectbox('RHOB log:', df_fill.columns, index=well_df.columns.get_loc(default_column_RHOB) if default_column_RHOB in well_df.columns else 1)
                        bbn = vcc.radio('Uniform Lithology (Matrix Density):',['Yes','No'])
                        if bbn =="Yes":
                            RHO_fl = cvc.text_input("Fluid Density Value:", value="1.04")
                            RHO_mat_str = cvc.text_input("Matrix density Value:", value="2.65")
                            RHO_mat = float(RHO_mat_str)
                            RHO_fl = float(RHO_fl)
                            df_fill[selected_column_RHOB] = df_fill[selected_column_RHOB].astype(float)
                            DPHI = (RHO_mat - df_fill[selected_column_RHOB]) / (RHO_mat - RHO_fl)
                            DPHI_shale_corrected=effective_phi(Vsh, DPHI,95, condition_good)
                            if gas_correction_option == 'Yes':
                                gas_corrected_data=gas_correction(DPHI, DPHI_shale_corrected, g_df, df_fill, selected_column_NPHI)
                                df_fill['DPHI']=gas_corrected_data[0]
                                unitadder(df_unit,'DPHI','V/V') 
                                df_fill['DPHIE']=gas_corrected_data[1]
                                unitadder(df_unit,'DPHIE','V/V')       
                                # Assign values to the 'TPHI' column
                                df_fill.loc[:, 'TPHI'] = gas_corrected_data[2]
                                unitadder(df_unit,'TPHI','V/V')
                            else:
                                TPHI = (DPHI + df_fill[selected_column_NPHI]) / 2
                                df_fill['DPHI']=DPHI
                                unitadder(df_unit,'DPHI','V/V') 
                                df_fill['DPHIE']=DPHI_shale_corrected
                                unitadder(df_unit,'DPHIE','V/V')       
                                df_fill['TPHI']=TPHI
                                unitadder(df_unit,'TPHI','V/V')      
                        if bbn =="No" and not l_df.empty:
                            num_of_form = len(l_df) + 1
                            depth_boundary_inner = np.array(l_df['Y'])
                            end1 = df_fill["DEPTH"].iloc[-1]
                            end2 = df_fill["DEPTH"].iloc[0]
                            depth_boundary =np.concatenate(([end1, end2], depth_boundary_inner))
                            depth_boundary = np.sort(depth_boundary)
                            RHOMA = []
                            for i in range(num_of_form):
                                rhoma_i = st.number_input(f'Enter density for formation {i + 1}:',value=2.65)
                                RHOMA.append(rhoma_i)
                            RHOMA_array = np.zeros(len(df_fill))
                            for i in range(num_of_form):
                                condition_boundary = (df_fill['DEPTH'] >= depth_boundary[i]) & (df_fill['DEPTH'] <= depth_boundary[i+1])
                                RHOMA_array[condition_boundary] = RHOMA[i]       
                            RHO_fl = st.number_input("Fluid Density Value:", value=1.04)
                            df_fill[selected_column_RHOB] = df_fill[selected_column_RHOB].astype(float)
                            DPHI = (RHOMA_array - (df_fill[selected_column_RHOB])) / (RHOMA_array - RHO_fl)
                            if st.checkbox('litholog based on density'):
                                color_scale = (RHOMA_array - 2.65) / (2.71 - 2.65)
                                color_scale = np.clip(color_scale, 0, 1)  # Ensure values are within [0, 1]
                                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(6, 7))
                                for i in range(len(df_fill)):
                                    ax1.hlines(df_fill['DEPTH'].iloc[i], 0, 1, color=plt.cm.jet(color_scale[i]), linewidth=2)
                                ax1.set_xlim(0, 1)
                                ax1.set_ylim(max(df_fill['DEPTH']), min(df_fill['DEPTH']))  # Reverse the y-axis
                                ax1.set_xlabel('Lithology Log')
                                ax1.set_ylabel('Depth (m)')
                                ax2.plot(RHOMA_array, df_fill['DEPTH'], color='blue', linewidth=2)
                                ax2.set_xlim(min(RHOMA_array), max(RHOMA_array))
                                ax2.set_ylim(max(df_fill['DEPTH']), min(df_fill['DEPTH']))  # Reverse the y-axis
                                ax2.set_xlabel('RHOMA_array')
                                ax2.set_ylabel('Depth (m)')
                                ax2.set_xlim(min(RHOMA_array)-0.2, max(RHOMA_array)+0.2)
                                st.pyplot(fig)
                            DPHI_shale_corrected=effective_phi(Vsh, DPHI,95, condition_good)
                            if gas_correction_option == 'Yes':
                                gas_corrected_data=gas_correction(DPHI, DPHI_shale_corrected, g_df, df_fill, selected_column_NPHI)
                                df_fill['DPHI']=gas_corrected_data[0]
                                unitadder(df_unit,'DPHI','V/V') 
                                df_fill['DPHIE']=gas_corrected_data[1]
                                unitadder(df_unit,'DPHIE','V/V')       
                                # Assign values to the 'TPHI' column
                                df_fill.loc[:, 'TPHI'] = gas_corrected_data[2]
                                unitadder(df_unit,'TPHI','V/V')
                            else:
                                TPHI = (DPHI + df_fill[selected_column_NPHI]) / 2
                                df_fill['DPHI']=DPHI
                                unitadder(df_unit,'DPHI','V/V') 
                                df_fill['DPHIE']=DPHI_shale_corrected
                                unitadder(df_unit,'DPHIE','V/V')       
                                df_fill['TPHI']=TPHI
                                unitadder(df_unit,'TPHI','V/V') 
                        elif bbn =="No" and l_df.empty:
                            st.warning('Note: Please ensure you have separated lithologies in the previous section;the entire formation is treated as a single lithology.')
                            RHO_fl = st.text_input("Fluid Density Value: ", value="1.04")
                            RHO_mat_str = st.text_input("Matrix density Value: ", value="2.65")
                            RHO_mat = float(RHO_mat_str)
                            RHOMA_array=RHO_mat
                            RHO_fl = float(RHO_fl)
                            df_fill[selected_column_RHOB] = df_fill[selected_column_RHOB].astype(float)
                            DPHI = (RHO_mat - df_fill[selected_column_RHOB]) / (RHO_mat - RHO_fl)
                            DPHI_shale_corrected=effective_phi(Vsh, DPHI,95, condition_good)
                            if gas_correction_option == 'Yes':
                                gas_corrected_data=gas_correction(DPHI, DPHI_shale_corrected, g_df, df_fill, selected_column_NPHI)
                                df_fill['DPHI']=gas_corrected_data[0]
                                unitadder(df_unit,'DPHI','V/V') 
                                df_fill['DPHIE']=gas_corrected_data[1]
                                unitadder(df_unit,'DPHIE','V/V')       
                                # Assign values to the 'TPHI' column
                                df_fill.loc[:, 'TPHI'] = gas_corrected_data[2]
                                unitadder(df_unit,'TPHI','V/V')
                            else:
                                TPHI = (DPHI + df_fill[selected_column_NPHI]) / 2
                                df_fill['DPHI']=DPHI
                                unitadder(df_unit,'DPHI','V/V') 
                                df_fill['DPHIE']=DPHI_shale_corrected
                                unitadder(df_unit,'DPHIE','V/V')       
                                df_fill['TPHI']=TPHI
                                unitadder(df_unit,'TPHI','V/V')        
                    ##########################################################################
                    #                  Total Porosity Plot                         #
                    ##########################################################################  
                    st.subheader("Total porosity Calculation")
                    # st.write(TPHI)
                    def total_phi_fig(df_fill):
                        fig = make_subplots(rows=1, cols=3, shared_yaxes=True, horizontal_spacing=0.03,subplot_titles=[curvename(df_unit,['TPHI'])[0],curvename(df_unit,[selected_column_NPHI])[0],curvename(df_unit,['DPHI'])[0]])

                        fig.add_trace(go.Scatter(x=df_fill['TPHI'], y=df_fill['DEPTH'], line=dict(width=1.5, color='green'), name='Total Porosity'), row=1, col=1)
                        fig.add_trace(go.Scatter(x=df_fill[selected_column_NPHI], y=df_fill['DEPTH'], line=dict(width=1.5, color='cyan'), name=selected_column_NPHI ), row=1, col=2)
                        fig.add_trace(go.Scatter(x=df_fill['DPHI'], y=df_fill['DEPTH'], line=dict(width=1.5, color='magenta'), name='DPHI'), row=1, col=3)

                        # Set axis titles and labels
                        fig.update_xaxes(title_text=curvename(df_unit,['TPHI'])[0], row=1, col=1)
                        fig.update_xaxes(title_text=curvename(df_unit,[selected_column_NPHI])[0], row=1, col=2)
                        fig.update_xaxes(title_text=curvename(df_unit,['DPHI'])[0], row=1, col=3)
                        fig.update_yaxes(title_text=curvename(df_unit,[deps])[0], autorange='reversed', gridwidth=0.8)

                        fig.update_layout(width=430, height=850)  # Adjust width and height as needed
                        fig.update_layout(
                                    title_text='<b>Total porosity</b>',
                                    title_font=dict(size=30, family='Arial', color='black'),
                                    width=600,
                                )
                        return fig
                    fig=total_phi_fig(df_fill)
                    st.plotly_chart(fig)
                    ###########################################################################
                    ##                  Effective Porosity Plot                         #
                    ###########################################################################
                    TPHI_shale_corrected=effective_phi(Vsh, df_fill['TPHI'],95, condition_good)
                    df_fill['PHIE']=TPHI_shale_corrected
                    unitadder(df_unit,'PHIE','V/V') 
                    if st.checkbox('Effective Porosity calculation'):
                        def effective_phi_fig(df_fill):                    
                            fig = make_subplots(rows=1, cols=3, shared_yaxes=True, horizontal_spacing=0.03,subplot_titles=[curvename(df_unit,['PHIE'])[0],curvename(df_unit,['NPHIE'])[0],curvename(df_unit,['DPHIE'])[0]])
                            fig.add_trace(go.Scatter(x=df_fill['PHIE'], y=df_fill['DEPTH'], line=dict(width=1.5, color='green'), name='Effective Porosity'), row=1, col=1)
                            fig.add_trace(go.Scatter(x=df_fill['NPHIE'], y=df_fill['DEPTH'], line=dict(width=1.5, color='cyan'), name=selected_column_NPHI +'Effective Porosity' ), row=1, col=2)
                            fig.add_trace(go.Scatter(x=df_fill['DPHIE'], y=df_fill['DEPTH'], line=dict(width=1.5, color='magenta'), name='DPHI'+'Effective Porosity'), row=1, col=3)
                            # Set axis titles and labels
                            fig.update_xaxes(title_text=curvename(df_unit,['PHIE'])[0], row=1, col=1)
                            fig.update_xaxes(title_text=curvename(df_unit,['NPHIE'])[0], row=1, col=2)
                            fig.update_xaxes(title_text=curvename(df_unit,['DPHIE'])[0], row=1, col=3)
                            fig.update_yaxes(title_text=curvename(df_unit,[deps])[0], autorange='reversed', gridwidth=0.8)
                            fig.update_layout(width=600, height=850)  # Adjust width and height as needed
                            fig.update_layout(
                                    title_text='<b>Effective porosity</b>',
                                    title_font=dict(size=30, family='Arial', color='black'),
                                    width=600,
                                )
                            return fig
                        fig=effective_phi_fig(df_fill)
                        st.plotly_chart(fig)

                    return df_fill, TPHI_shale_corrected,df_unit
                df_fill,TPHI_shale_corrected,df_unit = d_phi()

       # ##########################################################################
       # #                  Water Saturation calculation                          #
       # ##########################################################################  
        TPHI_selection = st.radio('Which Porosity To be used for further calculation:',['Calculated','Choose from the LAS file'])
        if TPHI_selection=='Calculated':
            pass
        elif TPHI_selection=='Choose from the LAS file':
            selected_column_TPHI=st.selectbox('Porosity', well_df.columns, index=well_df.columns.get_loc(default_column_DPHI) if default_column_DPHI in well_df.columns else 1)
            if selected_column_TPHI is not None:
                df_fill['TPHI']=df_fill[selected_column_TPHI]
                TPHI_shale_corrected=effective_phi(Vsh, df_fill['TPHI'],95, condition_good)
                df_fill['PHIE']=TPHI_shale_corrected        
                        
        
        if all_op in ['Water Saturation', 'Reservoir flag & NTG']:

            if df_fill['TPHI'] is not None:
                with st.expander("4. Water Saturation"):
                    # def toggle():
                    #     st.session_state.button = not st.session_state.button
                    # st.write('For improved visibility: collapses sidebar ')
                    # st.button("Click here ",key='sidebar_callapse_sw', on_click=toggle)



                    st.subheader("Water Saturation")


                    Rw= None

                    sim = st.radio('Calculate Using:',['Archie + Simandoux Method','Archie'])
                    st.title('')
                    st.write('Input Sw Parameters')
                    s0,s1,s2,s3,s4=st.columns(5)

                    bbn = s0.radio('Do you have Rw Value :',['Yes','No'])

                    a = s2.text_input('Input: a ',value='1',key='trw')
                    m = s3.text_input('Input: m ',value='2',key='trg')
                    n = s4.text_input('Input: n ',value='2',key='tri')
                    a= float(a)
                    m= float(m)
                    n= float(n)

                    if bbn =="Yes":

                        st.title('')
                        st.write('Choose Resistivity:')
                        uio,oiu=st.columns(2)

                        selected_column_RESD = uio.selectbox('Deep Resistivity:',df_fill.columns, index=well_df.columns.get_loc(default_column_RESD) if default_column_RESD in well_df.columns else 1)
                        selected_column_RESS = oiu.selectbox('Shallow Resistivity:',df_fill.columns,index=well_df.columns.get_loc(default_column_RESS) if default_column_RESS in well_df.columns else 1)
                        Rw =s1.text_input("Rw Value:", value="0.1")
                        Rw=float(Rw)

                    if bbn =="No":
                        ##########################################################################
                        #                          Rwa Method                                    #
                        ##########################################################################  
                        st.write('(Using Rwa Method)')

                        uio,oiu=st.columns(2)

                        selected_column_RESD = uio.selectbox('Deep Resistivity:',df_fill.columns, index=well_df.columns.get_loc(default_column_RESD) if default_column_RESD in well_df.columns else 1)
                        selected_column_RESS = oiu.selectbox('Shallow Resistivity:',df_fill.columns,index=well_df.columns.get_loc(default_column_RESS) if default_column_RESS in well_df.columns else 1)

                        gg=st.checkbox('Guide for Rw Picking')
                        if gg:
                            percentile_Vsh_Rw= st.number_input('percentile_Vsh_Rw',value=35, step=1)
                            tol_RD_RS_Rw=st.number_input('tol_RD_RS_Rw',value=1, step=1)
                            Condition_Rw = (Vsh <= np.percentile(Vsh, percentile_Vsh_Rw)) & condition_good & (abs(df_fill[selected_column_RESD] - df_fill[selected_column_RESS]) < tol_RD_RS_Rw)
                            Rwc = []
                            Dwc = []

                            for i in Vsh.index:
                                if Condition_Rw.loc[i]:
                                    Rwc.append(df_fill[selected_column_RESD].loc[i])
                                    Dwc.append(df_fill['DEPTH'].loc[i])
                            Rwc=np.array(Rwc)
                            Dwc=np.array(Dwc)
                        clicked_data = []

                        fig = sp.make_subplots(rows=1, cols=3, shared_yaxes=True, horizontal_spacing=0.03,subplot_titles=[curvename(df_unit,['TPHI'])[0],curvename(df_unit,[selected_column_GR])[0],'  '+curvename(df_unit,[selected_column_RESD])[0]+' and '+curvename(df_unit,[selected_column_RESS])[0]])

                        fig.add_trace(go.Scatter(x=df_fill['TPHI'], y=df_fill['DEPTH'], line=dict(width=0.5, color='blue'), name='Total Porosity'), row=1, col=1)
                        fig.update_xaxes(title='Total Porosity', row=1, col=1)
                        fig.update_yaxes(title='Depth (m)', autorange='reversed', row=1, col=1)

                        fig.add_trace(go.Scatter(x=df_fill[selected_column_GR], y=df_fill['DEPTH'], line=dict(width=0.5, color='green'), name='Gamma Ray(API)'), row=1, col=2)
                        fig.update_xaxes(title='Gamma Ray(API)', row=1, col=2)

                        fig.add_trace(go.Scatter(x=df_fill[selected_column_RESD], y=df_fill['DEPTH'], line=dict(width=0.5, color='blue'), name='Deep Resistivity'), row=1, col=3)

                        fig.add_trace(go.Scatter(x=df_fill[selected_column_RESS], y=df_fill['DEPTH'], line=dict(width=0.5, color='red'), name='Shallow Resistivity', showlegend=False), row=1, col=3)
                        fig.update_xaxes(title='Deep and Shallow Resistivity', type='log', range=[0, 2], row=1, col=3)

                        fig.update_layout(height=1000, width=450, title_text='Logs to determine the Rw', showlegend=False)
                        fig.update_layout(
                                title_text='<b>Rwa Method</b>',
                                title_font=dict(size=35, family='Arial', color='black'),
                                width=750,
                            )


                        if gg:
                            fig.add_trace(go.Scatter(x=Rwc, y=Dwc, mode='markers', name='Rw_condition', marker=dict(size=7, color='green')), row=1, col=3)

                        bqq = st.radio("Select Input Type", ["Picking from plot ","Mannual Input "])

                        r_df = pd.DataFrame({"X": []})

                        if bqq == "Mannual Input ":
                            st.plotly_chart(fig)

                            qwe,ewq=st.columns(2)
                            num_values = st.number_input("How many depth values for Rwa do you want to input?", min_value=1, step=1)
                            Rw = []
                            if num_values is not None and df_fill['TPHI'] is not None and m is not None and a is not None:
                                for i in range(num_values):
                                    Rwa_condition_depth = st.number_input(f"Enter depth value for the Rw condition {i + 1}:", step=0.01)
                                    nearest_index = (df_fill['DEPTH'] - Rwa_condition_depth).abs().idxmin()
                                    nearest_depth = float(df_fill['DEPTH'].loc[nearest_index])
                                    RW=(float(df_fill[selected_column_RESD].loc[df_fill['DEPTH'] == nearest_depth]))*df_fill['TPHI'][df_fill['DEPTH']==nearest_depth]**m/a
                                    Rw.append(RW)
                                st.write(np.mean(Rw))
                                Rwa_method_approvel = st.radio("Satisfied Rw ?",['Yes','No'])
                                if Rwa_method_approvel== 'Yes':
                                    Rw=np.mean(Rw)
                                    st.write("Rw Value:", Rw)
                                elif Rwa_method_approvel== 'No':
                                     Rw=float(input("Enter the Value of the Rw manually : "))    
                                     st.write("Rw Value:", Rw)


                        if bqq == "Picking from plot ":
                            component_value = plotly_events(fig)
                            if component_value:
                                st.subheader("Clicked Points:")
                                for point in component_value:
                                    st.write(f"X: {point['x']:.2f}, Y: {point['y']:.2f}")
                                    # Append the clicked data to the list
                                    clicked_data.append({"X": point['x'], "Y": point['y']})
                            r_df = pd.DataFrame(clicked_data)
                        if st.checkbox(" Finish"):
                            if r_df is not None and not r_df.empty and df_fill['TPHI'] is not None and m is not None and a is not None:
                                Rw=np.zeros(len(r_df['X']))
                                for i in range(len(r_df['Y'])):
                                    RW=r_df['X'][i]*df_fill['TPHI'][df_fill['DEPTH']==r_df['Y'][i]]**m/a
                                    Rw[i]=RW
                                st.write(Rw.mean())
                                Rwa_method_approvel = st.radio("Satisfied Rw ?",['Yes','No'])
                                if Rwa_method_approvel== 'Yes':
                                    Rw=Rw.mean()
                                    st.write("Rw Value:", Rw)
                                elif Rwa_method_approvel== 'No':
                                     Rw=float(input("Enter the Value of the Rw manually : "))    
                                     st.write("Rw Value:", Rw)



                    ##########################################################################
                    #                          Archie's Method                               #
                    ########################################################################## 
                    re_sw1,re_sw2,re_sw3=st.columns([1.5,0.75,0.75])            
                    if Rw is not None and df_fill['TPHI'] is not None:                
                        Sw_ar = [(a * Rw / (phi ** m * resd)) ** (1 / n) if phi != 0 and resd != 0 else 0 for phi, resd in zip(df_fill['TPHI'], df_fill[selected_column_RESD])]
                        Sw_ar = np.array(Sw_ar)
                        Sw_ar[Sw_ar>=1]=1
                        Sw_ar[Sw_ar<=0]=0

                        # st.write('Also Calculate Using:')
                        if sim =='Archie + Simandoux Method':
                            ##########################################################################
                            #                          Rsh calculation                               #
                            ##########################################################################    
                            # '''Rshc calculation'''
                            x=np.percentile(Vsh, 95)
                            Rshc=[]
                            Dshc=[]
                            for i in Vsh.index:  
                                if Vsh.loc[i] >= x and condition_good.loc[i]:
                                    Rshc.append(df_fill[selected_column_RESD].loc[i])
                                    Dshc.append(df_fill['DEPTH'].loc[i])

                            Rshc=np.array(Rshc)   
                            Rshc_mean=Rshc.mean()      
                            # st.write(Rshc_mean)

                            fig = make_subplots(rows=1, cols=4, shared_yaxes=True, horizontal_spacing=0.03,subplot_titles=[curvename(df_unit,[selected_column_CALI])[0],curvename(df_unit,[selected_column_GR])[0],curvename(df_unit,['Vsh'])[0],curvename(df_unit,[selected_column_RESD])[0]])


                            fig.add_trace(go.Scatter(x=df_fill[selected_column_CALI], y=df_fill['DEPTH'], line=dict(width=1, color='blue'),showlegend=False), row=1, col=1)

                            for depth, is_condition_met in zip(df_fill.DEPTH,condition_bad):
                                    if is_condition_met:
                                        fig.add_trace(go.Scatter(
                                            x=[df_fill[selected_column_CALI].min(), df_fill[selected_column_CALI].max()],  
                                            y=[depth, depth],  
                                            mode='lines',
                                            line=dict(width=0.3, color='red', dash='solid'),  
                                            name=f'Condition - Depth: {depth}',  
                                            showlegend=False  
                                        ), row=1, col=1)

                            fig.add_trace(go.Scatter(x=df_fill[selected_column_GR], y=df_fill['DEPTH'], line=dict(width=1, color='green'),name=selected_column_GR), row=1, col=2)
                            fig.add_trace(go.Scatter(x=Vsh, y=df_fill.DEPTH, mode='lines', name='Vsh', line=dict(color='red')), row=1, col=3)

                            fig.add_trace(go.Scatter(x=df_fill[selected_column_RESD], y=df_fill['DEPTH'], mode='lines', name=selected_column_RESD, line=dict(color='black')), row=1, col=4)
                            fig.add_trace(go.Scatter(x=Rshc, y=Dshc, mode='markers', name='Rsh', marker=dict(size=8, color='red')), row=1, col=4)
                            fig.update_xaxes(type="log", row=1, col=4)

                            fig.update_yaxes(title_text='Depth (m)', autorange='reversed', gridwidth=0.8)
                            fig.update_layout(title='Rsh Calculation :',width=530, height=900)  # Adjust width and height as needed
                            fig.update_layout(
                                title_text='<b>Rsh Calculation</b>',
                                title_font=dict(size=35, family='Arial', color='black'),
                            )

                            re_sw1.plotly_chart(fig)

                            # Rsh_value_approvel = input("Are you satisfied with value of Rsh calulated (y/n)? ").lower()
                            st.write('Rsh value:')
                            st.write(Rshc_mean)

                            Rsh_value_approvel=st.radio('Rsh value approvel',['Yes','No'])
                            if Rsh_value_approvel=='Yes':
                                Rsh=Rshc_mean
                            if Rsh_value_approvel=='No':
                                Rsh=st.text_input('Enter the Value of the Rsh manually :', value='5.0')
                                Rsh=float(Rsh)

                            ##########################################################################
                            #                          Simandoux Method                              #
                            ##########################################################################  

                            if Rw is not None and df_fill['TPHI'] is not None and Vsh is not None and Rsh is not None and df_fill[selected_column_RESD] is not None:
                                # Sw_sd = (0.1/(2*TPHI**2))*(np.sqrt((Vsh/Rsh)**2 + ((4*TPHI**2) / (0.1*data[selected_column_RESD])))-(Vsh/Rsh))
                                Sw_sd = ((a * Rw) / (2 * df_fill['TPHI'] **m)) * (np.sqrt((Vsh / Rsh)**2 + ((4 *df_fill['TPHI'] ** m) / (a * Rw * df_fill[selected_column_RESD]))) - (Vsh/ Rsh))
                                Sw_sd = np.array(Sw_sd)
                                Sw_sd[Sw_sd>=1]=1
                                Sw_sd[Sw_sd<=0]=0
                                col1w, col2w,col3w = st.columns(3)
                                with re_sw2:
                                    st.write('')
                                    fig, ax1 = plt.subplots(figsize=(6, 18.5))
                                    ax1.plot(Sw_sd, df_fill['DEPTH'], color='teal', lw=1)
                                    ax1.invert_yaxis()
                                    ax1.tick_params(axis='x', colors='teal')
                                    ax1.spines['top'].set_edgecolor('teal')
                                    ax1.xaxis.set_ticks_position('top')
                                    ax1.set_xlabel('Sw_Simandoux', color='teal', fontsize=18)
                                    ax1.xaxis.set_label_position('top')
                                    ax1.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
                                    st.title('')
                                    st.title('')
                                    st.pyplot(fig)
                                    df_fill['Sw_sd']=Sw_sd

                                # Plot for Sw_ar
                                with re_sw3:
                                    st.write('')
                                    fig, ax2 = plt.subplots(figsize=(6, 18.5))
                                    ax2.plot(Sw_ar, df_fill['DEPTH'], color='b', lw=1)
                                    ax2.invert_yaxis()
                                    ax2.tick_params(axis='x', colors='b')
                                    ax2.spines['top'].set_edgecolor('b')
                                    ax2.xaxis.set_ticks_position('top')
                                    ax2.set_xlabel('Sw_Archie', color='b', fontsize=18)
                                    ax2.xaxis.set_label_position('top')
                                    ax2.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
                                    ax2.set_xlim(0, 1)
                                    st.title('')
                                    st.title('')
                                    st.pyplot(fig)
                                    df_fill['Sw_ar']=Sw_ar
                                    # Final df
                                    # st.write(data.describe())
                    else:
                        Sw_ar=0*df_fill['DEPTH']
                        Sw_sd=0*df_fill['DEPTH']

                    if sim=='Archie':
                        col1w, col2w = st.columns(2)
                        with re_sw2:
                            st.write('')
                            fig, ax2 = plt.subplots(figsize=(6, 18.5))
                            ax2.plot(Sw_ar, df_fill['DEPTH'], color='b', lw=1)
                            ax2.invert_yaxis()
                            ax2.tick_params(axis='x', colors='b')
                            ax2.spines['top'].set_edgecolor('b')
                            ax2.xaxis.set_ticks_position('top')
                            ax2.set_xlabel('Sw_Archie', color='b', fontsize=18)
                            ax2.xaxis.set_label_position('top')
                            ax2.grid(which='both', color='black', axis='both', alpha=1, linestyle='--', linewidth=0.8)
                            ax2.set_xlim(0, 1)
                            st.title('')
                            st.title('')
                            st.pyplot(fig)
                            df_fill['Sw_ar']=Sw_ar
                    # return df_fill, Sw_ar,Sw_sd, sim
                    # df_fill, Sw_ar,Sw_sd, sim = sw_cal()    
            else:
                st.warning('TPHI is not decided for the calculation')
        if all_op == 'Reservoir flag & NTG':
            with st.expander("Reservoir flag & NTG"):
                st.subheader('Reservoir flag & NTG')
                st.title('')


                if df_fill['TPHI'] is not None and Vsh is not None and Sw_ar is not None:


                    def r_n_zones():
                        zpos1,zpos2=st.columns(2)
                        zpos1.write('Conditions for NTG:')
                        zpos2.write('Conditions for Reservoir Flag:')

                        cln1,cln2,cln3,cln5,cln6,cln7= st.columns(6)

                        # Sw = nlc.radio("Sw",['Sw_ar','Sw_sd'])
                        if sim =='Archie + Simandoux Method':
                            Sww = cln1.radio("Sw",['Archie','Simadaux'])
                            if Sww=='Archie':
                                Sw=Sw_ar
                            if Sww=='Simadaux':
                                Sw=Sw_sd
                        else:
                            Sw=Sw_ar
                        nswsd = cln1.number_input('',value=0.5)
                        nvsh = cln2.number_input('Vsh ', value=0.5)   
                        ntphi = cln2.number_input(' TPHI', value=0.05)

                        rswsd = cln5.number_input('Sw',value=0.6)
                        rvsh = cln6.number_input('Vsh', value=0.6)    
                        rtphi = cln6.number_input('TPHI', value=0.02)    



                        fig = plt.figure(figsize=(15, 12))
                        ax1 = plt.subplot2grid((1, 6), (0, 0), rowspan=1, colspan=1)
                        ax2 = plt.subplot2grid((1, 6), (0, 1), rowspan=1, colspan=1)
                        ax3 = plt.subplot2grid((1, 6), (0, 2), rowspan=1, colspan=1)
                        ax4 = plt.subplot2grid((1, 6), (0, 3), rowspan=1, colspan=1)
                        ax5 = plt.subplot2grid((1, 6), (0, 5), rowspan=1, colspan=1)
                        ax6 = plt.subplot2grid((1, 6), (0, 4), rowspan=1, colspan=1)

                            # ax6 = plt.subplot2grid((1, 5), (0, 5), rowspan=1, colspan=1)


                        ax1.plot(df_fill[selected_column_CALI], df_fill.DEPTH, lw=0.9, color='blue')
                        ax1.fill_betweenx(df_fill.DEPTH, df_fill[selected_column_BS], df_fill[selected_column_CALI], facecolor='yellow')
                        ax1.set_xlabel(curvename(df_unit,[selected_column_CALI])[0],color='b', fontsize=14)
                        ax1.set_ylabel(curvename(df_unit,[deps])[0])
                        # ax1.set_ylim(max_value, min_value) # Reversed the y-axis limits
                        ax1.set_xlim(5,15)
                        ax1.tick_params(axis='x', colors='b')
                        ax1.spines['top'].set_edgecolor('b')
                        ax1.xaxis.set_label_position('top')
                        ax1.grid(which='both',color='black', axis='both', alpha=1, linestyle='--',linewidth=0.8)

                        ax11=ax1.twiny()
                        ax11.plot(df_fill[selected_column_BS], df_fill.DEPTH, lw=0.9, color='red', linestyle='dashed')
                        ax11.set_xlim(5,15)
                        ax11.tick_params(axis='x', colors='r')
                        ax11.spines['top'].set_edgecolor('r')
                        ax11.spines['top'].set_position(("axes", 1.055))
                        ax11.set_xlabel('Bit size',color='r',fontsize=14)
                        ax11.xaxis.set_label_position('top')
                        ax1.xaxis.set_ticks_position('top')




                        ax2.plot(df_fill['Vsh'], df_fill.DEPTH, lw=0.9, color='green')
                        ax2.set_ylabel(curvename(df_unit,[deps])[0])
                        # ax2.set_ylim(max_value,min_value)  # Reversed the y-axis limits
                        ax2.tick_params(axis='x', colors='g')
                        ax2.spines['top'].set_edgecolor('g')
                        ax2.spines['top'].set_position(("axes", 1.0))
                        ax2.xaxis.set_ticks_position('top')
                        ax2.set_xlabel(curvename(df_unit,['Vsh'])[0],color='g', fontsize=14)
                        ax2.xaxis.set_label_position('top')
                        ax2.grid(which='both',color='black', axis='both', alpha=1, linestyle='--',linewidth=0.8)




                        ax3.plot(df_fill['PHIE'], df_fill['DEPTH'], lw=0.9, color='magenta')
                        ax3.set_ylabel(curvename(df_unit,[deps])[0])
                        ax3.set_xlim(0, 0.4)
                        # ax3.set_ylim(max_value,min_value)  # Reversed the y-axis limits
                        ax3.grid(which='both',color='black', axis='both', alpha=1, linestyle='--',linewidth=0.8)
                        ax3.tick_params(axis='x', colors='magenta')
                        ax3.spines['top'].set_edgecolor('magenta')
                        ax3.spines['top'].set_position(("axes", 1.0))
                        ax3.xaxis.set_ticks_position('top')
                        ax3.set_xlabel(curvename(df_unit,['PHIE'])[0],color='magenta', fontsize=14)
                        ax3.xaxis.set_label_position('top')
                        ax3.grid(which='both',color='black', axis='both', alpha=1, linestyle='--',linewidth=0.8)

                        ax31=ax3.twiny()

                        ax31.plot(df_fill['TPHI'], df_fill.DEPTH, color='g', lw=1)
                        ax31.set_ylabel('Depth (m)')
                        ax31.set_xlim(0, 0.4)
                        # ax31.set_ylim(max_value,min_value)  # Reversed the y-axis limits
                        ax31.grid(which='both',color='black', axis='both', alpha=1, linestyle='--',linewidth=0.8)
                        ax31.tick_params(axis='x', colors='indigo')
                        ax31.spines['top'].set_edgecolor('indigo')
                        ax31.spines['top'].set_position(("axes", 1.055))
                        ax31.xaxis.set_ticks_position('top')
                        ax31.set_xlabel(curvename(df_unit,['TPHI'])[0],color='indigo', fontsize=14)
                        ax31.xaxis.set_label_position('top')
                        ax31.grid(which='both',color='black', axis='both', alpha=1, linestyle='--',linewidth=0.8)
                        ax31.xaxis.set_ticks_position('top')
                        ax3.xaxis.tick_top()
                        ax3.set_xlim(0,0.7)
                        ax31.set_xlim(0,0.7)


                        ax4.plot(Sw_ar, df_fill.DEPTH, lw=0.9, color='deeppink')
                        ax4.set_ylabel(curvename(df_unit,[deps])[0])
                        # ax4.set_ylim(max_value,min_value)  # Reversed the y-axis limits
                        ax4.grid(which='both',color='black', axis='both', alpha=1, linestyle='--',linewidth=0.8)
                        ax4.tick_params(axis='x', colors='deeppink')
                        ax4.spines['top'].set_edgecolor('deeppink')
                        ax4.spines['top'].set_position(("axes", 1.0))
                        ax4.xaxis.set_ticks_position('top')
                        ax4.set_xlabel('Sw_ar',color='deeppink', fontsize=14)
                        ax4.xaxis.set_label_position('top')
                        ax4.grid(which='both',color='black', axis='both', alpha=1, linestyle='--',linewidth=0.8)
                        ax4.set_xlim(1,0)
                        ax4.xaxis.tick_top()

                        if sim =='Archie + Simandoux Method':
                            ax41=ax4.twiny()
                            ax41.plot(Sw_sd, df_fill.DEPTH, lw=0.9, color='b')
                            #ax41.fill_betweenx(df_fill.DEPTH,Sw_sd,Sw_ar, facecolor='yellow')
                            ax41.set_ylabel(curvename(df_unit,[deps])[0])
                            # ax41.set_ylim(max_value,min_value)  # Reversed the y-axis limits
                            ax41.grid(which='both',color='black', axis='both', alpha=1, linestyle='--',linewidth=0.8)
                            ax41.tick_params(axis='x', colors='b')
                            ax41.spines['top'].set_edgecolor('b')
                            ax41.spines['top'].set_position(("axes", 1.055))
                            ax41.xaxis.set_ticks_position('top')
                            ax41.set_xlabel('Sw_sd',color='b', fontsize=14)
                            ax41.xaxis.set_label_position('top')
                            ax41.grid(which='both',color='black', axis='both', alpha=1, linestyle='--',linewidth=0.8)
                            ax41.set_xlim(1,0)
                            ax4.xaxis.tick_top()
    


                        condition_ntg = (df_fill['Vsh'] <= nvsh) & (np.array(Sw) <=nswsd) & (df_fill['TPHI'] >= ntphi)
                        npayz=[]
                        for depth, is_condition_met in zip(df_fill['DEPTH'], condition_ntg):
                            if is_condition_met:
                                ax5.axhline(y=depth, color='teal', alpha=0.09)
                                npayz.append(1)
                            else:
                                npayz.append(0)
                        df_fill['Net Pay Zone']=npayz
                        ax5.set_xlabel('NTG_FLAG',color='teal', fontsize=14)

                        ax5.xaxis.set_label_position('top')
                        # ax6.set_ylim(max_value,min_value)

                        #reversing the axes
                        # ax4.fill_betweenx(df_fill.DEPTH,Sw_ar,Sw_sd,facecolor='red',hatch='xxx',alpha=0.8,where=condition_ntg)
                        max_value_depth=max(df_fill['DEPTH'].iloc[0],df_fill['DEPTH'].iloc[-1])
                        min_value_depth=min(df_fill['DEPTH'].iloc[0],df_fill['DEPTH'].iloc[-1])
                        ax1.set_ylim(max_value_depth,min_value_depth)
                        ax2.set_ylim(max_value_depth,min_value_depth)
                        ax3.set_ylim(max_value_depth,min_value_depth)
                        ax4.set_ylim(max_value_depth,min_value_depth)
                        ax5.set_ylim(max_value_depth,min_value_depth)
                        # ax5.xaxis.tick_top()
                        ax5.tick_params(axis='x', which='both', bottom=False)
                        ax5.set_xticks([])
                        #ax5.axis('off')


                        condition_res = (df_fill['Vsh'] <= rvsh) & (np.array(Sw) <=rswsd) & (df_fill['TPHI'] >= rtphi)
                        resz=[]
                        for depth, is_condition_met in zip(df_fill['DEPTH'], condition_res):
                            if is_condition_met:
                                ax6.axhline(y=depth, color='sandybrown', alpha=0.09)
                                resz.append(1)
                            else:
                                resz.append(0)
                        ax6.set_xlabel('RES_FLAG',color='sandybrown', fontsize=14)
                        df_fill['Reservoir']=resz
                        ax6.xaxis.set_label_position('top')     
                        ax6.tick_params(axis='x', which='both', bottom=False)
                        ax6.set_ylim(max_value_depth,min_value_depth)
                        ax6.set_xticks([])



                        plt.tight_layout()
                        nt1,nt2 = st.columns([1.5,0.5])
                        nt1.pyplot(fig)
                        if nt1.checkbox('NTG calculation :'):
                            num_gross_reserv = nt1.number_input('Enter the number of gross reservoir to be applied for :', min_value=0, step=1)
                            nt1.write(f'Depth ranges values to enter for gross reservoir: {num_gross_reserv}')
                            if num_gross_reserv:
                                end1 = df_fill["DEPTH"].iloc[-1]
                                end2 = df_fill["DEPTH"].iloc[0]
                                Depth_step=abs(df_fill['DEPTH'][1]-df_fill['DEPTH'][2])
                                depth_values=[]
                                for i in range(num_gross_reserv):
                                    start_depth =nt1.number_input(f"Enter the top depth  for the reservoir {i + 1}:",min_value=0.0 if i == 0 else depth_values[-1], step=0.1)
                                    end_depth = nt1.number_input(f"Enter the bottom depth  for the reservoir {i + 1}:",min_value=start_depth+Depth_step, step=0.1)
                                    if start_depth >= min(end1, end2) and end_depth <= max(end1, end2):
                                        depth_values.append(start_depth)
                                        depth_values.append(end_depth)
                                        Gross=end_depth-start_depth
                                        Net_pay_zone = df_fill['Net Pay Zone'][(df_fill['DEPTH'] >= start_depth) & (df_fill['DEPTH'] <= end_depth)]
                                        Net_zone_width = sum(Net_pay_zone * Depth_step)
                                        ntg=Net_zone_width/Gross
                                        st.write(f"For the reservoir {i + 1}, Net to gross ratio is: {ntg}")
                                    else:
                                        st.write(f"For the reservoir {i + 1} depth ranges are invalid")       

                        return df_fill
                    df_fill = r_n_zones()



        st.write('-------------------------------------------------------------------------------------------------------------------------------------')

        st.subheader('Core Data Plot')
        with st.expander("View"):
            if uploaded_file2 is not None and (uploaded_file2.name.lower().endswith('.xlsx') or uploaded_file2.name.lower().endswith('.csv')) or dftcc:
                st.title('')


                if 'TPHI' in df_fill.columns:
                    def core_dat(c_df):
                        rty, yty, tyr= st.columns(3)  # Changed from 2 to 3 columns
                        x = rty.selectbox('Select Depth', c_df.columns,index=c_df.columns.get_loc('Top depth (m)') if 'Top depth (m)' in c_df.columns else 1)
                        y = yty.selectbox('Select Porosity', c_df.columns,index=c_df.columns.get_loc('Porosity (%)') if 'Porosity (%)' in c_df.columns else 1)
                        z = tyr.selectbox('Permeability', c_df.columns,index=c_df.columns.get_loc('Permeability (mD)') if 'Permeability (mD)' in c_df.columns else 1)
                        crrp = st.radio("Core porosity type", ['(V/V) (%)', '(V/V)'])
                        if st.checkbox("Compare porosities: core vs log"):
                            c_df = pd.DataFrame({
                                'Top depth (m)': c_df[x],
                                'Porosity (%)': c_df[y],
                                'Permeability (mD)': c_df[z]
                            })

                            fig, axes = plt.subplots(figsize=(6, 9), ncols=2)
                            ax4, ax5 = axes  # Assigning axes to individual plots
                            if crrp == '(V/V)':
                                ax41 = ax4.twiny()
                                ax51 = ax5.twiny()
                                ax4.plot(df_fill['TPHI'], df_fill['DEPTH'], color='limegreen', lw=1, label='TPHI')
                                ax41.scatter(c_df[y], c_df[x], color='b', lw=1, s=10, label='CORPOR')
                                ax5.plot(df_fill['PHIE'], df_fill['DEPTH'], color='limegreen', lw=1, label='PHIE')
                                ax51.scatter(c_df[y], c_df[x], color='b', lw=1, s=10, label='CORPOR')
                            elif crrp == '(V/V) (%)':
                                ax41 = ax4.twiny()
                                ax51 = ax5.twiny()
                                ax4.plot(df_fill['TPHI'], df_fill['DEPTH'], color='limegreen', lw=1, label='TPHI')
                                ax41.scatter(c_df[y] * 0.01, c_df[x], color='b', lw=1, s=10, label='CORPOR')
                                ax5.plot(df_fill['PHIE'], df_fill['DEPTH'], color='limegreen', lw=1, label='PHIE')
                                ax51.scatter(c_df[y] * 0.01, c_df[x], color='b', lw=1, s=10, label='CORPOR')
                            # Customize other properties as needed
                            # Iterate over all axes for customization
                            for ax in axes:
                                ax.tick_params(axis='x', which='both', bottom=False)
                                ax.invert_yaxis()
                                ax.tick_params(axis='x', colors='limegreen', top=True, labeltop=True)
                                ax.spines['top'].set_edgecolor('limegreen')
                                ax.spines['top'].set_position(("axes", 1.0))
                                ax.xaxis.set_label_position('top')
                                ax.grid(which='both', color='black', axis='both', alpha=0.5, linestyle='--', linewidth=0.8)
                                ax.set_xlim(0, 1)
                                ax.xaxis.tick_top()
                            # Set labels for each subplot
                            axes[0].set_xlabel('TPHI', color='limegreen', fontsize=12)
                            axes[1].set_xlabel('PHIE', color='limegreen', fontsize=12)
                            # Customize the twin axes
                            for ax, color in zip([ax41, ax51], ['b', 'b']):
                                ax.tick_params(axis='x', colors=color, labeltop=True)
                                ax.spines['top'].set_edgecolor(color)
                                ax.spines['top'].set_position(("axes", 1.06))
                                ax.set_xlabel('CORPOR', color=color, fontsize=12)
                                ax.xaxis.set_label_position('top')
                                ax.grid(which='both', color='black', axis='both', alpha=0.5, linestyle='--', linewidth=0.8)
                                ax.set_xlim(0, 1)
                                ax.tick_params(axis='x', which='both', bottom=False)
                                ax.xaxis.tick_top()
                            plt.suptitle("Comparison of Core Porosity with Calculated Log Porosity", fontsize=12, y=1.01)
                            plt.tight_layout()
                            # Display the plot using Streamlit
                            newc, nwc = st.columns([1.3, 0.7])
                            newc.pyplot(fig)
                        if st.checkbox("Compute empirical formula via linear regression"):
                            c_df = pd.DataFrame({
                                'Top depth (m)': c_df[x],
                                'Porosity (%)': c_df[y],
                                'Permeability (mD)': c_df[z]
                            })
                            c_df = c_df.dropna()
                            top_depth_data_cl = c_df['Top depth (m)']
                            porosity_cl = c_df['Porosity (%)']
                            permeability_cl = c_df['Permeability (mD)']
                            if type(top_depth_data_cl) is not str and type(porosity_cl) is not str and type(permeability_cl) is not str:
                                mnd, mxd = st.columns(2)
                                mim = mnd.number_input('Min depth', value=c_df['Top depth (m)'].min())
                                mxa = mxd.number_input('Max depth', value=c_df['Top depth (m)'].max())
                                depth_range_filter = (top_depth_data_cl >= mim) & (top_depth_data_cl <= mxa)
                                depth_cl = top_depth_data_cl[depth_range_filter]
                                porosity_vulcan_cl = porosity_cl[depth_range_filter]
                                permeability_vulcan_cl = permeability_cl[depth_range_filter]
                                min_positive_value = 1e-4
                                y = np.log10(np.maximum(permeability_vulcan_cl, min_positive_value)).values.reshape(-1, 1)
                                x = porosity_vulcan_cl.values.reshape(-1, 1)
                                model = LinearRegression()
                                model.fit(x, y)
                                r21 = model.score(x, y)
                                st.write('R2 score: ' + str(r21))
                                regression_eq = f'10^({model.coef_[0][0]:.4f} * CPOR + ({model.intercept_[0]:.4f}))'
                                st.write('Regression Equation: ' + regression_eq)
                                # st.title('Porosity - Permeability Relation')
                                fig, ax = plt.subplots()
                                p = ax.scatter(x=porosity_cl, y=permeability_cl, c=top_depth_data_cl, cmap='viridis', s=50)
                                ax.plot(porosity_vulcan_cl, 10 ** model.predict(x), color='black')  # Fixed the plotting of the regression line
                                ax.semilogy()
                                ax.set_ylabel('Core Permeability (mD)', fontsize=12, fontweight='bold')
                                ax.set_xlabel('Core Porosity (%)', fontsize=12, fontweight='bold')
                                ax.set_title(f'Core Permeability = {regression_eq}', fontsize=13, color='green')
                                fig.suptitle('Porosity - Permeability Relation', fontsize=14, color='navy', y=1.02)
                                colorbar = fig.colorbar(p)
                                colorbar.ax.invert_yaxis()
                                colorbar.set_label('Depth (m)', fontsize=12)
                                nj,jn,nn=st.columns([1.25,1.25,0.5])            
                                nj.pyplot(fig)

                                slope = model.coef_[0][0]
                                intercept = model.intercept_[0]


                                def plot_permeability_vs_depth(df_fill, permeability_data, top_depth_data, permeability_label, color1, color2):
                                    fig, ax = plt.subplots(figsize=(2, 6))  

                                    ax.plot(df_fill['Perm_SRL'], df_fill['DEPTH'], color=color1, lw=1)
                                    ax.invert_yaxis()

                                    ax.tick_params(axis='x', colors=color1, labelsize=6, top=True, bottom=False)  # Set top parameter to True and bottom to False
                                    ax.tick_params(axis='y', labelsize=6)  
                                    ax.set_xlabel('Estimated Permeability', color=color1, fontsize=6)
                                    ax.set_ylabel(curvename(df_unit,[deps])[0], color=color1, fontsize=6)

                                    ax.xaxis.set_label_position('top')
                                    ax.grid(which='both', color='black', axis='both', alpha=0.5, linestyle='--', linewidth=0.8)
                                    ax.set_xlim(10**-10, 10**10)
                                    ax.spines['top'].set_edgecolor(color1)
                                    ax.spines['top'].set_position(("axes", 1.0))

                                    xlabel_padding = 2            # Padding in points


                                    ax.set_xlabel("Estimated Permeability", color=color1, fontsize=6, labelpad=xlabel_padding)

                                    ax1 = ax.twiny()
                                    ax1.scatter(permeability_data, top_depth_data, color=color2, lw=1, s=6)

                                    ax1.tick_params(axis='x', colors=color2, labeltop=True, labelsize=6, top=True, bottom=False)  # Set top parameter to True and bottom to False
                                    ax1.set_xlabel(permeability_label, color=color2, fontsize=6)
                                    ax1.xaxis.set_label_position('top')
                                    ax1.grid(which='both', color='black', axis='both', alpha=0.5, linestyle='--', linewidth=0.8)
                                    ax.semilogx()
                                    ax1.semilogx()
                                    ax1.set_xlim(10**-10, 10**10)
                                    ax1.spines['top'].set_edgecolor(color2)
                                    ax1.spines['top'].set_position(("axes", 1.08))
                                    ax1.xaxis.set_tick_params(labeltop=True)
                                    ax1.xaxis.tick_top()
                                    ax.xaxis.tick_top()
                                    return fig

                                # crr = st.radio("Core porosity type ",['(V/V) (%)','(V/V)'])
                                if crrp=='(V/V) (%)':
                                    Perm_SLR = 10**(slope * (df_fill['PHIE'] * 100) + intercept)
                                    df_fill['Perm_SRL'] = Perm_SLR #
                                    jn.pyplot(plot_permeability_vs_depth(df_fill, permeability_vulcan_cl, top_depth_data_cl, 'CORPERM', 'limegreen', 'b'))
                                if crrp=='(V/V)':
                                    Perm_SLR = 10**(slope * (df_fill['PHIE']) + intercept)
                                    df_fill['Perm_SRL'] = Perm_SLR #
                                    jn.pyplot(plot_permeability_vs_depth(df_fill, permeability_vulcan_cl, top_depth_data_cl, 'CORPERM', 'limegreen', 'b'))


                    core_dat(c_df)
                else:
                    st.warning('Calculate TPHI or choose from log')
            else:
                st.warning('Upload core data in Data Loading tab')



        st.subheader('Final Dataset')
        with st.expander("View / Download"):

            
            def dwnld():
                st.write(df_fill.describe())
                csv_button = st.download_button(
                    label="Download as CSV",
                    key="download_csv",
                    data=df_fill.to_csv(index=False).encode('utf-8'),
                    file_name='well_logs.csv',
                    mime='text/csv'
                )

                xlsx_buffer = BytesIO()
                df_fill.to_excel(xlsx_buffer, index=False)
                xlsx_button = st.download_button(
                    label="Download as XLSX",
                    key="download_xlsx",
                    data=xlsx_buffer.getvalue(),
                    file_name='well_logs.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                )

            dwnld()
