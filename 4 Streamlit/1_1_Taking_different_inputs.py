import streamlit as st
import sys
from streamlit.web.cli import main
from streamlit.web import cli as stcli

st.title("Hello 🤞")

# making button
if st.button("CLICK"):
    st.success("it is a success")

# -------------------------------------------------------------------

# making a checkbox
temp_1 = st.checkbox('Click the Check Box')
if temp_1:
    st.write("THE CHECKBOX WAS CLICKED")

# -------------------------------------------------------------------

# using radio (can only select only one option)
# putting them in one sentence
items = ['Milk','Rice','Water','Sugar']

# making a clear selection button
if "selected_item" not in st.session_state:
    st.session_state.selected_item = None                   # creating a variabel named 'selected_item' assigning 'None' to it

def clear_selection():
    st.session_state.selected_item=None

# whatever the user selects is saved directly into the 'session_state'
temp_2 = st.radio(
    "PICK ANY ONE : ", 
    options=items, 
    horizontal=True, 
    index=None,                                                 # index=None -- sets the default selction to none
    key='selected_item'                                         # whatever the user selects is saved directly into the variable created as 'selected_item' and will be stored in the session_state
)

st.button('Clear Selection', on_click=clear_selection)          # calls the 'clear_selection' function
if temp_2:
    st.write(f"YOU HAVE CLICKED -- {(temp_2).upper()}")         # getting output in upper case

# -------------------------------------------------------------------


nums = [1,2,3,4,5,6,7,8,9]

if 'nums_var' not in st.session_state:
    st.session_state.nums_var = None

def clear_nums():
    st.session_state.nums_var = None

temp_3 = st.multiselect('SELECT A NUMBER : ', options=nums, default=[])
if temp_3:
    st.write(f"SELECTED NUMBERS ARE {sorted(temp_3)}")


# -------------------------------------------------------------------


# using sliders
st.slider('SELECT YOUR AGE :', 1,30,2)                          # 1 - min value, 30 - max value, 2 - default value

# -------------------------------------------------------------------

if 'temp_age' not in st.session_state:
    st.session_state.temp_age = None

def verify(age):
    st.session_state.temp_age = age
    st.success(f"YOU ARE {age}. \n\n🟢YOU MAY ENTER")


temp_4 = st.selectbox('ARE YOU UNDER AGE :', ['YES', 'NO'], index=None)
if temp_4 == 'YES':
    st.error('❌ YOU ARE NOT ALLOWED')
elif temp_4 == 'NO':
    temp_age_2 = st.slider('SELECT YOUR AGE ',19,100,27)
    if st.button('VERIFY'):
        verify(temp_age_2)




# -------------------------------------------------------------------

if __name__ == '__main__':
    # Checks if Streamlit is already running
    if st.runtime.exists():
        pass
    else:
        # Simulate the "streamlit run" command
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())