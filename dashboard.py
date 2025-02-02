import streamlit as st
from analyzer import FinancialDataAnalyzer
import pandas as pd
from dotenv import load_dotenv
load_dotenv()
# Hardcoded list of stocks
stocks = ["AAPL", "TSLA", "META"]

# Time span options
time_spans = ["3 Months", "5 Months"]

# Streamlit UI for user input
st.title("Financial Data Analyzer")
st.markdown("### Select a Stock and Time Span to Analyze Data")

# Create form with selectbox for stock symbol and time span
with st.form(key="stock_form"):
    # Select stock symbol from the list
    stock_symbol = st.selectbox("Select a Stock Symbol", stocks)
    
    # Select time span
    time_span = st.selectbox("Select Time Span", time_spans)

    # Submit button
    submit_button = st.form_submit_button(label="Analyze Data")

# If submit button is pressed, display the results
if submit_button:
    

    # Create FinancialDataAnalyzer instance and get results
    if stock_symbol == "AAPL":
        file_path = 'first_50_data_AAPL.csv'
    elif stock_symbol == "TSLA":
        file_path = 'first_50_data_TSLA.csv'
    elif stock_symbol == "META":
        file_path = 'first_50_data_FB.csv'
    time_span_1 = 3 if time_span == "3 Months" else 5
    # Initialize the analyzer
    st.subheader(f"stock: {stock_symbol}")
    st.subheader(f"Time Span: {time_span}")
    st.write("ANALYZING DATA...")
    analyzer = FinancialDataAnalyzer(file_path, stock_symbol,time_span_1)
    result = analyzer.analyze_data()
    st.write(result.raw)
    