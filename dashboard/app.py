import streamlit as st
from streamlit_searchbox import st_searchbox
from dashboard.queries import company_check
from data_ingestion.fetch_data import fetch_financial_data
from data_ingestion.clean_data import clean_stock
from data_ingestion.load_data import load_financial_data

st.title("📈 Financial Dashboard")

symbol = st.text_input("Enter a company ticker:", "AAPL")

if st.button("Search"):
    if company_check(symbol):
        
        st.success(f"✅ Found {symbol} in database.")
    else:
        st.warning(f"⚠️ {symbol} not found, fetching from API...")
        raw = fetch_financial_data(symbol)
        cleaned = clean_stock(raw)
        load_financial_data(cleaned, symbol)
        st.success(f"📥 Data for {symbol} saved to database.")

    # Always query locally (fast!)
    df = company_check(symbol)
    st.line_chart(df.set_index("date")[["revenue", "profit", "stock_price"]])
    st.dataframe(df.tail(10))
