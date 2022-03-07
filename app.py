import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import altair as alt


st.title("Lab 3- CSE 5544")
st.header("Cara Nix")

st.header("Step 1: Choose Dataset")

st.write("The dataset I chose to use was the Gender Inequality Indicators dataset. This dataset spans 1960-2017 and tracks fertility rate, literacy, employment and ownership of businesses, and wages to study the extent of gender equality around the world. I chose to consdier the data from the year 2012 specifically. [Datasource](https://github.com/ZeningQu/World-Bank-Data-by-Indicators/tree/master/gender) for gender data. ")

df_data = pd.read_csv("https://raw.githubusercontent.com/ZeningQu/World-Bank-Data-by-Indicators/master/gender/gender.csv")

cols_to_keep= ['Country Name', 'Country Code', 'Year','average_value_Life expectancy at birth, female (years)',
       'average_value_Life expectancy at birth, male (years)','average_value_Mortality rate, adult, female (per 1,000 female adults)',
       'average_value_Mortality rate, adult, male (per 1,000 male adults)']

df_data_short= df_data[cols_to_keep]

#something weird happening here

gender_2012 = df_data_short[df_data_short["Year"] == 2012]

st.write("See below for the dataset I used, including the four variables which I created: diff_M-F_Life_expectancy, diff_M-F_Mortality_rate, diff_F-M_Life_expectancy, and diff_F-M_Mortality_rate")

st.write("Where negative (positive) values for diff_M-F_Life_expectancy indicate women have higher (lower) life expectancy at birth than men do and negative (positive) values for diff_M-F_Mortality_rate indicate more women (men) died than men (women) that year and vice versa for diff_F-M_Life_expectancy and diff_F-M_Mortality_rate") 

gender_2012["diff_M-F_Life_expectancy"] = pd.to_numeric(gender_2012["average_value_Life expectancy at birth, male (years)"]) -  pd.to_numeric(gender_2012["average_value_Life expectancy at birth, female (years)"])
gender_2012["diff_M-F_Mortality_rate"] = pd.to_numeric(gender_2012["average_value_Mortality rate, adult, male (per 1,000 male adults)"]) -  pd.to_numeric(gender_2012['average_value_Mortality rate, adult, female (per 1,000 female adults)'])

gender_2012["diff_F-M_Life_expectancy"] = pd.to_numeric(pd.to_numeric(gender_2012["average_value_Life expectancy at birth, female (years)"]- (gender_2012["average_value_Life expectancy at birth, male (years)"])))
gender_2012["diff_F-M_Mortality_rate"] = pd.to_numeric(pd.to_numeric(gender_2012['average_value_Mortality rate, adult, female (per 1,000 female adults)']- gender_2012["average_value_Mortality rate, adult, male (per 1,000 male adults)"]))


gender_2012

st.header("Step 2: Visualizations")


st.subheader("Vizualization From Perspective 1: Greyscale Heatmap")

heatmap2= alt.Chart(gender_2012).mark_bar().encode(
    alt.X('diff_M-F_Mortality_rate:Q', bin=alt.BinParams(maxbins=30), title="Difference in Mortality Rate, M-F"),
    alt.Y('diff_F-M_Life_expectancy:Q', bin=alt.BinParams(maxbins=30), title="Difference in Life Expectancy, F-M"),
    alt.Color('count()', scale=alt.Scale(scheme='greys'))
).properties(title='Heat Map of Mortality Rate and Life Expectancy (2012)', width=700, height = 700)

points2 = alt.Chart(gender_2012).mark_circle(
    color='black',
    size=5,
).encode(
    x='diff_M-F_Mortality_rate:Q',
    y='diff_F-M_Life_expectancy:Q',
)

#heatmap2 + points2

st.altair_chart(heatmap2+points2, use_container_width = True)

st.markdown("<p style='text-align: center;'>Figure 1: Figure which displays a heatmap of the realtionship between mortality rate and life expectancy; each point corresponds to a country. Positive values indicate better conditions for women on both axes. Data from the World Bank, 2012. </p>", unsafe_allow_html=True)

st.subheader("Vizualization From Perspective 2: Rainbow Heatmap")
heatmap= alt.Chart(gender_2012).mark_bar().encode(
    alt.X('diff_M-F_Mortality_rate:Q', bin=alt.BinParams(maxbins=80), title="Difference in Mortality Rate, M-F"),
    alt.Y('diff_M-F_Life_expectancy:Q', bin=alt.BinParams(maxbins=80), title="Difference in Life Expectancy, M-F"),
    alt.Color('count()', scale=alt.Scale(scheme='rainbow'))
).properties(title='Heat Map of Mortality Rate and Life Expectancy', width=700, height = 700)


points = alt.Chart(gender_2012).mark_circle(
    color='black',
    size=5,
).encode(
    x='diff_M-F_Mortality_rate:Q',
    y='diff_M-F_Life_expectancy:Q',
)

#heatmap + points


st.altair_chart(heatmap+ points + points.transform_regression('diff_M-F_Mortality_rate', 'diff_M-F_Life_expectancy').mark_line(color='yellow'))

st.markdown("<p style='text-align: center;'>Figure 2: Figure which displays a heatmap of the realtionship between mortality rate and life expectancy; each point corresponds to a country. Axes correspond to the difference between values for men and women. </p>", unsafe_allow_html=True)



st.subheader("Vizualization From Perspective 3: Inferno Heatmap")

heatmap2= alt.Chart(gender_2012).mark_bar().encode(
    alt.X('diff_M-F_Mortality_rate:Q', bin=alt.BinParams(maxbins=30), title="Difference in Mortality Rate, M-F"),
    alt.Y('diff_F-M_Life_expectancy:Q', bin=alt.BinParams(maxbins=30), title="Difference in Life Expectancy, F-M"),
    alt.Color('count()', scale=alt.Scale(scheme='inferno'))
).properties(title='Heat Map of Mortality Rate and Life Expectancy (2012)', width=700, height = 700)

points2 = alt.Chart(gender_2012).mark_circle(
    color='black',
    size=5,
).encode(
    x='diff_M-F_Mortality_rate:Q',
    y='diff_F-M_Life_expectancy:Q',
)

#heatmap2 + points2

st.altair_chart(heatmap2+points2, use_container_width = True)

st.markdown("<p style='text-align: center;'>Figure 3: Figure which displays a heatmap of the realtionship between mortality rate and life expectancy; each point corresponds to a country. Positive values indicate better conditions for women on both axes. Data from the World Bank, 2012. </p>", unsafe_allow_html=True)



st.subheader("Discussion")
st.write("Visualization from perspective 1 is better than the visualization from perspective 2. First, the greyscale heat map is much easier to interpret than the rainbow heat map. Rainbow colors are inherently unordered and work best for categorical data, rather than quantitative data, which is what we are working with here. It is much easier to interpret that the darker the color (black) the more observations than it is to first check the color mapping and realize that green was assigned to be the color for the highest concentration of points.")
st.write("Second, the axes labels on the perspective 2 visualization are misleading in the sense they make the chart more difficult to interpret. You’ll note that the x-axis label is Difference in Mortality Rate, M-F and the y-axis label is Difference in Life Expectancy, M-F. Which, at first glance seems okay as they are both M-F. However, how we think about life expectancy and mortality are different. Here’s what I mean: on the x axis, positive values indicate that more men died than women in 2012 (which implies a better quality of life for women) and on the y-axis positive values indicate that men had a higher life expectancy than women (indicating worse quality of life for women). Therefore, the visualization from perspective 1, where the axes do have differing M-F is more clearly interpretable in the sense that large positive values on both axes mean good things for women, and large negative values on both indicate things are worse off for women.  So, as the data is primarily in the bottom left corner for visualization 1 we can easily determine that in most countries women have a shorter life expectancy and a higher mortality rate.") 
st.write("Third, note that the visualization from perspective 2 has an added yellow regression line which is completely unnecessary- it’s chart junk used to distract. Fourth, due to the binning used in the perspective two visualization the figure looks more cluttered and messy than it does in the perspective 1 visualization where data points share boxes, rather than having almost every data point have it’s own box. Lastly, one should note the year is missing from the title in the perspective 2 visualization, so it does not indicate when this relationship occurred temporally. ")

st.write("Visualization from perspective 1 is better than the visualization from perspective 3. I'd argue the greyscale color map is more interpretable than the inferno colormap, as the greyscale color map goes from light to dark (where dark indicates a higher quantity), whereas the inferno color map goes from dark to light (where dark indicates a lower quantity). However, I do think that the inferno colormap is better than the rainbow colormap, as the colors in the inferno colormap are perceptually uniform and do have some sense of dark to light.")
