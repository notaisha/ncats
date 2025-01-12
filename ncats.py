import streamlit as st
import pandas as pd
import os
import pathlib
import plotly.express as px
import io
from scipy.stats import zscore




"### Hello, Alec! <3 :bee:"

online = st.toggle("Robot run", value=False)

if online:

    file = st.file_uploader("Upload the CSV file that has the mandatory columns [Read] and [Compound], and an optional [Cell line] column. The headers must be exact:")
    row_skip_count = 6
    if not file:
        st.stop()
    df = pd.read_csv(file, index_col=0)
    df
    dict = df.to_dict()
else:
    row_skip_count = 7

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
        title = stat_file.name.replace(".stat1","").replace(".statAll", "")
    
    df_stat = pd.read_csv(stat_file,delimiter='\t', skiprows=row_skip_count, nrows=32, index_col=0)

    neg_mean = df_stat["1"].mean()
    neg_sd = df_stat["1"].std()
    neg_thresh = neg_mean + (3*neg_sd)
    
    pos_mean = df_stat["2"].mean()
    pos_sd = df_stat["2"].std()
    pos_thresh = pos_mean - (3*pos_sd)

    s = pos_thresh - neg_thresh
    r = abs(neg_mean-pos_mean)
    z = s/r
    
    if show_table:
        st.write(title)
        df_stat
        df_values = df_stat.values
 
    img = px.imshow(df_stat)
    img.update_layout(title_text=f"{title}   |   Z-factor = {round(z,2)}")
    st.plotly_chart(img,use_container_width=True)
  



