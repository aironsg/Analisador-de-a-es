import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import timedelta as td, datetime


DATE_INITIAL_HISTORY = '2022-01-01'
DATE_FINAL_HISTORY = datetime.now()
@st.cache_data
def loading_data(enterprises):
    text_tickers = ' '.join(enterprises)
    data_stock = yf.Tickers(text_tickers)
    stock_prices = data_stock.history(period='1d', start=DATE_INITIAL_HISTORY, end= DATE_FINAL_HISTORY)
    stock_prices = stock_prices['Close']
    return stock_prices

@st.cache_data
def loading_tickers_locks():
    base_tickers = pd.read_csv('IBOV.csv',sep=';')
    tickers = list(base_tickers['Código'])
    tickers = [item + '.SA' for item in tickers]
    return tickers
    
    
    
stocks = loading_tickers_locks()
data_stocks = loading_data(stocks)

st.sidebar.header('Filtros')

# filtros de visualizações
stocks_list = st.sidebar.multiselect('Escolha as ações para visualizar',data_stocks.columns)
if stocks_list:
    data_stocks = data_stocks[stocks_list]
    if len(stocks_list) == 1:
        unique_stock = stocks_list[0]
        data_stocks = data_stocks.rename(columns={unique_stock: 'Close'})

st.write('''
# App Preço de Ações
O gráfico abaixo representa a evolução do preço das ações da IBOVESPA.

''')

date_initial = data_stocks.index.min().to_pydatetime()
date_final = data_stocks.index.max().to_pydatetime()
days = 1
interval_date =  st.sidebar.slider('Escolha um período',
                                   min_value=date_initial, max_value=date_final,
                                   value=(date_initial, date_final),
                                   step=td(days=days))
data_stocks = data_stocks.loc[interval_date[0]:interval_date[1]]

# Cria o grafico de linha
st.line_chart(data=data_stocks)

text_stock = ''

if len(stocks_list) == 0:
    stocks_list = list(data_stocks.columns)
elif len(stocks_list) == 1:
    data_stocks = data_stocks.rename(columns={'Close': unique_stock})    
    
asset_portfolio = [1000 for stock in stocks_list]
total_initial_asset_portfolio = sum(asset_portfolio)

for i, stock in enumerate(stocks_list):
    asset_performance = (data_stocks[stock].iloc[-1] / data_stocks[stock].iloc[0]) - 1
    asset_performance = float(asset_performance)
    
    asset_portfolio[i] = asset_portfolio[i] * (1 + asset_performance)
    
    if asset_performance > 0:
            text_stock = text_stock + f'  \n{stock}: :green[{asset_performance:.1%}]'
    elif asset_performance < 0:
        text_stock = text_stock + f'  \n{stock}: :red[{asset_performance:.1%}]'
    else:
        text_stock = text_stock + f'  \n{stock}: {asset_performance:.1%}'
    
total_final_asset_portfolio = sum(asset_portfolio)
asset_performance = total_final_asset_portfolio / total_initial_asset_portfolio - 1

if asset_performance > 0:
            text_asset_performance = f'Performance da carteira com todos os ativos: :green[{asset_performance:.1%}]'
elif asset_performance < 0:
        text_asset_performance = f'Performance da carteira com todos os ativos: :red[{asset_performance:.1%}]'
else:
        text_asset_performance = f'Performance da carteira com todos os ativos: {asset_performance:.1%}'

st.write(f'''
### Perfomace dos Ativos
Essa foi a perfomance de cada ativo no período selecionado:

{text_stock}


{text_asset_performance}
''')