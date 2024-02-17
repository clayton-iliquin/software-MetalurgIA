import streamlit as st
import time
import numpy as np
from Utilities import utilities as ut

st.set_page_config(
    page_title = 'Tools',
    page_icon = "🧰",
    layout = 'wide'
)

st.title("Fast Tools To Use:")

ut.logo()

col1, col2, col3 = st.columns(3)

with col1:

    with st.form('Mill Chargue level'):
        st.write('### Mill Chargue level')

        diameter = st.number_input('Efective diameter D (m): ', value = 3.4)
        height = st.number_input('Free Height H (m): ',value = 2.1)

        mill_chargue = st.form_submit_button('Calculate')
    
    
    
    if mill_chargue:
        level = round((1.13 - 1.23*(height/diameter))*100,2)

        st.write(f'Chargue level is {level} %')
    else:
        st.write("")
    
    st.image('https://raw.githubusercontent.com/clayton-iliquin/software-MetalurgIA/blob/main/Imagenes/mill_chargue_level.jpg')

