import streamlit as st
import pandas as pd
import os
import pathlib
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

"### Hello, Alec! <3 :bee:"

offline = st.toggle("Offline")

file = st.file_uploader("Upload the CSV file that has the columns [Compound] and [Cell line], the headers must be exact:")
if not file:
    st.stop()
df = pd.read_csv(file, index_col=0)
df

dict = df.to_dict()
#dict
#st.write(dict["Compound"]["T5747796"])

fig = make_subplots(rows=1, cols=2)

stat_files = st.file_uploader("drag all stat files here", accept_multiple_files=True)
if not stat_files:
    st.stop()
show_table = st.checkbox("Show table")
stat_file_name_dict = {}
for stat_file in stat_files:
    for read in df.index:
        if read in stat_file.name:
            stat_file_name_dict[stat_file.name]=[read, dict["Compound"][read],dict["Cell line"][read]]
            title = '\t'.join(stat_file_name_dict[stat_file.name])
            st.write(title)
            df_stat = pd.read_csv(stat_file,delimiter='\t', skiprows=6, nrows=32, index_col=0)
            if show_table:
                df_stat
                df_values = df_stat.values
 

            img = px.imshow(df_stat)
            img.update_layout(title_text=title)
            st.plotly_chart(img)
            fig = go.Figure(data=img.data, layout=fig.layout)
            st.plotly_chart(fig)


            #img = sn.heatmap(df_stat)
            #img


#stat_file_name_dict
#"now"