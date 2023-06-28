import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page
from hugchat import hugchat

st.markdown("# Getting Started.")


pa_name = st.text_input(label="What would you like to call your new Personal Assistant.")

# For when the name has been assigned previously
if "pa_name" in st.session_state.keys():
    update = st.button("Update")

    if update:
        st.session_state["pa_name"] = pa_name

# For when the name has not been assigned previously
if "pa_name" not in st.session_state.keys():
    if pa_name:
        st.session_state["pa_name"] = pa_name

# Buttons to switch between pages
col1, col2 = st.columns(2)

with col1:
    prev_page1 = st.button("Reset")
with col2:
    next_page1 = st.button('Next Page.')

# st.session_state

if next_page1:
    switch_page('User Name')

if prev_page1:
    switch_page("app")