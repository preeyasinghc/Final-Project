import pandas as pd
pd.DataFrame.iteritems = pd.DataFrame.items
import numpy as np
#import plotly.express as px
import streamlit as st
#from streamlit_extras.add_vertical_space import add_vertical_space
import matplotlib.pyplot as plt
from datetime import datetime

# Displaying an image from a URL
image_url = "https://www.pinterest.co.uk/pin/454933999876263451/visual-search/?x=16&y=16&w=414&h=302&cropSource=6&surfaceType=flashlight"
#image_url = "https://static.appflow.ai/images/blog/ee40aedc-4b8a-4bd2-8af5-58f5e2cf3395.png" 
#st.image(image_url, caption="Customer App Subscription", use_column_width=True)


#st.title('Customer App Subscription Prediction Model')

# Load the CSV file
file_path = "output.csv"
final_results_df = pd.read_csv('output.csv')

# Streamlit App
st.title("Enrollment Prediction Results")

# Dropdown for 'enrolled' column
#selected_enrolled = st.selectbox("Select 'enrolled' value:", final_results_df['enrolled'].unique())
# Use st.sidebar for the sidebar elements
with st.sidebar:
    selected_enrolled = st.selectbox("Select 'enrolled' value:", final_results_df['enrolled'].unique())
# Filter DataFrame based on selected 'enrolled' value
filtered_results_enrolled = final_results_df[final_results_df['enrolled'] == selected_enrolled]

# Display the filtered DataFrames
st.write("### Results for Selected 'enrolled' Value:")
st.dataframe(filtered_results_enrolled)

# Count the occurrences of each value in 'enrolled'
st.title("Enrolled Count")
enrolled_counts = final_results_df['enrolled'].value_counts()

# Streamlit bar chart
st.bar_chart(enrolled_counts)


# Count the occurrences of each value in 'predicted_results'
st.title("Predicted Count")
predicted_counts = final_results_df['predicted_results'].value_counts()

# Check if there are any cases where no one has been predicted
#if 0 in predicted_counts.index:
    #st.write("There are cases where no one has been predicted.")
#else:
   # st.write("Everyone has been predicted.")

# Display the counts for each predicted value
with st.sidebar:
    st.title("Predicted Count")
    st.write("Counts for each predicted value:")
    st.write(predicted_counts)

# Plot a bar chart for the counts
st.bar_chart(predicted_counts)

#Downloading the dataframe into csv
@st.cache_data
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(final_results_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='final_results_df.csv',
    mime='text/csv',
)

# Display current date and time in Streamlit app
with st.sidebar:
    current_datetime = datetime.now()
    st.write("Current Date and Time:", current_datetime)