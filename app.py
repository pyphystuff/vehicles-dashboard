import pandas as pd
import plotly.express as px
import streamlit as st

# lendo os dados
car_data = pd.read_csv('vehicles_us.csv')

# cabeçalho principal
st.header('Análise de anúncios de venda de carros')
st.write(
    'Este aplicativo permite explorar interativamente o conjunto de dados '
    'de anúncios de venda de carros nos EUA.'
)

# caixa de seleção para o histograma
build_histogram = st.checkbox('Criar histograma')

if build_histogram:
    st.write('Criando um histograma para o odômetro dos veículos')
    fig_hist = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig_hist, use_container_width=True)

# caixa de seleção para o gráfico de dispersão
build_scatter = st.checkbox('Criar gráfico de dispersão')

if build_scatter:
    st.write('Criando um gráfico de dispersão entre preço e odômetro')
    fig_scatter = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig_scatter, use_container_width=True)
