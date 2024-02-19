import streamlit as st
from Utilities import utilities as ut
from Utilities import mass_balance as mb

st.set_page_config(
    page_title="Hidrociclon Mass Balance",
    page_icon = "🌪",
    layout = "wide"
)

st.title("Mass Balance")
ut.logo()
col1, col2, col3 = st.columns(3)

with col1:
    with st.form('Input_data'):
        st.write('Enter de data')


        feed_tms = st.number_input('Feed (Tons/hour): ',value = 550.56)
        feed_rcc = st.number_input('% CC',value = 250)
        feed_sg = st.number_input('Specific gravity: ',value = 1.56)
        uf_density = st.number_input ('U/F density',value = 1.43)
        of_density = st.number_input ('O/F density',value = 1.14)

        excecute = st.form_submit_button('Excecute')

    if excecute:
        of_balance,uf_balance,feed_balance = mb.hidrociclon_balance(feed_tms,feed_rcc,feed_sg,uf_density,of_density)

    else:
        of_balance,uf_balance,feed_balance =[["","","","",""],["","","","",""],["","","","",""]]
    

    st.divider()

    st.write('### Legend')
    legend = ["TMS (ton/hr)","%Sol","TMA (ton/hr)","Density (Ton/m3)","TMP (Ton/hr)"]
    cols = ut.grid(2)
    for col, descr in zip(cols,legend):
        cont = col.container(height=45)
        cont.caption(descr)


with col2:
    st.write('### Feed Balance')
    ut.grid_display(2,feed_balance)
    
    st.divider()

    st.image("Imagenes\Hidrociclon.jpg")

with col3:
    st.write('### OF Balance')
    ut.grid_display(2,of_balance)

    st.divider()
    st.write('### UF Balance')
   
    ut.grid_display(2,uf_balance)

    st.divider()
    