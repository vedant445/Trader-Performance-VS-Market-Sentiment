# Trader Performance vs Market Sentiment Analysis

## Overview
This project analyzes how **Bitcoin market sentiment (Fear/Greed Index)** relates to **trader behavior and performance** using historical trading data from Hyperliquid.

The objective is to explore whether trader activity and profitability vary depending on the overall market sentiment and to extract insights that could inform better trading strategies.

---

# Datasets

## 1. Bitcoin Market Sentiment Dataset
Daily sentiment classification of the Bitcoin market.

Columns:
- `timestamp`
- `value`
- `classification` (Fear / Extreme Fear / Greed / Extreme Greed / Neutral)
- `date`

Example:

| timestamp | value | classification | date |
|----------|------|---------------|------|
|1517463000|30|Fear|2018-02-01|
|1517549400|15|Extreme Fear|2018-02-02|

---

## 2. Historical Trader Data (Hyperliquid)

Contains trading activity from traders on the Hyperliquid platform.

Key columns:

- `Account`
- `Coin`
- `Execution Price`
- `Size Tokens`
- `Size USD`
- `Side`
- `Timestamp IST`
- `Closed PnL`
- `Fee`
- `Trade ID`

Dataset size:

| Dataset | Rows | Columns |
|-------|------|------|
|Sentiment Data|2644|4|
|Trader Data|211,224|16|

---

# Data Preparation

The first step in the analysis was to clean and prepare the datasets so they could be used together for analysis.

The Bitcoin Fear & Greed dataset contains sentiment values recorded over time, while the trader dataset contains individual trade records. Since the goal of this project was to analyze trader performance relative to market sentiment, both datasets needed to be aligned by **date**.

The timestamp columns in both datasets were converted into a standard datetime format. After conversion, the **date component** was extracted from the timestamps so that trading activity could be aggregated at the **daily level**.

The trader dataset contains individual trade executions. To make the analysis meaningful, the data was aggregated per **trader per day**. This aggregation allowed us to analyze how traders performed and behaved on each trading day.

---

# Feature Engineering

Several key metrics were created from the raw trading data to capture trader behavior and performance.

### Daily Profit and Loss (PnL)

The **Closed PnL** column represents the profit or loss from each trade.  
To measure trader performance, the total PnL for each trader was calculated on a **daily basis**. This metric represents the net profitability of a trader for a given day.

---

### Number of Trades

To measure trader activity, the number of trades executed by each trader per day was calculated.  
This metric helps identify how active a trader is during different market conditions.

---

### Average Trade Size

The **Size USD** column indicates the dollar value of each trade.  
For each trader and day, the average trade size was computed. This metric helps identify whether traders are taking **larger or smaller positions** under different sentiment conditions.

---

### Win Rate

A new metric called **win rate** was created to measure trading success.

A trade was considered a **win** if its Closed PnL was greater than zero.  
The win rate was then calculated as the percentage of profitable trades for each trader per day.

This metric helps evaluate the consistency of trader performance.

---

# Dataset Merging

After computing all trader-level metrics, they were combined into a single dataset containing:

- Daily PnL
- Number of trades
- Average trade size
- Win rate

This dataset was then merged with the **market sentiment dataset** using the date column.  

This merge allowed each trading day to be associated with the corresponding **Fear & Greed sentiment classification**.

The resulting dataset contains both **trader behavior metrics and market sentiment**, enabling comparative analysis.

---

# Exploratory Data Analysis

Several analyses were performed to understand the relationship between trader performance and market sentiment.

---

# 1. Trader Performance vs Market Sentiment

The first analysis examined whether trader profitability changes under different sentiment conditions.

Average daily PnL was calculated for each sentiment category:

- Extreme Fear
- Fear
- Neutral
- Greed
- Extreme Greed

This analysis helps determine whether traders perform better during **fear-driven markets or greed-driven markets**.

---

# 2. Trading Activity vs Market Sentiment

The next analysis focused on trader behavior rather than profitability.

The average number of trades executed under each sentiment category was calculated.  
This helps reveal whether traders become more active during certain market conditions.

For example, traders may increase activity during high volatility periods such as **Extreme Fear or Extreme Greed**.

---

# 3. Position Size vs Market Sentiment

The third analysis examined whether traders adjust their **position sizes** depending on market sentiment.

The average trade size in USD was compared across sentiment categories.

This helps determine whether traders take **larger risks during bullish markets** or reduce exposure during fearful markets.

---

# Trader Segmentation

To better understand different trading behaviors, traders were segmented into groups based on their activity and position sizes.

---

## Frequent vs Infrequent Traders

Traders were categorized based on their trading frequency.  

Those executing more trades than the median were labeled as **Frequent Traders**, while those below the median were labeled as **Not Frequent Traders**.

This segmentation helps determine whether highly active traders perform differently compared to less active traders.

---

## High Volume vs Low Volume Traders

Traders were also segmented based on their average trade size.

Traders whose average trade size was greater than the dataset median were classified as **High Volume Traders**, while others were classified as **Low Volume Traders**.

This analysis helps identify whether larger position sizes are associated with higher profitability or higher risk.

---

# Predictive Model

To further explore the relationship between trader behavior and profitability, a simple machine learning model was built.

A **Random Forest Classifier** was trained to predict whether a trader would be **profitable or not profitable**.

The model used the following features:

- Market sentiment score
- Number of trades executed
- Average trade size
- Win rate

The target variable was **profitability**, derived from whether daily PnL was positive or negative.

After training and testing the model, it achieved **very high prediction accuracy** on the dataset.

This suggests that trader behavior metrics combined with market sentiment contain strong signals about profitability.

---

# Trader Clustering

In addition to prediction, clustering was performed to identify different **trader behavior archetypes**.

The clustering algorithm grouped traders using behavioral features such as:

- Sentiment score
- Trade frequency
- Position size
- Win rate

A **K-Means clustering algorithm** was used to identify three distinct trader groups.

These clusters represent different types of traders, such as:

- High activity traders
- Large position traders
- More conservative traders

Visualizing these clusters helps understand how different trader types behave in the market.

---

# Output Dataset

The final processed dataset containing trader metrics and sentiment information was saved as:
processed_trader_sentiment_data.csv


This dataset can be used for further analysis, machine learning, or dashboard visualization.

---

# Tools and Libraries Used

The project was implemented using the following Python libraries:

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

These libraries were used for data processing, visualization, machine learning, and dashboard development.

---

# Author

Vedant Maladkar  
Data Science / Analytics Intern Assignment
