import pandas as pd

df = pd.read_csv('tourism_dataset_5000.csv')

print(df.head())

print(df.info())

print(df.describe())

print(df['Site Name'])

