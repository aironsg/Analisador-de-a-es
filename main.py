import streamlit as st
import pandas as pd
import yfinance as yf

NAME_STOCK = 'ITUB4.SA'

@st.cache_data
def loading_data(enterprise):
    data_stock = yf.Ticker(enterprise)
    stock_prices = data_stock.history(period='1d', start='2010-01-01', end='2024-12-30')
    stock_prices = stock_prices[['Close']]
    return stock_prices

data = loading_data(NAME_STOCK)

st.write('''
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações do Itaú(ITUB4) ao longo dos anos.

''')

st.line_chart(data=data)