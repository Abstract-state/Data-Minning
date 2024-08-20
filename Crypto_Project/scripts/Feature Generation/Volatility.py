import pandas as pd

# Step 1: Define the file paths for each cryptocurrency final data file
crypto_files = {
    'BTC': '../data/BTC_final_data.csv',
    'ETH': '../data/ETH_final_data.csv',
    'SOL': '../data/SOL_final_data.csv',
    'DOGE': '../data/DOGE_final_data.csv',
    'ADA': '../data/ADA_final_data.csv'
}

# Step 2: Calculate Rolling Volatility for Each Cryptocurrency
for crypto, file_path in crypto_files.items():
    # Load the dataset for the current cryptocurrency
    data = pd.read_csv(file_path, parse_dates=['timestamp'])
    
    # Calculate the daily percentage change in closing prices
    data['pct_change'] = data['close'].pct_change() * 100
    
    # Calculate the rolling volatility (standard deviation) over a 20-day window
    data['volatility'] = data['pct_change'].rolling(window=20).std()
    
    # Save the updated dataset back to the same CSV file
    data.to_csv(file_path, index=False)
    
    print(f"Calculated volatility for {crypto} and saved to {file_path}.")
