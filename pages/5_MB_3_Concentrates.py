import streamlit as st
import pandas as pd
from Utilities import utilities as ut
from Utilities import mass_balance as mb



st.set_page_config(
    page_title='Mass Balance 3 Conc',
    page_icon = '⚖️',
    layout = 'wide'
)

# Store the Initial Values in session state

if 'law_1_mb_3' not in st.session_state:
    st.session_state.law_1_mb_3 = '%'
    st.session_state.law_2_mb_3 = '%'
    st.session_state.law_3_mb_3 = '%'
    st.session_state.element_1_mb_3 = 'Cu'
    st.session_state.element_2_mb_3 = 'Pb'
    st.session_state.element_3_mb_3 = 'Zn'
    st.session_state.recovery_mb_3 = int()

st.title('⚖️ Mass Balance 3 Concentrates 3 Elements')
ut.logo()

with st.container(border = True):
    data_1, data_2, data_3 = st.columns(3)
    
    with data_1:
        with st.container(border = True):
            
            element1, element2, element3 = st.columns(3)
            element_1_mb_3 = element1.selectbox('Element 1:',('Cu','Au','Ag','Pb','Zn','Sn'),key = 'element_1_mb_3')
            element_2_mb_3  = element2.selectbox('Element 2:',('Cu','Au','Ag','Pb','Zn','Sn','Mo'),key = 'element_2_mb_3')
            element_3_mb_3  = element3.selectbox('Element 3:',('Cu','Au','Ag','Pb','Zn','Sn','Mo'),key = 'element_3_mb_3')

            sep1, sep2 = st.columns([2,1])
            feed_law_1 = sep1.number_input(f'Feed Law {st.session_state.element_1_mb_3}: ',value = 0.89)
            feed_law_2 = sep1.number_input(f'Feed Law {st.session_state.element_2_mb_3}: ',value = 1.83)
            feed_law_3 = sep1.number_input(f'Feed Law {st.session_state.element_3_mb_3}',value = 5.66)

            law_1_mb_3 = sep2.selectbox('Choose:',['%','Oz/Tn'],key = 'law_1_mb_3')
            law_2_mb_3 = sep2.selectbox('Choose:',['%','Oz/Tn'],key = 'law_2_mb_3')
            law_3_mb_3 = sep2.selectbox('Choose:',['%','Oz/Tn'],key = 'law_3_mb_3')
        
        with st.container(border = True):
            
            mb3_feed_ton = st.number_input('Feed (dry Ton):', value = 4_000.0)
        
    with data_2:
        
        with st.container(border = True):
            st.caption(f'Concentrate of {st.session_state.element_1_mb_3}')
            conc_1_law_1 = st.number_input(f'Concentrate Law {st.session_state.element_1_mb_3} {st.session_state.law_1_mb_3} : ', value = 24.29)
            conc_1_law_2 = st.number_input(f'Concentrate Law {st.session_state.element_2_mb_3} {st.session_state.law_2_mb_3} : ', value = 7.45)
            conc_1_law_3 = st.number_input(f'Concentrate Law {st.session_state.element_3_mb_3} {st.session_state.law_3_mb_3} :', value = 6.99)
        
        with st.container(border = True):
            st.caption(f'Concentrate of {st.session_state.element_2_mb_3}')
            conc_2_law_1 = st.number_input(f'Concentrate Law {st.session_state.element_1_mb_3} {st.session_state.law_1_mb_3} :', value = 0.85, key = 102030)
            conc_2_law_2 = st.number_input(f'Concentrate Law {st.session_state.element_2_mb_3} {st.session_state.law_2_mb_3} :', value = 60.97, key = 102031)
            conc_2_law_3 = st.number_input(f'Concentrate Law {st.session_state.element_3_mb_3} {st.session_state.law_3_mb_3} :', value = 8.90, key = 102032)

    with data_3:

        with st.container(border = True):
            st.caption(f'Concentrate of {st.session_state.element_3_mb_3}')
            conc_3_law_1 = st.number_input(f'Concentrate Law {st.session_state.element_1_mb_3} {st.session_state.law_1_mb_3} :', value = 2.74, key = 102033)
            conc_3_law_2 = st.number_input(f'Concentrate Law {st.session_state.element_2_mb_3} {st.session_state.law_2_mb_3} :', value = 0.82, key = 102034)
            conc_3_law_3 = st.number_input(f'Concentrate Law {st.session_state.element_3_mb_3} {st.session_state.law_3_mb_3} :', value = 56.14, key = 102035)

        with st.container(border = True):
            st.caption('Tail: ')
            tail_law_1 = st.number_input(f'Tail Law {st.session_state.element_1_mb_3} {st.session_state.law_1_mb_3} : ', value = 0.11)
            tail_law_2 = st.number_input(f'Tail Law {st.session_state.element_2_mb_3} {st.session_state.law_2_mb_3} : ', value = 0.17)
            tail_law_3 = st.number_input(f'Tail Law {st.session_state.element_3_mb_3} {st.session_state.law_3_mb_3} :', value = 0.66)

    chart = mb.mass_balance_3_conc_3_elemet_chart(st.session_state.element_1_mb_3, st.session_state.element_2_mb_3, st.session_state.element_3_mb_3, st.session_state.law_1_mb_3, st.session_state.law_2_mb_3, st.session_state.law_3_mb_3)


but1, but2 = st.columns(2)
balance_3_conc = but1.button('Excecute Balance', use_container_width = True)
clear_mb_3_conc = but2.button('Clear Data', use_container_width = True)

if balance_3_conc:
    mb.mass_balance_3_conc_3_elemet_calc(mb3_feed_ton, feed_law_1,feed_law_2,feed_law_3,
    conc_1_law_1, conc_1_law_2,conc_1_law_3, conc_2_law_1, conc_2_law_2, conc_2_law_3,
    conc_3_law_1, conc_3_law_2, conc_3_law_3, tail_law_1, tail_law_2, tail_law_3, chart)

if clear_mb_3_conc:
    chart.iloc[:,1:] = ''

with st.container(border = True):
    
    st.dataframe(data = chart, hide_index = True, use_container_width = True)