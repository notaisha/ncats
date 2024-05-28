import streamlit as st
import pandas as pd
import os
import pathlib
import plotly.express as px

"### Hello, Alec! <3 :bee:"

'''
- do you want the names actually changed for each file? or do you just want the results or whatever calsulation we come up with to be clear?
- would you rather type a path to all your documents? or drag and drop?
- will your csv always be a csv, and will it always have the same headers?
- will the csv and the stat files always be saved within the same structure of folders? (this doesn't matter if you prefer to drag and drop and don't want names changed)
- will the stat files always start the same way, with 6 lines to be ignored
'''

file = st.file_uploader("upload file here")
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

stat_file_name_dict = {}
for stat_file in stat_files:
    for read in df.index:
        if read in stat_file.name:
            stat_file.name, read
            stat_file_name_dict[stat_file.name]=[read, dict["Compound"][read],dict["Cell line"][read]]
            df_stat = pd.read_csv(stat_file,delimiter='\t', skiprows=6, nrows=32, index_col=0)
            df_stat
            fig = px.imshow(df_stat)
            fig.show()


stat_file_name_dict
"now"