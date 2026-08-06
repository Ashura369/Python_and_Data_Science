import streamlit as st
import sys
from streamlit.web.cli import main
from streamlit.web import cli as stcli
import pandas as pd


# -------------------------------------------------------------------
st.title("Using Pandas in Streamlit")

# -------------------------------------------------------------------

# taking the files in input (only csv and xlsx)
file_exist = st.file_uploader("UPLOAD THE DATASET (csv / xlsx ONLY)", type=['csv','xlsx'])
if file_exist is not None:
    st.toast("File Successfully Uploaded")
    file_name = file_exist.name.lower()

    if file_name.endswith('.csv'):
        df = pd.read_csv(file_exist)
        st.subheader("Data Preview")
        st.write(f"Rows : {df.shape[0]}")
        st.write(f"Features : {df.shape[1]}")
        st.dataframe(df)
    elif file_name.endswith('.xlsx'):
        df = pd.read_excel(file_exist)
        st.subheader("Data Preview")
        st.write(f"Rows : {df.shape[0]}")
        st.write(f"Features : {df.shape[1]}")
        st.dataframe(df)



# -------------------------------------------------------------------













# -------------------------------------------------------------------


if __name__ == '__main__':
    if st.runtime.exists():
        pass
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())




