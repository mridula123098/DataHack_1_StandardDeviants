import streamlit as st
import pandas as pd
import altair as alt


# Select the relevant columns for the chart
df=pd.read_csv("100Startups.csv")
data_chart = df[['Company', 'Valuation ($B) 2018', 'Valuation ($B) 2019', 'Valuation ($B) 2020','Valuation ($B) 2021','Valuation ($B) 2022']].sort_values("Valuation ($B) 2022",ascending=False).head(20)

# Reshape the data from wide to long format
data_long = data_chart.melt(id_vars=['Company'], var_name='Year', value_name='Valuation')

# Create an Altair multi-series line chart
brush=alt.selection_interval()
alt.renderers.enable('default')
chart = alt.Chart(data_long).mark_line().encode(
    x='Company:N',
    y='Valuation:Q',
    color='Year:N',
    tooltip=['Company', 'Year', 'Valuation']
)
chart
# # Define a variable to hold the selected company
# selected_company = None

# # Create a selection based on clicking a line in the chart
# selection = alt.selection_single(on='click', nearest=True, empty=False)
# chart = chart.add_selection(selection)

# # Create a condition to filter the data for the selected company

# condition = alt.Chart(data_long).transform_filter(selection)

# # Display the selected company's details
# selected_company = st.text("")

# # Create a separate graph for the selected company
# if selected_company is not None:
#     details = df[df['Company'] == selected_company]
#     st.subheader(f"Graph for {selected_company}")
#     chart_for_selected_company = alt.Chart(details).mark_line().encode(
#         x='Year:N',
#         y=alt.Y('Valuation ($B):Q', title="Valuation ($B)"),
#         tooltip=['Year', alt.Tooltip('Valuation ($B)', title="Valuation ($B)")]
#     ).properties(
#         width=600,
#         height=300
#     )
#     st.altair_chart(chart_for_selected_company)
