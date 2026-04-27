import streamlit as st
import folium
from streamlit_folium import st_folium

m = folium.Map(location=[51.05, 13.73], zoom_start=12)

folium.Marker(
    [51.05, 13.73],
    popup="Dresden"
).add_to(m)

st.title("Folium 地图")

st_folium(m, width=700, height=500)