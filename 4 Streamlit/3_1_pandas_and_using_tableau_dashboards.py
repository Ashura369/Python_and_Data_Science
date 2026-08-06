import streamlit as st
import sys
from streamlit.web.cli import main
from streamlit.web import cli as stcli
import pandas as pd


# -------------------------------------------------------------------

# THIS MUST BE THE FIRST STREAMLIT COMMAND!
# It forces the website to be full-screen width instead of a narrow column
st.set_page_config(layout="wide")

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
        
    elif file_name.endswith('.xlsx'):
        df = pd.read_excel(file_exist)


    st.subheader("Data Preview")
    st.write(f"Rows : {df.shape[0]}")
    st.write(f"Features : {df.shape[1]}")

    col1, col2 = st.columns(2)
    with col1:
        st.write("Describing the Dataset")
        st.dataframe(df.describe())
    with col2:
        st.write("Checking for Datatypes")
        st.dataframe(df.dtypes)

    # -------------------------------------------------------------------

# making multiple tableau dashboards

# Using tableau dashboards in streamlit
import streamlit.components.v1 as components

type = [
    'Centralized Visualisation of Existing Problems', 
    'Performance, Quality, and Error Analysis', 
    'Efficiency Status and Cross-Metrics Diagnostics'
]

selection = st.selectbox('Select the Tableau Presentation', options=type, index=None)

left, center, right = st.columns([1,15,1])

if selection == 'Centralized Visualisation of Existing Problems':
    embed_code_1 = st.secrets["Centralized_Visualisation_of_Existing_Problems"]   
    with center: 
        components.html(embed_code_1, height=900, scrolling=True)

elif selection == 'Performance, Quality, and Error Analysis':
    embed_code_2 = st.secrets["Performance_Quality_and_Error_Analysis"]
    with center:
        components.html(embed_code_2, height=900, scrolling=True)

elif selection == 'Efficiency Status and Cross-Metrics Diagnostics':
    embed_code_3 = st.secrets['Efficiency_Status_and_Cross_Metrics_Diagnostics']
    with center:
        components.html(embed_code_3, height=900, scrolling=True)



# -------------------------------------------------------------------

st.subheader("My Tableau Dashboard")
tableau_embed_code = "<div class='tableauPlaceholder' id='viz1786030957325' style='position: relative'><noscript><a href='#'><img alt='Thales Group - Efficiency Status and Cross-Metrics Diagnostics ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Th&#47;ThalesGroup-EfficiencyStatusandCross-MetricsDiagnostics&#47;Dashboard3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='ThalesGroup-EfficiencyStatusandCross-MetricsDiagnostics&#47;Dashboard3' /><param name='tabs' value='no' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Th&#47;ThalesGroup-EfficiencyStatusandCross-MetricsDiagnostics&#47;Dashboard3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1786030957325');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.height='1627px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"

# putting the tableau presentation at the center of the webpage
# Creingat 3 columns. The middle one is 4x wider than the side ones!
# [1, 4, 1] means: Small Left Column, HUGE Middle Column, Small Right Column
left_spacer, center_column, right_spacer = st.columns([1, 15 , 1])

with center_column:
    components.html(tableau_embed_code, height=900, scrolling=True)


# -------------------------------------------------------------------

if __name__ == '__main__':
    if st.runtime.exists():
        pass
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())




