import pandas as pd

df = pd.read_csv('result.csv')
df_transposed = df.transpose()
df_transposed.to_csv('file_transposed.csv', index=False)