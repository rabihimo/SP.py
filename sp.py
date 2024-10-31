import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Define the top 5 S&P 500 companies
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA']

# Download historical data
data = yf.download(tickers, period="5y")  # Adjust the period as needed

# Extract adjusted closing prices
adj_close = data['Adj Close']

# Plot the adjusted closing prices
plt.figure(figsize=(14, 7))
for ticker in tickers:
    plt.plot(adj_close.index, adj_close[ticker], label=ticker)

plt.xlabel('Date')
plt.ylabel('Adjusted Closing Price')
plt.title('Adjusted Closing Price of Top 5 S&P 500 Companies')
plt.legend()
plt.grid(True)
plt.show()
