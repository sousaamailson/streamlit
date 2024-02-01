import streamlit as st
import plotly as px
import pandas as pd

# Criando dados de exemplo
dados = pd.DataFrame({
    'X': [1, 2, 3, 4, 5],
    'Y': [10, 11, 12, 13, 14]
})

# Título do aplicativo
st.title('Exemplo de Gráfico com Streamlit')

# Criando um gráfico de dispersão com Plotly Express
fig = px.scatter(dados, x='X', y='Y', title='Gráfico de Dispersão')

# Exibindo o gráfico no Streamlit
st.plotly_chart(fig)
