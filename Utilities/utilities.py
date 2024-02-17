import streamlit as st
from streamlit_extras.app_logo import add_logo

def logo():
    add_logo(
        "https://raw.githubusercontent.com/clayton-iliquin/software-MetalurgIA/blob/b8c1cc7fec5884a4c96ec3dfb2ba7c6462c70093/Imagenes/Hidrociclon.jpg",
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