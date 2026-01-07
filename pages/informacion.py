import yfinance as yf
import pandas as pd
import streamlit as st

ticker=yf.Ticker("BTC-USD")
# Capitalización de mercado
cap=ticker.info['marketCap']
# Volumen 24h
volumen=ticker.info["volume24Hr"]

#Cargamos los datos
precios=ticker.history(period='5y')['Close']
#Ajustamos el indice
precios=precios.sort_index(ascending=False).reset_index()
# Precio actual
pr_actual=precios['Close'].iloc[0]
# Rentabilidad 1 mes (30 días)
r30=(precios['Close'].iloc[0]-precios['Close'].iloc[30])/precios['Close'].iloc[30]*100
# Rentabilidad 1 año (360 días)
r360=(precios['Close'].iloc[0]-precios['Close'].iloc[360])/precios['Close'].iloc[360]*100
# Rentabilidad 5 años (1800 días)
r1800=(precios['Close'].iloc[0]-precios['Close'].iloc[1800])/precios['Close'].iloc[1800]*100

#Mostramos los resultados
st.write(f'Precio actual {pr_actual}')
st.write(f'Capitalización de mercado {cap}')
st.write(f'Volumen 24h {volumen}')
st.write(f'Rentabilidad a 1 mes (30 días) {r30}')
st.write(f'Rentabilidad a 1 año (360 días) {r360}')
st.write(f'Rentabilidad a 5 años (1800 días) {r1800}')