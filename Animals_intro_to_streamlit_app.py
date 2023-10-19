import streamlit as st

# Create a selectbox to choose the active tab
selected_tab = st.selectbox("Select a tab:", ['Data Loading', 'Formation Evaluation', 'Visualization'])

if selected_tab == 'Data Loading':
    st.title("Data Loading Tab")
elif selected_tab == 'Formation Evaluation':
    st.title("Formation Evaluation Tab")
elif selected_tab == 'Visualization':
    st.title("Visualization Tab")
