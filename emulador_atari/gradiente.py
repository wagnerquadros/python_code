from matplotlib import pyplot as plt #Plotar graficos
import pandas as pd # Manipular os dados - riar os data frames
import pylab as pl
import numpy as np
import requests
import csv

url ='https://raw.githubusercontent.com/diogocortiz/Crash-Course-IA/master/RegressaoLinear/FuelConsumptionCo2.csv'
response = requests.get(url)
for row in csv_reader:
    print(row)
# Cria um dataset chamado 'df' que receberá os dados do csv
df = pd.read_csv("FuelConsumptionCo2.csv")

#EXIBE A ESTRUTURA DO DATAFRAME
print(df.head())