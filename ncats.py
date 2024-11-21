import streamlit as st
import pandas as pd
import os
import pathlib
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

"### Hello, Alec! <3 :bee:"

online = st.toggle("Robot run", value=True)

if online:

    file = st.file_uploader("Upload the CSV file that has the mandatory columns [Read] and [Compound], and an optional [Cell line] column. The headers must be exact:")
    if not file:
        st.stop()
    df = pd.read_csv(file, index_col=0)
    df

    dict = df.to_dict()

#fig = make_subplots(rows=1, cols=1)

stat_files = st.file_uploader("Drag all stat files here", accept_multiple_files=True)
if not stat_files:
    st.stop()


show_table = st.checkbox("Show table")
stat_file_name_dict = {}

for stat_file in stat_files:
    if online:
        for read in df.index:
            if read in stat_file.name:
                try:
                    stat_file_name_dict[stat_file.name]=[read, dict["Compound"][read],dict["Cell line"][read]]
                except KeyError:
                    stat_file_name_dict[stat_file.name]=[read, dict["Compound"][read]]
                title = '\t'.join(stat_file_name_dict[stat_file.name])
    else:
        title = stat_file.name.replace(".stat1","")
    
    df_stat = pd.read_csv(stat_file,delimiter='\t', skiprows=6, nrows=32, index_col=0)
    if show_table:
        st.write(title)
        df_stat
        df_values = df_stat.values
 

    img = px.imshow(df_stat)
    img.update_layout(title_text=title)
    st.plotly_chart(img)
            #fig = go.Figure(data=img.data, layout=fig.layout)
            #st.plotly_chart(fig)


            #img = sn.heatmap(df_stat)
            #img


#stat_file_name_dict
#"now"