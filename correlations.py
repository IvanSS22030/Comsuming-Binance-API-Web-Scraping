import pandas as pd
import numpy as np

#We need to import the data from the csv files

sp500_df = pd.read_csv("sp500.csv").tail(30)
gold_df = pd.read_csv("Gold.csv").tail(30)

#columns to study
sp500_df = sp500_df[['Date', 'Close']]
gold_df = gold_df[['Date', 'Close']]

#Fusion in a dataframe
df = pd.merge(sp500_df, gold_df, on='Date', how='inner')

#correlation
correlation = np.corrcoef(df['Close_x'], df['Close_y'])[0,1]
print(correlation)


# asignar una puntuación basada en el nivel de correlación
if correlation > 0.8:
    score = 10
elif correlation > 0.78:
    score = 9
elif correlation > 0.4:
    score = 8
elif correlation > 0.2:
    score = 7
elif correlation > 0:
    score = 6
elif correlation > -0.2:
    score = 5
elif correlation > -0.4:
    score = 4
elif correlation > -0.6:
    score = 3
elif correlation > -0.8:
    score = 2
elif correlation > -1:
    score = 1
else:
    print("No hay correlación")
    score = 0



# imprimir la puntuación
print(f"La puntuación de correlación entre xrp y ada es: {score}")