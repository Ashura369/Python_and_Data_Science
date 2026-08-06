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

st.image(url, width=300)


# -------------------------------------------------------------------

# using sidebar
st.sidebar.subheader("This is sidebar")
st.sidebar.selectbox("Choose a number", [1,2,3])

# -------------------------------------------------------------------

# using expander
# within expansion you can put anything you want
with st.expander('Show the expansion'):

    # using texts inside expander
    st.write("""
    1. This is step 1
    1. This is step 2
    1. This is step 3
    1. This is step 4
""")

    # using buttonos inside expander
    col1, col2 = st.columns(2)
    with col1:
        temp_yes = st.button("YES")
            
    with col2:
        temp_no = st.button("NO")

    if temp_yes:
        st.toast("YOU CLICKED YES")
    elif temp_no:
        st.toast("YOU CLICKED NO")
        
# -------------------------------------------------------------------

# Changing background color

# default background color selection
default_bg_black = "#000000"
default_text_black = "#FFFFFF"

# white background color selection
bg_white = "#FFFFFF"
text_white = "#000000"


if "bg_color" not in st.session_state:
    st.session_state.bg_color = default_bg_black
if "txt_color" not in st.session_state:
    st.session_state.txt_color = default_text_black


# making a function for setting the theme of the page
def set_background(bg_color, txt_color):
    st.markdown(
        f"""
            <style>
            .stApp{{
                background-color : {bg_color};
                color : {txt_color}
            }}

            /* Applying color filter on buttons */

            div.stButton > Button{{
                background-color: {txt_color} !important;   /* The light grey hover color */
                color: {bg_color} !important;               /* Text color */
                border: 1px solid #d6d6d6 !important;       /* Optional border match */
            }}

            </style>
        
            """,
            unsafe_allow_html = True
    )


st.write("Change Background")
col3, col4 = st.columns(2)
with col3:
    if st.button("WHITE"):
        st.session_state.bg_color = bg_white
        st.session_state.txt_color = text_white
        st.rerun()                                                  # 'st.rerun()' immediately interrupts the execution of the script from that exact point and restarts it from the very beginning.
with col4:
    if st.button("BLACK"):
        st.session_state.bg_color = default_bg_black
        st.session_state.txt_color = default_text_black
        st.rerun()


# making black theme as the default
set_background(st.session_state.bg_color, st.session_state.txt_color)

# -------------------------------------------------------------------

# using markdown
st.markdown("## This is Markdown")
st.markdown("> This is notes")


# -------------------------------------------------------------------

if __name__ == '__main__':
    # Checks if Streamlit is already running
    if st.runtime.exists():
        pass
    else:
        # Simulate the "streamlit run" command
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())