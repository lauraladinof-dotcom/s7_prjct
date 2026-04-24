import pandas as pd
import plotly.express as px
import streamlit as st

# encabezado
st.header("Dashboard de anuncios de coches")

# leer datos
car_data = pd.read_csv("vehicles_us.csv")

# botón histograma
hist_button = st.button("Construir histograma")

if hist_button:
    st.write("Creación de un histograma para el odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# botón scatter
scatter_button = st.button("Construir gráfico de dispersión")

if scatter_button:
    st.write("Relación entre odómetro y precio")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
