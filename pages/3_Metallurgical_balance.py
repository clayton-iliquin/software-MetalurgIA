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

st.title('⚖️ Metallurgical Balance')
ut.logo()

one_conc, two_conc, three_conc = st.tabs(['One concentrate','Two Concentrates','Three Concentrates'])

with one_conc:
    st.write('### One Concentrate Balance')
    data, display =  st.columns([0.35,0.65])
    with data:

        with st.container(border = True):
            st.write('Enter the data: ')
            
            with st.container(border = True):
                st.caption('Mineral')
                
                feed_ton = st.number_input('Feed (Ton): ', value = 150.00)
                feed_humidity = st.number_input('Humidity (%): ', value = 2.00)

            with st.container(border = True):
                st.caption('Feed')

                sep1, sep2 = st.columns([2,1])
                feed_law = sep1.number_input('Feed Law: ',value = 0.3)
                law = sep2.selectbox('Choose:',['%','Oz/Tn'],key = 'law')
                
                element = st.selectbox('Element:',('Cu','Au','Ag','Pb','Zn','Sn'),key = 'element')

            with st.container(border = True):
                st.caption('Concentrate')
                conc_law = st.number_input(f'Concentrate Law {st.session_state.law} : ', value = 20.3)

            with st.container(border = True):
                st.caption('Tail')
                tail_law = st.number_input(f'Tail Law {st.session_state.law} : ', value = 0.20)


            
            balance_1_conc = st.button('Excecute Balance')
            
            chart = mb.mass_balance_1_conc_1_elemet_chart(st.session_state.element, st.session_state.law)
            rec = float()
            if balance_1_conc:
                mb.mass_balance_1_conc_1_element_calc(feed_ton, feed_humidity,feed_law,conc_law,tail_law,chart)

            
            
    with display:
            st.dataframe(data =chart, hide_index = True)
            
            with st.container(border = True):
                st.write(f"Recuperation of {st.session_state.element} is :")


            
        

        



