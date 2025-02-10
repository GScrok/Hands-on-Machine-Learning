import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression


df = pd.read_csv('pizzas.csv')

modelo = LinearRegression()
x = df[['diametro']]
y = df[['preco']]

modelo.fit(x, y)

st.title('Prevendo o preço da pizza')
st.divider()

diamtetro = st.number_input('Digite o tamanho do diametro da pizza: ', min_value=10, max_value=100)

if diamtetro:
    preco_previsto = modelo.predict([[diamtetro]])[0][0]
    st.write(f'O preço previsto da pizza é R$ {preco_previsto:.2f}')
    st.balloons()