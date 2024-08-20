import pandas as pd

final_data = pd.read_csv(r'D:\SEM-7\DataMinning\Theory_DA\Crypto_Project\data\final_centralized_data.csv', parse_dates=['timestamp'])

crypto_names = final_data['crypto'].unique()

for crypto_name in crypto_names:
    crypto_data = final_data[final_data['crypto'] == crypto_name]

    output_path = f'D:\SEM-7\DataMinning\Theory_DA\Crypto_Project\data\\final\{crypto_name}_final_data.csv'
    crypto_data.to_csv(output_path, index=False)
    
    print(f"Saved {crypto_name} final data to {output_path}.")