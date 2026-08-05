import streamlit as st
import sys
from streamlit.web.cli import main
from streamlit.web import cli as stcli

st.title("Hello")
st.subheader("Please Choose a Candidate")

# -------------------------------------------------------------------

# making columns
col1, col2 = st.columns(2)

with col1:
    st.header("Vote for Ayush")
    vote_ayush = st.button("Vote", key="btn_ayush")                     # if we are keeping the same name for the all the buttons then we need to assign them a key

    st.header("Vote for Ravi")
    vote_ravi = st.button("Vote", key="btn_ravi")
    
with col2:
    st.header("Vote for Rinki")
    vote_rinki = st.button("Vote", key="btn_rinki")

    st.header("Vote for Teja")
    vote_teja = st.button("Vote", key="btn_teja")

if vote_ayush:
    st.toast("You voted for Ayush!")            # this disappears after few seconds
elif vote_ravi:
    st.toast("You voted for Ravi!")
elif vote_rinki:
    st.toast("You voted for Rinki!")
elif vote_teja:
    st.toast("You voted for Teja!")


# -------------------------------------------------------------------

# loading image
st.write("Showing Images...")
url = "https://as1.ftcdn.net/v2/jpg/19/12/18/70/1000_F_1912187040_98lrqwC4PW2bnLHqX5iEuv22Y0qkA5WH.jpg"

st.image(url, width=700)


# -------------------------------------------------------------------

# using sidebar
st.sidebar.subheader("This is sidebar")
st.sidebar.selectbox("Choose a number", [1,2,3])




















# -------------------------------------------------------------------

if __name__ == '__main__':
    # Checks if Streamlit is already running
    if st.runtime.exists():
        pass
    else:
        # Simulate the "streamlit run" command
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())