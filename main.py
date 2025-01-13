import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta as td
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

st.sidebar.header('Filtros')

# filtros de visualizações
locks_list = st.sidebar.multiselect('Escolha as ações para visualizar',data.columns)
if locks_list:
    data = data[locks_list]
    if len(locks_list) == 1:
        unique_lock = locks_list[0]
        data = data.rename(columns={unique_lock: 'Close'})

st.write('''
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações da IBOVESPA.

''')

date_initial = data.index.min().to_pydatetime()
date_final = data.index.max().to_pydatetime()
days = 1
interval_date =  st.sidebar.slider('Escolha um período',
                                   min_value=date_initial, max_value=date_final,
                                   value=(date_initial, date_final),
                                   step=td(days=days))
data = data.loc[interval_date[0]:interval_date[1]]

st.line_chart(data=data)