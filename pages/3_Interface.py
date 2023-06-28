import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page
from hugchat import hugchat
import backend_functions as bf

st.markdown("# All done!")
st.write("Greetings from ", st.session_state["pa_name"])


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

input = st.text_input("So how can I be of assistance today?")


output = bf.final_PA(input, namespace=st.session_state["user_name"])
st.write(output)

col1, col2 = st.columns(2)

with col1:
    prev_page3 = st.button("Back")
    if prev_page3:
        switch_page("User Name")

with col2:
    next_page3 = st.button("Check past entries")
    if next_page3:
        switch_page("Previous Entries")