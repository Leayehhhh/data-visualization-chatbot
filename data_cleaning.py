import pandas as pd

raw_data = pd.read_csv('datasets/raw_data_five_second_test.csv')

processed_data = raw_data.dropna()
processed_data.columns = ['Category', 'Percentage']

processed_data.to_csv('datasets/cleaned_data.csv', index=False)
print("Data cleaning completed!")
