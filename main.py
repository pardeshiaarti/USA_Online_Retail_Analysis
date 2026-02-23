import streamlit as st
from USA_Online_Store_Transaction_Analysis import run_analysis

st.set_page_config(page_title="USA Online Retail Analysis", layout="wide")

st.title("📊 USA Online Retail Analysis Dashboard")

st.markdown("Click below to run the analysis.")

if st.button("Run Analysis"):
    run_analysis()
