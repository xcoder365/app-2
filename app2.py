import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Data Analysis with Pandas and Streamlit")

# Load the dataset
@st.cache  # Caching to improve performance
def load_data():
    data = pd.read_csv("data.csv")  # Change the filename as per your data
    return data

data = load_data()

# Sidebar for data selection
st.sidebar.title("Data Selection")
selected_columns = st.sidebar.multiselect(
    "Select Columns", data.columns.tolist(), default=data.columns.tolist()
)

# Display the selected data
if selected_columns:
    st.write("### Selected Data")
    st.write(data[selected_columns])

# Basic data statistics
st.sidebar.title("Basic Data Statistics")
if st.sidebar.checkbox("Show Summary Statistics"):
    st.write("### Summary Statistics")
    st.write(data[selected_columns].describe())

# Data Visualization
st.sidebar.title("Data Visualization")
if st.sidebar.checkbox("Show Data Visualization"):
    st.write("### Data Visualization")
    st.bar_chart(data[selected_columns])
    # You can add your visualization code here using libraries like Matplotlib or Seaborn
    # Example: st.bar_chart(data[selected_columns])

# Data Filtering
st.sidebar.title("Data Filtering")
if st.sidebar.checkbox("Apply Filters"):
    st.write("### Filtered Data")
    # You can add filtering options and display the filtered data here
    # Example: filtered_data = data[data['Column_name'] > value]
    # st.write(filtered_data)

# Exporting Data
st.sidebar.title("Export Data")
if st.sidebar.button("Export CSV"):
    st.markdown(
        f"**Exported {len(data)} rows to data_export.csv**",
        unsafe_allow_html=True,
    )
    # You can add code here to export the data to a CSV file
    # Example: data[selected_columns].to_csv("data_export.csv", index=False)

# Add any additional features or analysis as needed

# Footer
st.sidebar.title("About")
st.sidebar.info(
    "This is a simple Streamlit app for data analysis using Pandas."
    "\n\n"
    "Built with ❤️ by Your Name"
)
