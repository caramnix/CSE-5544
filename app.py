import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt

df_data = pd.read_csv("https://raw.githubusercontent.com/ZeningQu/World-Bank-Data-by-Indicators/master/gender/gender.csv")

cols_to_keep= ['Country Name', 'Country Code', 'Year','average_value_Life expectancy at birth, female (years)',
       'average_value_Life expectancy at birth, male (years)','average_value_Mortality rate, adult, female (per 1,000 female adults)',
       'average_value_Mortality rate, adult, male (per 1,000 male adults)']

df_data_short= df_data[cols_to_keep]

#something weird happening here

gender_2012 = df_data_short[df_data_short["Year"] == 2012]

gender_2012

gender_2012["diff_M-F_Life_expectancy"] = pd.to_numeric(gender_2012["average_value_Life expectancy at birth, male (years)"]) -  pd.to_numeric(gender_2012["average_value_Life expectancy at birth, female (years)"])
gender_2012["diff_M-F_Mortality_rate"] = pd.to_numeric(gender_2012["average_value_Mortality rate, adult, male (per 1,000 male adults)"]) -  pd.to_numeric(gender_2012['average_value_Mortality rate, adult, female (per 1,000 female adults)'])


heatmap= alt.Chart(gender_2012).mark_bar().encode(
    alt.X('diff_M-F_Mortality_rate:Q', bin=alt.BinParams(maxbins=30), title="Difference in Mortality Rate, M-F"),
    alt.Y('diff_M-F_Life_expectancy:Q', bin=alt.BinParams(maxbins=30), title="Difference in Life Expectancy, M-F"),
    alt.Color('count()', scale=alt.Scale(scheme='rainbow'))
).properties(title='Heat Map of Mortality Rate and Life Expectancy (2012)', width=700, height = 700)


points = alt.Chart(gender_2012).mark_circle(
    color='black',
    size=5,
).encode(
    x='diff_M-F_Mortality_rate:Q',
    y='diff_M-F_Life_expectancy:Q',
)

#heatmap + points


st.altair_chart(heatmap+points)

heatmap2= alt.Chart(gender_2012).mark_bar().encode(
    alt.X('diff_M-F_Mortality_rate:Q', bin=alt.BinParams(maxbins=30), title="Difference in Mortality Rate, M-F"),
    alt.Y('diff_M-F_Life_expectancy:Q', bin=alt.BinParams(maxbins=30), title="Difference in Life Expectancy, M-F"),
    alt.Color('count()', scale=alt.Scale(scheme='greys'))
).properties(title='Heat Map of Mortality Rate and Life Expectancy (2012)', width=700, height = 700)

points2 = alt.Chart(gender_2012).mark_circle(
    color='black',
    size=5,
).encode(
    x='diff_M-F_Mortality_rate:Q',
    y='diff_M-F_Life_expectancy:Q',
)

#heatmap2 + points2


st.altair_chart(heatmap2+points2, use_container_width = True)