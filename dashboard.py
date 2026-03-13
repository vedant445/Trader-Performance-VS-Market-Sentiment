import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("processed_trader_sentiment_data.csv")

st.title("Trader Behavior vs Market Sentiment Dashboard")

st.subheader("Dataset Preview")
st.write(data.head())

st.subheader("PnL by Market Sentiment")

pnl_sentiment = data.groupby('classification')['daily_pnl'].mean()

fig, ax = plt.subplots()

pnl_sentiment.plot(kind='bar', ax=ax)

st.pyplot(fig)

st.subheader("Trade Activity by Sentiment")

activity = data.groupby('classification')['num_traders'].mean()

fig2, ax2 = plt.subplots()

activity.plot(kind='bar', ax=ax2)

st.pyplot(fig2)