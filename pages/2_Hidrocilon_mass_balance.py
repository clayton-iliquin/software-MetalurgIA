import streamlit as st
from Utilities import utilities as ut
from Utilities import mass_balance as mb
from Utilities import imag_draw

st.set_page_config(
    page_title='Hydrocyclon Mass Balance',
    page_icon = '🌪️',
    layout = 'wide'
)

st.title('🌪️ Hydrocyclon Mass Balance')
ut.logo()

# load functions
cyclon_balance = mb.HydroyclonMassBalance()
chart = cyclon_balance.hydrocyclon_mass_balance_simple_chart()
image_display = './Imagenes/Hydrocyclon_mass_balance.png'
load_data_image = imag_draw.DrawBalances()

col1, col2 = st.columns(2)

with col1:
    with st.form('Input_data'):
        st.write('Enter the data')

        feed_tms = st.number_input('Dry Feed (Tons/hour): ',value = 1622.8)
        
        # feed_rcc = st.number_input('% CC',value = 250)
        feed_sg = st.number_input('Specific gravity: ',value = 2.80)
        solids_feed = st.number_input ('Feed Cyclon (%)',value = 62.2)
        solids_uf = st.number_input ('%Sol U/F Cyclon(%)',value = 76.0)
        solids_of = st.number_input ('%Sol O/f Cyclon(%)',value = 40.0)

        execute = st.form_submit_button('Execute')


    if execute:
        cyclon_balance.hydrocyclon_mass_balance_simple(feed_tms,feed_sg,solids_feed,solids_uf,solids_of,chart)
        image_display = load_data_image.draw_hydrocyclon_simple_balance(chart)

with col2:

    st.image(image_display)

with st.container(border = True):

    st.dataframe(data = chart, hide_index = True, use_container_width = True)
