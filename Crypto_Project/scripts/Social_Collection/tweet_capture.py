import tweepy
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

crypto_keywords = [
    'Bitcoin', 'BTC', 'Ethereum', 'ETH', 'Solana', 'SOL', 'Dogecoin', 'DOGE', 'Cardano', 'ADA',
    'cryptocurrency', 'crypto', 'blockchain', 'digital currency', 'altcoin', 'stablecoin', 
    'Binance Coin', 'BNB', 'Polkadot', 'DOT', 'Ripple', 'XRP', 'Litecoin', 'LTC',]

def extract_tweets(keyword, max_tweets=100):
    tweets = []
    
    try:
        for tweet in tweepy.Cursor(api.search_tweets, q=keyword, lang="en", tweet_mode='extended').items(max_tweets):
            tweets.append({
                'tweet_id': tweet.id_str,
                'created_at': tweet.created_at,
                'user': tweet.user.screen_name,
                'text': tweet.full_text,
                'likes': tweet.favorite_count,
                'retweets': tweet.retweet_count
            })
        
        df = pd.DataFrame(tweets)

        df.to_csv(f'D:/SEM-7/DataMinning/Theroy_DA/Crypto_Project/data/{keyword}_tweets.csv', index=False)
        print(f"Extracted {len(df)} tweets for {keyword} and saved to CSV.")
    
    except Exception as e:
        print(f"Error fetching tweets for {keyword}: {e}")

for keyword in crypto_keywords:
    extract_tweets(keyword, max_tweets=100)
