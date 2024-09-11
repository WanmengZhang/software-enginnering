import requests
import json
import streamlit as st
import matplotlib.pyplot as plt

# Make a GET request to the weather API
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')
result_dict = json.loads(result.text)  # Parse the JSON string into a dict object

# Extract temperature data
locations = [data["place"] for data in result_dict["temperature"]["data"]]
temperatures = [data["value"] for data in result_dict["temperature"]["data"]]

# Streamlit app
st.title("Hong Kong Weather Data~")

# Sidebar for location selection
selected_location = st.sidebar.selectbox("Select a location", locations)

# Display temperature for selected location
if selected_location:
    selected_temp = next(data["value"] for data in result_dict["temperature"]["data"] if data["place"] == selected_location)
    st.write(f"Temperature at {selected_location}: {selected_temp}°C")

# Bar chart for all locations
fig, ax = plt.subplots()
ax.barh(locations, temperatures)
ax.set_xlabel('Temperature (°C)')
ax.set_title('Temperature of All Locations')

st.pyplot(fig)