import streamlit as st
import pandas as pd
import yfinance as yf

NAME_STOCK = 'ITUB4.SA'
locks = ['ITUB4.SA','PETR4.SA','MGLU3.SA','VALE3.SA','ABEV3.SA','GGBR4.SA']

@st.cache_data
def loading_data(enterprises):
    text_tickers = ' '.join(enterprises)
    data_stock = yf.Tickers(text_tickers)
    stock_prices = data_stock.history(period='1d', start='2010-01-01', end='2024-12-30')
    stock_prices = stock_prices['Close']
    return stock_prices

data = loading_data(locks)


# filtros de visualizações
locks_list = st.multiselect('Escolha as ações para visualizar',data.columns)
if locks_list:
    data = data[locks_list]
    if len(locks_list) == 1:
        unique_lock = locks_list[0]
        data = data.rename(columns={unique_lock: 'Close'})

st.write('''
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações da IBOVESPA.

''')

st.line_chart(data=data)