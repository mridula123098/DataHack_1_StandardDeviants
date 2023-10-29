import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
import seaborn as sns

st.markdown("""
<style>
.st-emotion-cache-6q9sum.ef3psqc4  
{
    visibility:hidden;
}
.st-emotion-cache-1wbqy5l.e17vllj40 ,.st-emotion-cache-z3au9t.ea3mdgi2, .st-emotion-cache-cio0dv.ea3mdgi1
{
    visibility:hidden;
}
</style>
""", unsafe_allow_html=True)

df = pd.read_csv('EV Dataset.csv')
ev_startups = df[df['Organization Name'].str.contains('', case=False)]

ev_startups = df[df['Organization Name'].str.contains('', case=False)]
st.title('Analysis of Electric Vehicle Startups')
st.write(f"Number of Electric Vehicle Startups from 2018 to 2022: {len(ev_startups)}")

st.subheader('Electric Vehicle Startups Details')
st.dataframe(ev_startups)

st.subheader('Geographic Distribution of EV Startups')
fig, ax = plt.subplots(figsize=(10, 6))
ev_startups['Headquarters Location'].value_counts().plot(kind='bar', ax=ax)
ax.set_ylabel('Number of Startups')
ax.set_xlabel('Location')
ax.set_title('Geographic Distribution of EV Startups')
plt.xticks(rotation=45, ha='right')
st.pyplot(fig)

st.subheader('Funding Trends Over Time (Boxplot)')
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Founded Date', y='Total Funding Amount', data=ev_startups, ax=ax)
ax.set_ylabel('Total Funding Amount')
ax.set_xlabel('Year')
ax.set_title('Funding Trends Over Time')
st.pyplot(fig)

st.subheader('Scatter Plot: Funding Amount vs. Number of Funding Rounds')
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='Number of Funding', y='Total Funding Amount', data=ev_startups, ax=ax)
ax.set_xlabel('Number of Funding Rounds')
ax.set_ylabel('Total Funding Amount')
ax.set_title('Scatter Plot: Funding Amount vs. Number of Funding Rounds')
st.pyplot(fig)

