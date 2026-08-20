import streamlit as st
import sys
from streamlit.web.cli import main
from streamlit.web import cli as stcli
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# -------------------------------------------------------------------------------------------------
st.set_page_config(layout='wide')
st.title("Plotting in Streamlit")
# -------------------------------------------------------------------------------------------------

# loading the dataframe
df = pd.read_csv("Final Visualization Dataset.csv")

st.button('Refresh')
st.dataframe(df.sample(10))

# -------------------------------------------------------------------------------------------------

# making seaborn plots (SEABORN PLOTS ARE NOT INTERACTIVE)
# st.write("Seaborn Plots")
# fig, ax = plt.subplots()
# sns.histplot(data=df, x='Compensation Rate', ax=ax)
# st.pyplot(fig)

# -------------------------------------------------------------------------------------------------

# making plotly plots
st.write("Plotly Plots")
fig = px.histogram(df, x='Compensation Rate')
fig.update_traces(marker_line_color='black', marker_line_width=1)
st.plotly_chart(fig)




# -------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    if st.runtime.exists():
        pass
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())


