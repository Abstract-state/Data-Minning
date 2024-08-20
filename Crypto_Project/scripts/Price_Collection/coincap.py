import requests
import pandas as pd
import time

def fetch_coincap_price(crypto):
    url = f"https://api.coincap.io/v2/assets/{crypto.lower()}"
    try:
        response = requests.get(url)
        data = response.json()
        return {
            'symbol': crypto.upper(),
            'price': data['data']['priceUsd'],
            'timestamp': pd.Timestamp.now()
        }
    except Exception as e:
        print(f"Error fetching data for {crypto}: {e}")
        return None

def main():
    cryptos = ['bitcoin', 'ethereum', 'solana', 'dogecoin', 'cardano']
    data_list = []

    while len(data_list) < 100:
        for crypto in cryptos:
            data = fetch_coincap_price(crypto)
            if data:
                data_list.append(data)
                print(f"Collected data: {data}")

                df = pd.DataFrame(data_list)
                df.to_csv(r'D:\SEM-7\DataMinning\Theory_DA\Crypto_Project\data\Frequent_Data\coincap_prices.csv', index=False)

        time.sleep(5)
    
    print("Collected 100 records. Stopping the script.")

if __name__ == "__main__":
    main()
