import streamlit as st
import folium
from streamlit_folium import folium_static

# Title
st.title("Map with Marker")

# Input fields for longitude and latitude
longitude = st.number_input("Enter longitude:", format="%.6f")
latitude = st.number_input("Enter latitude:", format="%.6f")

# Create map
if longitude and latitude:
    # Create a map centered at the specified location
    m = folium.Map(location=[latitude, longitude], zoom_start=12)

    # Add a marker to the map
    folium.Marker([latitude, longitude], tooltip="Selected Location").add_to(m)

    # Display the map
    folium_static(m)
else:
    st.write("Please enter valid longitude and latitude.")