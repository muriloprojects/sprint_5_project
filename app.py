# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import plotly.express as px

# Lendo o conjunto de dados (certifique-se de que o arquivo CSV está no mesmo diretório)
car_data = pd.read_csv('vehicles_us.csv')

# Criando o cabeçalho do aplicativo
st.header('Análise de Vendas de Carros nos EUA')

# Criando um botão para gerar o histograma
hist_button = st.button('Criar histograma')

# Quando o botão for clicado
if hist_button:
    # Mensagem para o usuário
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # Criando o histograma
    fig = px.histogram(car_data, x="odometer", title="Distribuição da Quilometragem dos Veículos")

    # Exibindo o gráfico
    st.plotly_chart(fig, use_container_width=True)

# Você pode adicionar mais interatividade, por exemplo:
# Um segundo botão para criar outro gráfico
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão entre preço e quilometragem')
    fig2 = px.scatter(car_data, x="odometer", y="price", title="Relação entre Quilometragem e Preço")
    st.plotly_chart(fig2, use_container_width=True)

