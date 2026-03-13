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

### Timestamp Conversion

```python
sentiment['timestamp'] = pd.to_datetime(sentiment['timestamp'])
trades['Timestamp'] = pd.to_datetime(trades['Timestamp'])
