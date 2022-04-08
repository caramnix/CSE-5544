


# Application for CSE 5544 Final Project 

import pandas as pd 
import numpy as np 
import altair as alt 
import streamlit as st 
from datetime import datetime
from vega_datasets import data

st.set_page_config(
    layout= "wide"
)


df_data = pd.read_csv("https://raw.githubusercontent.com/caramnix/CSE-5544/main/Final%20Project/data_geospatial.csv")
df_data['Year'] = df_data['Year'].astype(int)

#df_data

from datetime import time

gun_panel = st.container() 
with gun_panel:
    columns= st.columns([3, .2, 2, 5])
    with columns[0]: 
        start_time= st.slider("Select Range of Years:",
                1996, 2021, (2000, 2021))
        min_year = start_time[0]
        max_year = start_time[1]
        current_data= df_data.loc[df_data['Year'] >= min_year] 
        current_data= df_data.loc[df_data['Year'] <= max_year] 
     

    chart1, chart2 = st.columns([3,2])

    airports = data.airports.url
    states = alt.topo_feature(data.us_10m.url, feature='states')

    with chart1: 
        background = alt.Chart(states).mark_geoshape(
        fill='lightgray',
        stroke='white'
        #).properties(
        #width=500,
        #height=300
        ).project('albersUsa')

        base = alt.Chart(current_data).encode(
            longitude='longitude:Q',
            latitude='latitude:Q'
        )
        points = base.mark_circle(opacity=0.3).encode(
            color=alt.value('red'),
            size=alt.Size('Number of Victims:Q', title='Number of Victims'),
            tooltip=['location:N', 'Full Date', 'Number of Victims']
        )
        st.altair_chart(background + points, use_container_width=True)

   # with chart2: dounut plots

   


gun_row2 = st.container()

with gun_row2:

    columns = st.columns([3, 1, .2, 2])
    with columns[1]: 
        timespan = columns[1].radio(
            'Display',
            ('Number of Victims', 'Number of Shootings')
            )

    with columns[0]:

        if timespan == 'Number of Victims':
            input= 'sum(Number of Victims)'
            t= "Number of Victims"
        else:
            input = 'sum(Shooting)' 
            t= "Number of Shootings"
            
        bar_graph= alt.Chart(df_data).mark_bar().encode(
            x='Year:O',
             y=alt.Y(input, title=t),
            tooltip=[alt.Tooltip(input, title= t)]
        ).configure_bar(
         opacity=.7,
        color='red'
        )
        st.altair_chart(bar_graph,  use_container_width=True)

   
    #with columns[3]:
        #bottom right viz


