import yfinance as yf

def get_price(ticker):
    asset = yf.Ticker(ticker)
    price = asset.history(period="1d")['Close'].iloc[-1]
    return round(price, 2)


symbol = "BTC-USD"
print(f"The current price of {symbol} is ${get_price(symbol)}")
