import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de vehículos en venta en EE.UU.')

# Gráfico de barras sobre la condicion de los vehículos
st.subheader('Condición de los vehículos')
st.write('Distribución de los vehículos según su condición.')
bar_button = st.button('Construir gráfico de barras')
if bar_button:
    fig = px.bar(car_data['condition'].value_counts().reset_index(),
                 x='condition', y='count',
                 title='Condición de los vehículos',
                 labels={'condition': 'Condición', 'count': 'Cantidad'})
    st.plotly_chart(fig, use_container_width=True)

# Histograma sobre la distribucion de precios
st.subheader('Distribución de precios')
st.write('Distribución de los precios de los vehículos en venta.')
hist_button = st.button('Construir histograma')
if hist_button:
    fig = px.histogram(car_data, x='price', title='Distribución de precios',
                       labels={'price': 'Precio', 'count': 'Cantidad'})
    st.plotly_chart(fig, use_container_width=True)

# Scatter odometro en comparación con el precio
st.subheader('Relación entre precio y odómetro')
st.write('Cómo el millaje influye en el precio de venta.')
show_scatter = st.checkbox('Mostrar gráfico de dispersión')
if show_scatter:
    fig = px.scatter(car_data, x='odometer', y='price',
                     title='Precio vs Odómetro',
                     labels={'odometer': 'Odómetro (millas)', 'price': 'Precio'})
    st.plotly_chart(fig, use_container_width=True)