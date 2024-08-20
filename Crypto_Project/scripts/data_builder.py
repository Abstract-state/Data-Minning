import pandas as pd
from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata

crypto_files = {
    'BTC': 'D:\SEM-7\DataMinning\Theory_DA\Crypto_Project\data\Price_Data\BTC-USD.csv',
    'ETH': 'D:\SEM-7\DataMinning\Theory_DA\Crypto_Project\data\Price_Data\ETH-USD.csv',
    'SOL': 'D:\SEM-7\DataMinning\Theory_DA\Crypto_Project\data\Price_Data\SOL-USD.csv',
    'DOGE': 'D:\SEM-7\DataMinning\Theory_DA\Crypto_Project\data\Price_Data\DOGE-USD.csv',
    'ADA': 'D:\SEM-7\DataMinning\Theory_DA\Crypto_Project\data\Price_Data\ADA-USD.csv'
}

centralized_data = pd.DataFrame()

for crypto, file_path in crypto_files.items():
    crypto_data = pd.read_csv(file_path, parse_dates=['timestamp'])
    crypto_data['crypto'] = crypto
    centralized_data = pd.concat([centralized_data, crypto_data])

sample_sentiment_data = pd.DataFrame({
    'very_poor': [3, 2, 5, 4, 3, 4, 2, 5, 3, 4],
    'poor': [15, 12, 17, 14, 16, 14, 13, 15, 17, 14],
    'neutral': [60, 55, 58, 62, 57, 61, 59, 58, 60, 63],
    'good': [18, 22, 15, 17, 20, 18, 21, 17, 16, 19],
    'excellent': [4, 9, 5, 3, 4, 3, 5, 5, 4, 4]
})

metadata = SingleTableMetadata()
metadata.detect_from_dataframe(sample_sentiment_data)

synthesizer = GaussianCopulaSynthesizer(metadata)
synthesizer.fit(sample_sentiment_data)

synthetic_sentiment_data = synthesizer.sample(len(centralized_data))
synthetic_sentiment_data = synthetic_sentiment_data.round(0).astype(int)

final_data = pd.concat([centralized_data.reset_index(drop=True), synthetic_sentiment_data.reset_index(drop=True)], axis=1)

final_data.to_csv(r'D:\SEM-7\DataMinning\Theory_DA\Crypto_Project\data\final_centralized_data.csv', index=False)
