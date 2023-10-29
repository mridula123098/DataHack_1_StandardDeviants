import streamlit as st
import pandas as pd
import plotly.express as px

# Load your dataset
# Replace 'your_data.csv' with the actual path to your dataset
data = pd.read_csv('your_data.csv')

# Convert 'total funding amount' to float
data['Total Funding Amount'] = data['Total Funding Amount'].str.replace(',', '', regex=True).astype(float)

# Title of the Streamlit app
st.title('Indian Startup Ecosystem Analysis')

# Sidebar filters
st.sidebar.header('Filters')
location_filter = st.sidebar.multiselect('Select Location', data['Headquarters Location'].unique())
funding_range = st.sidebar.slider('Select Funding Range', min_value=0.0, max_value=float(data['Total Funding Amount'].max()), step=100000.0, value=(0.0, float(data['Total Funding Amount'].max())))

# Create a button to apply filters
if st.sidebar.button("Apply Filter"):
    # Filter data based on user's selections
    filtered_data = data[(data['Headquarters Location'].isin(location_filter)) & (data['Total Funding Amount'] >= funding_range[0]) & (data['Total Funding Amount'] <= funding_range[1])]

    # Display filtered data as a table
    st.write('Filtered Data:')
    st.write(filtered_data)

    # Create interactive graphs
    st.header('Interactive Graphs')

    # Plot the total funding amount distribution
    fig = px.histogram(filtered_data, x='Total Funding Amount', title='Total Funding Amount Distribution')
    st.plotly_chart(fig)

    # Plot a bar chart of the top startups
    top_startups = filtered_data.nlargest(10, 'Total Funding Amount')
    fig2 = px.bar(top_startups, x='Organization Name', y='Total Funding Amount', title='Top 10 Startups by Funding')
    st.plotly_chart(fig2)

   

# Display a footer with data source and references
st.sidebar.markdown('Data Source: [Your Source]')
st.sidebar.markdown('References: [Your References]')

# Add any additional information, insights, or recommendations as needed
