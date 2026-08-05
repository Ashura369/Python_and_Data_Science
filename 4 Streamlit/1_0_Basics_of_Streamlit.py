import streamlit as st
import sys
from streamlit.web.cli import main

# this is title
st.title("Hello World")

# this is for Subheadings
st.subheader("pradhans36933@gmail.com")

# this is for putting texts only
st.text("Hello this is Biswajeet Pradhan, from Bhubaneswar Odisha.")

# this is used for texts, but also for markdown, different plots etc.
st.write("I like coding on VS Code.")

# used for a selectbox (can also put strings with numbers)
# ONLY FOR SELECTING ONE ITEM
st.selectbox("SELECT NUMBERS : ", [1,2,3,4,5])

# used for selecting multiple items
# if 'defaults=[]' is empty then it is set to nothing, if you put a number, that number will be selected by default in the website
# this one by default comes with select all option with all other items in the list
temp = [1,2,3,4,5,6,7,8,9,10]
st.multiselect("SELECT NUMBERS : ", options=temp, default=[])


num = st.multiselect('CHOOSE : ', options=temp, default=[])
# the text will only show if the numbers are chosen in the box
if num:
    st.write(f"YOU HAVE CHOSEN NUMBER {sorted(num)}")               # chosen sorted function in python

    # this is a success section
    st.success("🎉 IT IS A SUCCESS")

    # this is error section
    st.error("⚠️ IT IS AN ERROR")

