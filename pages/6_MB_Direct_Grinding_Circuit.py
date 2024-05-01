import streamlit as st
import pandas as pd
from Utilities import utilities as ut
from Utilities import mass_balance as mb



st.set_page_config(
    page_title='Direct Circuit Mass Balance',
    page_icon = '🌊',
    layout = 'wide'
)

# if 'law_1_mb_3' not in st.session_state:
#     st.session_state.law_1_mb_3 = '%'

st.title('🌊  Mass Balance Direct Grinding Circuit')
ut.logo()

with st.container(border = True):
    mineral, solids = st.columns(2)

    with mineral.container(border = True):
        fresh_charge = st.number_input('Fresh Charge (Ton):', value = 421.10)
        moisture = st.number_input('Moisture (%):', value = 5.0)
        spec_grav =st.number_input('Specific Gravity', value = 2.80)

    with solids.container(border=True):
        over_sol = st.number_input('%Sol Overflow Cyclon: ', value = 40.00)
        under_sol = st.number_input('%Sol Underflow Cyclon: ', value = 76.00)
        feed_sol = st.number_input('%Sol Feed Cyclon: ', value = 62.2)

direct_circuit = mb.DirectGrinding()
chart = direct_circuit.chart_balance()

with st.container(border=True):
    but_1, but_2 = st.columns(2)
    
    balance_direct_circuit = but_1.button('Execute Balance', use_container_width = True)
    clear_direct_circuit = but_2.button('Clear Data', use_container_width = True)

    if balance_direct_circuit:
        direct_circuit.mass_balance_direct_circuit(fresh_charge,moisture,spec_grav, over_sol,under_sol,feed_sol,chart)
        
    if clear_direct_circuit:
        chart.iloc[:,1:] = ' '

st.dataframe(data =chart, hide_index = True)