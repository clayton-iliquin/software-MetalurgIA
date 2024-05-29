import streamlit as st
import pandas as pd
from Utilities import utilities as ut
from Utilities import mass_balance as mb
from Utilities import imag_draw


st.set_page_config(
    page_title='Reverse Circuit Mass Balance',
    page_icon = '🌊',
    layout = 'wide'
)

# if 'law_1_mb_3' not in st.session_state:
#     st.session_state.law_1_mb_3 = '%'

st.title('🌊↪️ Mass Balance D SAG Grinding Circuit')
ut.logo()

with st.container(border = True):
    mineral, solids = st.columns(2)

    with mineral:
        with st.container(border = True):
            fresh_charge = st.number_input('Fresh Charge (Ton): ', value = 421.053)
            moisture = st.number_input('Moisture (%): ', value = 5.0)
            spec_grav =st.number_input('Specific Gravity: ', value = 2.80)

        with st.container(border = True):
            st.caption('SAG Mill')

            sag_solid_discharge = st.number_input('%Sol SAG Discharge (%): ', value = 82.43)
            cc_pebbles = st.number_input('CC Pebbles (%):', value = 30)
            moisture_pebbles = st.number_input('Moisture Pebbles (%): ', value = 2.5)


    with solids.container(border=True):
        st.caption('Ball Mill')

        over_sol = st.number_input('%Sol Overflow Cyclon:', value = 40.00)
        under_sol = st.number_input('%Sol Underflow Cyclon:', value = 76.00)
        feed_sol = st.number_input('%Sol Feed Cyclon:', value = 64.1)
        discharge_sol = st.number_input('%Sol Mill Discharge:', value = 72.00)

reverse_circuit = mb.DSagGrinding()
chart = reverse_circuit.chart_d_sag_grinding()
image_display = "./Imagenes/d_sag_circuit.png"
load_data_image = imag_draw.DrawBalances()

with st.container(border=True):
    but_1, but_2 = st.columns(2)
    
    balance_reverse_circuit = but_1.button('Execute Balance', use_container_width = True, type = "primary")
    clear_reverse_circuit = but_2.button('Clear Data', use_container_width = True)

    if balance_reverse_circuit:
        reverse_circuit.mass_balance_d_sag(fresh_charge,moisture,spec_grav,sag_solid_discharge,cc_pebbles,moisture_pebbles,over_sol,under_sol,feed_sol,discharge_sol,chart)
        image_display = load_data_image.draw_d_sag_mass_balance(chart)

    if clear_reverse_circuit:
        chart.iloc[:,1:] = ' '

st.image(image_display)

with st.container(border = True):
    st.dataframe(data =chart, hide_index = True, use_container_width = True)