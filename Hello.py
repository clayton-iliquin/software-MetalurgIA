import streamlit as st
from Utilities import utilities as ut


st.set_page_config(
    page_title = 'Welcome to **Metalurg.IA** ',
    page_icon = "👷‍♀️"
)

st.title("Welcome to **Metalurg.IA** Software Probe")
ut.logo()

st.sidebar.success("Select an application to use in the slide bar ⬆")

st.markdown(
    """
    This is a Demo for the use of Metalurgical Aplications in web browser.


    ### Our Blog
    - Take a Look of our block (Espanish) [Metarlurg.IA Blog](https://metalurg-ia.blogspot.com/)
    """)