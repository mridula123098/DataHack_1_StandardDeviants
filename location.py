import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Sample dataset (replace this with your actual dataset)

df=pd.read_csv("Location.csv")

# Create a DataFrame
df = pd.DataFrame(df)

unique_locations = df['Location'].unique()

# Streamlit app
st.title("Scatter Plot of Location vs. Valuation in 2023")

# Create a scatter plot for each unique location
fig, ax = plt.subplots()
for location in unique_locations:
    location_data = df[df['Location'] == location]
    ax.scatter(location_data['Location'], location_data['Valuation ($B) 2023'], marker='o', label=location)

ax.set_xlabel('Location')
ax.set_ylabel('Valuation ($B) 2023')
ax.set_title('Scatter Plot of Location vs. Valuation in 2023')
ax.set_xticklabels(unique_locations, rotation=45)  # Rotate x-axis labels for readability
ax.grid(True)

# Display the scatter plot using Streamlit
st.pyplot(fig)





