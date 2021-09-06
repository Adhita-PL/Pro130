import pandas as pd

df = pd.read_csv('final.csv')
print(df.shape)

del df['Luminosity'] 
print(df.shape)

df.to_csv('main.csv') 