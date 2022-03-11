import streamlit as st
import yfinance as finance


import streamlit as st
import yfinance as finance


def get_ticker(name):
	company = finance.Ticker(name) # google
	return company


# Project Details
st.title("Stock Market Prediction App Using Streamlit")
st.header("A Data Science Web Application")
st.sidebar.header(" Created By: \n  Mohd Aqdas \n \n Saurabh Kumar Mishra")

company1 = get_ticker("GOOGL")
company2 = get_ticker("MSFT")
company3 = get_ticker("ORCL")
company4 = get_ticker("TTM")

# fetches the data: Open, Close, High, Low and Volume
google = finance.download("GOOGL", start="2020-01-01", end="2021-12-01")
microsoft = finance.download("MSFT", start="2020-01-01", end="2021-12-01")
Oracle = finance.download("ORCL", start="2021-01-01", end="2021-12-01")
Tata  = finance.download("TTM", start="2020-01-01", end="2021-12-01")

# Valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
data1 = company1.history(period="6mo")
data2 = company2.history(period="6mo")
data3 = company3.history(period="6mo")
data4 = company4.history(period="6mo")

# markdown syntax
st.write("""
### Google
""")

# detailed summary on Google
st.write(company1.info['longBusinessSummary'], "\n", google)
st.write(google)

# plots the graph
st.line_chart(data1.values)

st.write("""
### Microsoft
""")
st.write(company2.info['longBusinessSummary'], "\n", microsoft)
st.line_chart(data2.values)

st.write("""
### ORACLE 
""")
st.write(company3.info['longBusinessSummary'], "\n", Oracle)
st.line_chart(data3.values)

st.write("""
### Tata Motors 
""")
st.write(company3.info['longBusinessSummary'], "\n", Tata )
st.line_chart(data4.values)

