import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page
from hugchat import hugchat
import backend_functions as bf
import pandas as pd


st.markdown("# Journal Entries History")
st.write("Here's your interaction history with ", st.session_state["pa_name"])


# Sidebar contents
with st.sidebar:
    st.title('%s Interface' %st.session_state['pa_name'])
    st.markdown('''
    ## About
    This app is your daily personal assistant who you can tell about your day and it will remember and recall the information as and when required.
    
    💡 Note: No API key required!
    ''')
    add_vertical_space(5)
    st.write('Made by Mining Ninjas')

n_entries = st.number_input(label = "How many latest entries do you want to retrieve? (0 defaults to all)", min_value = 0, step = 1, value = 25)

history = bf.access_entries(namespace=st.session_state["user_name"], k = n_entries)
pd.set_option('display.max_colwidth', None)

st.write(history)

col1, col2 = st.columns(2)
with col1:
    prev_page4 = st.button("Back to Main Interface")
with col2:
    next_page4 = st.button('Log out')


if prev_page4:
    switch_page("Interface")
if next_page4:
    switch_page('Main')
