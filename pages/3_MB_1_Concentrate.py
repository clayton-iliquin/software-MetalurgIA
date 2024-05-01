import streamlit as st
import pandas as pd
from Utilities import utilities as ut
from Utilities import mass_balance as mb



st.set_page_config(
    page_title='Metallurgical Balance',
    page_icon = '⚖️',
    layout = 'wide'
)

# Store the Initial Values in session state

if 'law' not in st.session_state:
    st.session_state.law = '%'
    st.session_state.element = 'Cu'
    st.session_state.recovery = int()

st.title('⚖️ Mass Balance 1 Concentrate 1 Element')
ut.logo()

st.write('### One Concentrate Balance')

with st.container(border = True):
    mineral, feed, laws = st.columns(3)
    
    with mineral:
        with st.container(border = True):
            st.caption('Mineral')
            
            feed_ton = st.number_input('Feed (Ton): ', value = 150.00,key = 'feed_ton')
            feed_humidity = st.number_input('Humidity (%): ', value = 2.00, key = 'feed_hum')

    with feed: 
        with st.container(border = True):
            st.caption('Feed')

            sep1, sep2 = st.columns([2,1])
            feed_law = sep1.number_input('Feed Law: ',value = 0.3, key = 'feed_law')
            law = sep2.selectbox('Choose:',['%','Oz/Tn'],key = 'law')
            
            element_1 = st.selectbox('Element:',('Cu','Au','Ag','Pb','Zn','Sn'),key = 'element_1')
    
    with laws:
        with st.container(border = True):
            st.caption('Concentrate')
            conc_law = st.number_input(f'Concentrate Law {st.session_state.law} : ', value = 20.3, key = 'conc_law')

        with st.container(border = True):
            st.caption('Tail')
            tail_law = st.number_input(f'Tail Law {st.session_state.law} : ', value = 0.20, key = 'tail_law')

chart = mb.mass_balance_1_conc_1_elemet_chart(st.session_state.element_1, st.session_state.law)
rec = float()


but_1, but_2 = st.columns(2)

balance_1_conc = but_1.button('Execute Balance', use_container_width = True)
clear_1_conc = but_2.button('Clear Data', use_container_width = True)

if balance_1_conc:
    mb.mass_balance_1_conc_1_element_calc(feed_ton, feed_humidity,feed_law,conc_law,tail_law,chart)
    st.session_state.recovery = ut.calc_recovery(feed_law, tail_law, conc_law)

if clear_1_conc:
    chart.iloc[:,1:] = ' '
    st.session_state.recovery = 0

st.dataframe(data =chart, hide_index = True)

with st.container(border = True):
    st.write(f"Recuperation of {st.session_state.element_1} is : {st.session_state.recovery} %")
    
