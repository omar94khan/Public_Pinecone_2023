import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page
from hugchat import hugchat

st.markdown("# Getting Started.")

st.write("Great! Now let's let %s know your name."% st.session_state["pa_name"])

user_name = st.text_input(label="Please enter your username here.")

if "user_name" in st.session_state.keys():
    update = st.button("Update")
    if update:
        st.session_state["user_name"] = user_name

if "user_name" not in st.session_state.keys():
    if user_name:
        st.session_state["user_name"] = user_name


col1, col2 = st.columns(2)

with col1:
    prev_page2 = st.button("Back")
with col2:
    next_page2 = st.button('Next Page.')

# st.session_state


st.session_state["all_inputs"] = []
st.session_state["all_outputs"] = []


if next_page2:
    switch_page('Interface')

if prev_page2:
    switch_page("Introduction")