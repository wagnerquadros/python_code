import matplotlib.pyplot as plt
import pandas as pd # Manipular os dados - riar os data frames


df = pd.read_csv("variaveis.csv")
print(df.head())
print(df.describe())

df.plot.scatter(x='brain_weight', y='body_weight', title='Relação entre Brain Weight e Body Weight')

plt.show()