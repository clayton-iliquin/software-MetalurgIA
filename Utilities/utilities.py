import streamlit as st
from streamlit_extras.app_logo import add_logo
from PIL import Image

def logo():
    path = "Imagenes/Metalurg_app.png"
    #logo = Image.open(path)
    add_logo(
        path,
        height =90)


def grid(n_rows):
    """
    Create a grid of n columns and n+1 rows 
    """
    rows = rows = [st.columns(n_rows) for _ in range(n_rows+1)]
    cols = [column for row in rows for column in row]

    return cols

def grid_display(n_rows,list_data):
    """
    Create a grid of n columns and n+1 rows 
    """
    rows = rows = [st.columns(n_rows) for _ in range(n_rows+1)]
    cols = [column for row in rows for column in row]

    for col, data in zip(cols,list_data):
        cont = col.container(height=50)
        cont.write(data)

def solid_to_density(sepecific_graviti, percent_solid):
    pulp_density = 1/((percent_solid/100)/sepecific_graviti + 1 - (percent_solid/100))

    return pulp_density

def density_to_solid(sepecific_graviti, pulp_density):
    percent_solid = ((1/pulp_density)-1)/((1/sepecific_graviti)-1)*100

    return percent_solid
