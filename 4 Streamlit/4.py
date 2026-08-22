import streamlit as st
import sys
from streamlit.web.cli import main
from streamlit.web import cli as stcli
import pandas as pd
import seaborn as sns
import plotly.express as px

# -------------------------------------------------------------------------------------------------
st.set_page_config(layout='wide')
st.title("Plotting in Streamlit")
# -------------------------------------------------------------------------------------------------

# loading the dataframe
df = pd.read_csv("Final Visualization Dataset.csv")

st.button('Refresh')
st.dataframe(df.sample(5))
# -------------------------------------------------------------------------------------------------

# showing columns with different datatypes
label_dtype = ['int','float','object']
btn_dtype = st.multiselect('Select Data Type', options=label_dtype)
if btn_dtype:
    st.write(f"No. of Columns : {len(df.select_dtypes(include=btn_dtype).columns)}")
    st.write(", ".join(df.select_dtypes(include=btn_dtype).columns))
    st.dataframe(df.select_dtypes(include=btn_dtype).head(5))


# -------------------------------------------------------------------------------------------------

# making seaborn plots (SEABORN PLOTS ARE NOT INTERACTIVE)
# st.write("Seaborn Plots")
# fig, ax = plt.subplots()
# sns.histplot(data=df, x='Compensation Rate', ax=ax)
# st.pyplot(fig)

# -------------------------------------------------------------------------------------------------
# making plotly plots

# histogram
st.subheader("Plotly Histogram Plot")

# plot 1
fig = px.histogram(df, x='Compensation Rate', color='Gender',
                    color_discrete_map={'Male' : 'Red', 'Female' : 'Blue'}
                   )
fig.update_traces(marker_line_color='black', marker_line_width=1)
fig.update_layout(bargap=0.2, title='Histogram for Compentation Rate', xaxis_title='Compentation Rate', yaxis_title='Count')
st.plotly_chart(fig)
st.write()

# plot 2
fig = px.histogram(df, y='Hourly Rate', x='Job Role', color_discrete_sequence=['blue'], 
                   title='Hourly Rate at Different Job Roles for Male and Females', 
                   text_auto=True,
                   facet_col='Gender'
                   )
fig.update_traces(marker_line_color='black', marker_line_width=1, textposition='outside')
st.plotly_chart(fig)

# plot 3
fig = px.pie(df, names='Attrition', color='Attrition', 
            color_discrete_map={0:'Green', 1:'Red'}, 
            title='Travel Type Affecting Attrition',
            facet_col='Business Travel'
)
fig.update_traces(marker=dict(line=dict(color='white', width=3)))
st.plotly_chart(fig)



# -------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    if st.runtime.exists():
        pass
    else:
        sys.argv = ['streamlit', 'run', sys.argv[0]]
        sys.exit(stcli.main())


