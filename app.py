import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
df = pd.read_csv('cleaned_data.csv')

# Streamlit layout 
st.title("CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers")

# Add an interactive widget to filter by year range
year_range = st.slider("Select year range", 2019, 2022, (2020, 2021))
df_filtered = df[df['year'].between(year_range[0], year_range[1])]

# Display a sample of the filtered data
st.write(df_filtered[['title', 'year', 'journal']].head())

# Plot number of publications over time
papers_per_year = df_filtered['year'].value_counts().sort_index()
fig, ax = plt.subplots()
ax.bar(papers_per_year.index, papers_per_year.values)
ax.set_title('Publications by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Number of Publications')
st.pyplot(fig)

# Show top journals
top_journals = df_filtered['journal'].value_counts().head(10)
st.bar_chart(top_journals)
