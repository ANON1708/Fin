### README.md for Stock Sentiment Analysis

---

# Stock Sentiment Analysis

## Overview
The **Stock Sentiment Analysis** tool allows users to analyze the sentiment of recent news headlines related to specified stock tickers. It fetches up-to-date news, performs sentiment analysis (positive, neutral, or negative), aggregates the results, and provides actionable insights.

---

## Features
- **User Input**: Accepts stock tickers as a comma-separated list.
- **News Fetching**: Fetches up to 10 recent headlines for each ticker using the [NewsAPI](https://newsapi.org/).
- **Sentiment Analysis**: Classifies each headline as positive, neutral, or negative using `TextBlob`.
- **Aggregated Sentiment**:
  - Calculates sentiment percentages (e.g., 60% Positive, 30% Neutral).
  - Provides an overall sentiment summary (e.g., "Mostly Positive").
- **Actionable Insights**: Displays headline-level sentiment analysis along with distribution.

## Improvements added

- 1. **Stock Price Trend Analysis** 
Fetches recent stock price data using the Alpha Vantage API.
Calculates the percentage change in stock price over the last two trading days.
Integrates price trend analysis into the insights provided for each stock.

- 2. **Stock Recommendation System**
Combines sentiment analysis and price trends to generate actionable recommendations:
Buy: Positive sentiment with a recent price dip.
Hold: Positive sentiment with stable or increasing price.
Monitor: Neutral sentiment with no strong signals.
Sell: Negative sentiment detected.
Helps users make informed investment decisions quickly.
---

## Prerequisites
1. **Python**:
   - Ensure Python 3.7 or above is installed on your system.
2. **API Key**:
   - Register on [NewsAPI](https://newsapi.org/) to obtain a free API key.
3. **Dependencies**:
   - Install required Python libraries:
     ```bash
     pip install requests textblob
     ```

## Product Documentation

### Purpose
The tool helps investors gauge public sentiment around specific stocks using recent news, aiding in making data-driven decisions.

### Use Cases
1. **Investors**: Quickly understand sentiment trends for potential investments.
2. **Portfolio Managers**: Monitor sentiment for stocks in a portfolio.
3. **Analysts**: Use headline sentiment to assess market sentiment.

### Technical Details
- **Sentiment Analysis**:
  - `TextBlob` calculates sentiment polarity:
    - Positive (>0), Neutral (0), Negative (<0).
-Calculates price trend over last 2 days
-Calculates recommendations such as:
Buy: Positive sentiment with a recent price dip.
Hold: Positive sentiment with stable or increasing price.
Monitor: Neutral sentiment with no strong signals.
Sell: Negative sentiment detected.

- **API Integration**:
  - Uses `requests` to fetch JSON data from NewsAPI and Alpha Vantage
- **Data Processing**:
  - Aggregates sentiment and calculates percentages using Python’s `Counter`.

### Limitations
- **API Dependency**: Relies on NewsAPI for headlines.
- **TextBlob**: Sentiment classification may not account for nuances.


## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

--- 

Feel free to copy this `README.md` into your repository! Let me know if you'd like to include any additional details or features. 🚀
