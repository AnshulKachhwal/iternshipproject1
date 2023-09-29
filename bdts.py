import streamlit as st
import pandas as pd
from streamlit_folium import folium_static
import folium

# Load data
hotels = pd.read_csv(r"C:\Users\Rahil Khan\OneDrive\Desktop\tourism data\Hotels.csv")
places = pd.read_csv(r"C:\Users\Rahil Khan\OneDrive\Desktop\tourism data\Places.csv")  # Replace "path_to_places.csv" with the actual file path

# Sidebar: User input
st.sidebar.header('User Input')
budget = st.sidebar.slider('Select your budget', min_value=0, max_value=5000, step=100, value=1000)

# Filter hotels based on budget
filtered_hotels = hotels[hotels['PRICE_RUPEES'] <= budget]

# Create a map centered around Jaipur for hotels
hotel_map = folium.Map(location=[26.9124, 75.7873], zoom_start=12, tiles='openstreetmap')

# Add hotel markers to the map
for lat, lon, name, price in zip(filtered_hotels['Lat'], filtered_hotels['Lng'], filtered_hotels['HOTEL'], filtered_hotels['PRICE_RUPEES']):
    folium.Marker([lat, lon], radius=10,
                  popup = (f'<strong>Hotel</strong>: {name}<br>'
                           f'<strong>Price</strong>: {price}<br>'),
                  icon=folium.Icon(color='red', icon='hotel', prefix='fa')).add_to(hotel_map)

# Create a map centered around Jaipur for places
places_map = folium.Map(location=[26.9124, 75.7873], zoom_start=12, tiles='openstreetmap')

# Add places markers to the map
for lat, lon, poi, in_time1, in_time2, out_time1, out_time2, price_ind, price_for in zip(places['LATITUDE'], places['LONGITUDE'], places['POIs'], places['IN-TIME1'], places['IN-TIME2'], places['OUT-TIME1'], places['OUT-TIME2'], places['PRICE (ind)'], places['PRICE(forigner)']):
    folium.Marker([lat, lon], radius=10,
                  popup = (f'<strong>Place</strong>: {poi}<br>'
                           f'<strong>In-Time 1</strong>: {in_time1}<br>'
                           f'<strong>In-Time 2</strong>: {in_time2}<br>'
                           f'<strong>Out-Time 1</strong>: {out_time1}<br>'
                           f'<strong>Out-Time 2</strong>: {out_time2}<br>'
                           f'<strong>Price (Ind)</strong>: {price_ind}<br>'
                           f'<strong>Price (Foreigner)</strong>: {price_for}<br>'),
                  icon=folium.Icon(color='blue', icon='info-sign')).add_to(places_map)

# Display the maps
st.header("Recommended Hotels and Places in Jaipur")
st.markdown("Here are some recommended hotels within your budget and places:")
st.markdown("Note: Prices are in Rupees.")

# Display the hotel map
st.subheader("Recommended Hotels")
folium_static(hotel_map)

# Display the places map
st.subheader("Places")
folium_static(places_map)

# Display the recommended hotels as a table
st.subheader("Recommended Hotels")
st.write(filtered_hotels[['HOTEL', 'PRICE_RUPEES']].reset_index(drop=True))

# Display the places as a table
st.subheader("Places")
st.write(places[['POIs', 'IN-TIME1', 'IN-TIME2', 'OUT-TIME1', 'OUT-TIME2', 'PRICE (ind)', 'PRICE(forigner)']].reset_index(drop=True))

# Additional information or instructions can be provided here.
