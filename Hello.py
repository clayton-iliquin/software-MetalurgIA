import streamlit as st
from Utilities import utilities as ut


st.set_page_config(
    page_title = 'Welcome',
    page_icon = "👷‍♀️",
    initial_sidebar_state ="expanded",
    layout = "wide"
)

st.title('Welcome to Metalurg.IA Software Probe')
ut.logo()
st.sidebar.success("This is a Metlaurg.IA App, choose a tool 👆 o go home 🏠 to explore the menu")

st.write("""This is a demo app who contains some useful tools for fast calculations and application  for mineral processing.
Please explore our fast tools and mass balance:
""")

col1, col2 = st.columns(2)

with col1: 
    with st.container(border = True):
        st.write("**Calcs**")
        
        st.page_link("pages/1_Tools.py" ,label = """ 
        #Tools:
        1️⃣ Mill Chargue Level.
        2️⃣ %Sol to Pulp Density
        3️⃣ Pulp Density to %Sol
        4️⃣ Recovery Calc""", 
        icon = "🧰",
        use_container_width = False)
        

with col2.container(border = True):
    st.write("**Mass Balance**")
    
    st.page_link("pages/2_Hidrocilon_mass_balance.py" ,label = "Hidrociclon Balance", icon = "🌪️")
    st.page_link("pages/3_Metallurgical_balance.py", label =  """
    Mass Balance:
    1️⃣ 1 Concen. - 1 Metal.
    2️⃣ 2 Concen. - 2 Metals.
    """, icon = "⚖️")
     


st.markdown(
    """
    This is a Demo for the use of Metalurgical Aplications in web browser.


    ### About Us
    - Take a Look of our block (Espanish) [Metarlurg.IA Blog](https://metalurg-ia.blogspot.com/).
    - Our LinkedIn Profiles:
        - [Clayton Jhordan Iliquin Zavaleta](https://www.linkedin.com/in/clayton-jhordan-iliquin-zavaleta/)

    """)