import streamlit as st
import time
import numpy as np
# from Utilities import utilities as ut
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
        st.write('### :one: Mill Chargue level')

        diameter = st.number_input('Efective diameter D (m): ', value = 3.4)
        height = st.number_input('Free Height H (m): ',value = 2.1)

        mill_chargue = st.form_submit_button('Calculate')
    
    
    
    if mill_chargue:
        level = ut.mill_chargue_level(height, diameter)

        st.write(f'Chargue level is {level} %')
    else:
        st.write("")
    
    st.image("./Imagenes/mill_chargue_level.jpg")

with col2:

    with st.form('%Sol to Pulp Density'):
        
        st.write('### :two: % Solids to Pulp density')

        specific_gravity = st.number_input('Ore Specific Gravity:', value = 2.700 )
        percentaje_solids = st.number_input('%Solids (w/w): ', value = 30.000 )

        solid_to_density = st.form_submit_button('Calculate')

    if solid_to_density:
        pulp_density_calc = round(ut.solid_to_density(specific_gravity,percentaje_solids),2)

        st.write(f"Pulp Desnity: {pulp_density_calc}")
    
    with st.form('P.D. To %Sol'):
        
        st.write('### :three: Pulp density to % Solids')

        specific_gravity = st.number_input('Ore Specific Gravity:', value = 2.700)
        pulp_density = st.number_input('Pulp Density: ', value = 1.230)

        density_to_solid = st.form_submit_button('Calculate')

    if density_to_solid:
        percent_solid_calc = round(ut.density_to_solid(specific_gravity,pulp_density),2)

        st.write(f"Weight Percent Solid: {percent_solid_calc}%")


with col3:

    with st.form('Fast Recuperation'):
        st.write('### :four: Metal Recovery')

        calc_recovery = 0.00
        feed_law = st.number_input('Feed Assay(%): ', value = 2.09)
        concentrate_law = st.number_input('Concentrate Assay(%): ', value = 20.0)
        tail_law = st.number_input('Tail Assay(%): ', value = 0.1)

        recovery = st.form_submit_button('Calcualte')

    if recovery:
        calc_recovery = ut.calc_recovery(feed_law, tail_law, concentrate_law)
        st.write(f'Metal Recovery: {calc_recovery} %')

