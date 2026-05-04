import requests
import json

def get_bitcoin_price():
    """Fetches the current Bitcoin price from CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        data = response.json()
        price = data['bitcoin']['usd']
        return price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None

# Get and display the current price
current_price = get_bitcoin_price()
if current_price:
    print(f"Current Bitcoin Price: ${current_price:,.2f} USD")
else:
    print("Could not retrieve Bitcoin price.")
