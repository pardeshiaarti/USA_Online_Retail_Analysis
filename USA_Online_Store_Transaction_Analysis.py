import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.linear_model import LinearRegression


def run_analysis():

    st.subheader("Dataset Loading")

    df = pd.read_csv("dataset.csv")

    st.write("Dataset Preview:")
    st.dataframe(df.head())

    # -----------------------------
    # Date Conversion (if exists)
    # -----------------------------
    if "Transaction_date" in df.columns:
        df["Transaction_date"] = pd.to_datetime(df["Transaction_date"])

        monthly_sales = (
            df.resample("M", on="Transaction_date")["Amount_spent"]
            .sum()
        )

        st.subheader("📈 Monthly Sales Trend")
        st.line_chart(monthly_sales)

    # -----------------------------
    # Fill Missing Segment
    # -----------------------------
    if "Segment" in df.columns:
        df["Segment"].fillna(df["Segment"].mode()[0], inplace=True)

    # -----------------------------
    # KMeans Clustering
    # -----------------------------
    if "Amount_spent" in df.columns:

        X = df[["Amount_spent"]]

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        kmeans = KMeans(n_clusters=3, random_state=42)
        df["Cluster"] = kmeans.fit_predict(X_scaled)

        st.subheader("📊 Cluster Distribution")
        st.bar_chart(df["Cluster"].value_counts())

    st.success("Analysis Completed Successfully!")
