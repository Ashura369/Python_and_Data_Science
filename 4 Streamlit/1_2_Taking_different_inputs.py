import streamlit as st
import sys
from streamlit.web import cli as stcli

# -------------------------------------------------------------------

st.title("Welcome to the page")

# -------------------------------------------------------------------

# taking numerical input from user
temp_age = st.number_input("Select your age (between 1 to 100)", min_value=1, max_value=100, value=None)                                  # by default it will be selected to 'None'
if temp_age:
    st.write(f'You selected {temp_age}')


# -------------------------------------------------------------------

# taking string input

# this function checks for valid phone numbers
def check_phone_no(number):
    try:
        temp_num = number.replace(" ","").replace("-","")
        int(temp_num)

        if (len(temp_num) >= 10) and (len(temp_num) <= 12):
            return True, temp_num
        else:
            st.error("Please enter a phone number with min 10 digit and max 12 digit")
            return False, None
    except ValueError:
        st.error("Please enter a valid phone number using only digits!")
        return False, None




# putting both name and email inputs in column format
col1, col2 = st.columns(2)

with col1:      # puts items on the left
    temp_name = st.text_input('Enter your name')
    temp_phone = st.text_input('Enter your phone no.')

    temp_1 = False
    temp_2 = ""

    if temp_phone:
        temp_1, temp_2 = check_phone_no(temp_phone)


with col2:      # puts items on the right
    temp_email = st.text_input('Enter your email')

if temp_name and temp_email and temp_1:
    st.write(f"Entered name : {temp_name.upper()}")
    st.write(f"Entered email : {temp_email}")
    st.write(f"Entered phone : {temp_2}")

# -------------------------------------------------------------------

# using select slider
st.select_slider("Rating", options=["Bad", "Okay", "Good", "Great"])


# -------------------------------------------------------------------

# taking date input
temp_date = st.date_input("Enter date", value=None, format="DD/MM/YYYY")
if temp_date:
    st.write(f"Entered date : {temp_date}")

# -------------------------------------------------------------------

# toggle input
if st.toggle("Toggle here"):
    st.write('Toggle ON')
else:
    st.write('Toggle OFF')

# -------------------------------------------------------------------

# picking a custom color
st.color_picker("Pick a custom color")

# -------------------------------------------------------------------

# file uploader
st.file_uploader("Upload Resume")

# -------------------------------------------------------------------

# camera input
st.camera_input("Turn on camera")



# -------------------------------------------------------------------

if __name__ == '__main__':
    # Checks if Streamlit is already running
    if st.runtime.exists():
        pass
    else:
        # Simulate the "streamlit run" command
        sys.argv = ["streamlit", "run", sys.argv[0]]
        sys.exit(stcli.main())