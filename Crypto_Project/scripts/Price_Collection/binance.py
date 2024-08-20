import requests
import pandas as pd
import time

def fetch_binance_price(symbol):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}USDT"
    try:
        response = requests.get(url)
        data = response.json()
        return {
            'symbol': symbol,
            'price': data['price'],
            'timestamp': pd.Timestamp.now()
        }
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def main():
    cryptos = ['BTC', 'ETH', 'SOL', 'DOGE', 'ADA']
    data_list = []

    while len(data_list) < 100:
        for crypto in cryptos:
            data = fetch_binance_price(crypto)
            if data:
                data_list.append(data)
                print(f"Collected data: {data}")

                df = pd.DataFrame(data_list)
                df.to_csv(r'D:\SEM-7\DataMinning\Theory_DA\Crypto_Project\data\Frequent_Data\binance_prices.csv', index=False)

        time.sleep(5)
    
    print("Collected 100 records. Stopping the script.")

if __name__ == "__main__":
    main()
