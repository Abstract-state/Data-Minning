import requests
import pandas as pd
import time

def fetch_gecko_price_data(cryptos):
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        'vs_currency': 'usd',
        'ids': ','.join(cryptos),  
        'order': 'market_cap_desc',
        'per_page': len(cryptos),
        'page': 1,
        'sparkline': False
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        crypto_data_list = []

        for coin_data in data:
            crypto_data_list.append({
                'id': coin_data.get('id'),
                'symbol': coin_data.get('symbol'),
                'name': coin_data.get('name'),
                'current_price': coin_data.get('current_price'),
                'market_cap': coin_data.get('market_cap'),
                'market_cap_rank': coin_data.get('market_cap_rank'),
                'fully_diluted_valuation': coin_data.get('fully_diluted_valuation'),
                'total_volume': coin_data.get('total_volume'),
                'high_24h': coin_data.get('high_24h'),
                'low_24h': coin_data.get('low_24h'),
                'price_change_24h': coin_data.get('price_change_24h'),
                'price_change_percentage_24h': coin_data.get('price_change_percentage_24h'),
                'market_cap_change_24h': coin_data.get('market_cap_change_24h'),
                'market_cap_change_percentage_24h': coin_data.get('market_cap_change_percentage_24h'),
                'circulating_supply': coin_data.get('circulating_supply'),
                'total_supply': coin_data.get('total_supply'),
                'max_supply': coin_data.get('max_supply'),
                'ath': coin_data.get('ath'),
                'ath_change_percentage': coin_data.get('ath_change_percentage'),
                'atl': coin_data.get('atl'),
                'atl_change_percentage': coin_data.get('atl_change_percentage'),
                'last_updated': coin_data.get('last_updated')
            })
        
        return pd.DataFrame(crypto_data_list)
    
    except Exception as e:
        print(f"Error fetching data from CoinGecko: {e}")
        return None

def main():

    cryptos = ['bitcoin', 'ethereum', 'solana', 'dogecoin', 'cardano']

    df = fetch_gecko_price_data(cryptos)
    
    if df is not None:
        print(df)
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    main()
