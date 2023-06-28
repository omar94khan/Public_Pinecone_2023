import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.switch_page_button import switch_page
from hugchat import hugchat

       
for key in st.session_state:
    del st.session_state[key]

st.markdown(
    """
    # Personal Assistant - A Pinecone Hackathon Submission!

    This project is developed by the Mining Ninjas for the Pinecone Hackathon 2023. 


    The purpose of this project was to build a Personal Assistant that you can use for making journal entries, and then later ask the assistant to callback information you fed it earlier through simple queries.

    The PA will distinguish between your journal entries, and your queries, and then respond accordingly.

    Let's proceed to the next page.
"""
)

col1, col2 = st.columns(2)

with col2:
    next_page = st.button('Next Page.')

if next_page:
    switch_page('Introduction')