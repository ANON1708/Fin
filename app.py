from flask import Flask, render_template, request, jsonify
import requests
from textblob import TextBlob
import os

app = Flask(__name__)

# API Keys
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "fcda71eae5464edaa75e8b5839ac30c")
ALPHA_VANTAGE_KEY = os.getenv("ALPHA_VANTAGE_KEY", "BUK7BJUVY8JMOOZI")


# Fetch Stock News
def fetch_news_headlines(ticker):
    url = f"https://newsapi.org/v2/everything?q={ticker}&apiKey={NEWS_API_KEY}"
    response = requests.get(url)
    data = response.json()
    return [article["title"] for article in data.get("articles", [])[:5]]


# Sentiment Analysis
def analyze_sentiment(headlines):
    sentiments = [
        TextBlob(headline).sentiment.polarity for headline in headlines
    ]
    avg_sentiment = sum(sentiments) / len(sentiments) if sentiments else 0
    if avg_sentiment > 0: return "Positive"
    elif avg_sentiment < 0: return "Negative"
    return "Neutral"


# Fetch Stock Price Change
def fetch_stock_price_change(ticker):
    url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={ALPHA_VANTAGE_KEY}"
    response = requests.get(url).json()
    time_series = response.get("Time Series (Daily)", {})
    dates = sorted(time_series.keys(), reverse=True)

    if len(dates) < 2:
        return "Price data unavailable"

    latest_close = float(time_series[dates[0]]["4. close"])
    previous_close = float(time_series[dates[1]]["4. close"])
    return f"{((latest_close - previous_close) / previous_close) * 100:.2f}%"


# Home Page
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ticker = request.form.get("ticker").upper()
        if ticker:
            headlines = fetch_news_headlines(ticker)
            sentiment = analyze_sentiment(headlines)
            price_change = fetch_stock_price_change(ticker)

            return render_template("index.html",
                                   ticker=ticker,
                                   headlines=headlines,
                                   sentiment=sentiment,
                                   price_change=price_change)
    return render_template("index.html", ticker=None)


# Run Flask App
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
