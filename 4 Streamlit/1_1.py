import streamlit as st
import sys
from streamlit.web.cli import main

st.title("Hello")

# making button
if st.button("CLICK"):
    st.success("it is a success")

# -------------------------------------------------------------------

# making a checkbox
temp_1 = st.checkbox('Click to Check Here')
if temp_1:
    st.write("THE CHECKBOX WAS CLICKED")

# -------------------------------------------------------------------

# using radio (can only select only one option)
# putting them in one sentence
items = ['Milk','Rice','Water','Sugar']

# making a clear selection button
if "selected_item" not in st.session_state:
    st.session_state.selected_item = None

def clear_selection():
    st.session_state.selected_item=None

temp_2 = st.radio(
    "PICK ANY ONE : ", 
    options=items, 
    horizontal=True, 
    index=None,  # index=None -- sets the default selction to none
    key='selected_item'
)

st.button('Clear Selection', on_click=clear_selection)
if temp_2:
    st.write(f"YOU HAVE CLICKED -- {(temp_2).upper()}")        # getting output in upper case

# -------------------------------------------------------------------



