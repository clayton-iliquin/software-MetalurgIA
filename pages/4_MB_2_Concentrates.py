import streamlit as st
import pandas as pd
from Utilities import utilities as ut
from Utilities import mass_balance as mb

@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun

    return df.to_excel('mass_balanace_2_conc.xlsx', index = False,float_format=",.3f")


st.set_page_config(
    page_title='MB 2 Concentrates',
    page_icon = '⚖️',
    layout = 'wide'
)

# Store the Initial Values in session state

if 'law_1' not in st.session_state:
    st.session_state.law_1 = '%'
    st.session_state.law_2 = '%'
    st.session_state.element_1 = 'Cu'
    st.session_state.element_2 = 'Pb'
    st.session_state.recovery = int()

st.title('⚖️ Mass Balance 2 Concentrates 2 Elements')
ut.logo()

with st.container(border = True):
    st.write('Enter the data: ')
    data_1, data_2, data_3 = st.columns(3)
    
    
    with data_1:
        with st.container(border = True):
            
            st.caption('Load data: ')
            element1, element2 = st.columns(2)
            element_1 = element1.selectbox('Element 1:',('Cu','Au','Ag','Pb','Zn','Sn'),key = 'element_1')
            element_2  = element2.selectbox('Element 2:',('Cu','Au','Ag','Pb','Zn','Sn','Mo'),key = 'element_2')
            
            sep1, sep2 = st.columns([2,1])
            feed_law_1 = sep1.number_input(f'Feed Law {st.session_state.element_1}: ',value = 1.50)
            feed_law_2 = sep1.number_input(f'Feed Law {st.session_state.element_2}: ',value = 1.80)
            law_1 = sep2.selectbox('Choose:',['%','Oz/Tn'],key = 'law_1')
            law_2 = sep2.selectbox('Choose:',['%','Oz/Tn'],key = 'law_2')
        
    with data_2:
        with st.container(border = True):
            st.caption('Mineral')

            c2_feed_ton = st.number_input('Feed (Ton):', value = 1_330.84)
            c2_feed_humidity = st.number_input('Humidity (%):', value = 0.00)
        
        with st.container(border = True):
            st.caption(f'Concentrate {st.session_state.element_1} {st.session_state.law_1}')
            conc_1_law_1 = st.number_input(f'Concentrate Law {st.session_state.element_1} {st.session_state.law_1} : ', value = 29.60)
            conc_1_law_2 = st.number_input(f'Concentrate Law {st.session_state.element_2} {st.session_state.law_2} : ', value = 1.70)
    
    with data_3:

        with st.container(border = True):
            st.caption(f'Concentrate {st.session_state.element_2} {st.session_state.law_2}')
            conc_2_law_1 = st.number_input(f'Concentrate Law {st.session_state.element_1} {st.session_state.law_1} :', value = 1.70)
            conc_2_law_2 = st.number_input(f'Concentrate Law {st.session_state.element_2} {st.session_state.law_2} :', value = 62.30)

        with st.container(border = True):
            st.caption('Tail: ')
            tail_law_1 = st.number_input(f'Tail Law {st.session_state.law_1} : ', value = 0.10)
            tail_law_2 = st.number_input(f'Tail Law {st.session_state.law_2} : ', value = 0.11)
    chart = mb.mass_balance_2_conc_2_elemet_chart(st.session_state.element_1, st.session_state.element_2, st.session_state.law_1, st.session_state.law_2)


but1, but2 = st.columns(2)
balance_2_conc = but1.button('Excecute Balance', use_container_width = True, type = 'primary')
clear_mb_2_conc = but2.button('Clear data', use_container_width = True)


if balance_2_conc:
    mb.mass_balance_2_conc_2_elemet_calc(c2_feed_ton,c2_feed_humidity,feed_law_1,feed_law_2,conc_1_law_1,
    conc_1_law_2, conc_2_law_1, conc_2_law_2, tail_law_1, tail_law_2, chart)

if clear_mb_2_conc:
    chart.iloc[:,1:] = ''


with st.container(border = True):
    
    st.dataframe(data = chart, hide_index = True, use_container_width = True)

# report_mb_2_conc = st.download_button('Download Report',data = convert_df(chart),
#                                     use_container_width = True,file_name='template.xlsx',
#                                      mime = 'application/octet-stream')
