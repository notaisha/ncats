import streamlit as st
import pandas as pd
import os
import pathlib
import plotly.express as px
import seaborn as sn

"### Hello, Alec! <3 :bee:"


file = st.file_uploader("Upload the CSV file that has the columns [Compound] and [Cell line], the headers must be exact:")
if not file:
    st.stop()
df = pd.read_csv(file, index_col=0)
df

dict = df.to_dict()
#dict
#st.write(dict["Compound"]["T5747796"])


stat_files = st.file_uploader("drag all stat files here", accept_multiple_files=True)
if not stat_files:
    st.stop()
show_table = st.checkbox("Show table")
stat_file_name_dict = {}
for stat_file in stat_files:
    for read in df.index:
        if read in stat_file.name:
            stat_file_name_dict[stat_file.name]=[read, dict["Compound"][read],dict["Cell line"][read]]
            st.write('\t'.join(stat_file_name_dict[stat_file.name]))
            df_stat = pd.read_csv(stat_file,delimiter='\t', skiprows=6, nrows=32, index_col=0)
            if show_table:
                df_stat
            fig = px.imshow(df_stat)
            #fig.show()
            st.plotly_chart(fig)
            img = sn.heatmap(df_stat)
            img


#stat_file_name_dict
#"now"