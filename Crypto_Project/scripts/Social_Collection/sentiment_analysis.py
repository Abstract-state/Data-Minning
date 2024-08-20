import pandas as pd
import numpy as np
import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = TFBertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=3) 

def preprocess_texts(texts, max_len=128):
    encodings = tokenizer(texts, truncation=True, padding=True, max_length=max_len, return_tensors='tf')
    return encodings

def predict_sentiment(texts):
    encodings = preprocess_texts(texts)
    outputs = model(encodings['input_ids'], attention_mask=encodings['attention_mask'], training=False)
    predictions = tf.nn.softmax(outputs.logits, axis=-1)
    sentiment_scores = np.argmax(predictions, axis=1)
    return sentiment_scores

df = pd.read_csv(r'D:\SEM-7\DataMinning\Theory_DA\Crypto_Project\data\Social_Data\Tweet_Data.csv')

split_dfs = np.array_split(df, 10)

df['Sentiment'] = 0

for i, part_df in enumerate(split_dfs):
    print(f"Processing part {i + 1}/10...")
    
    tweets = part_df['cleanText'].astype(str).tolist()

    sentiments = predict_sentiment(tweets)

    df.loc[part_df.index, 'Sentiment'] = sentiments

df.to_csv('path_to_tweet_data_with_sentiment.csv', index=False)
