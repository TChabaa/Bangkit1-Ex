import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Load datasets
day_df = pd.read_csv("../data/day.csv")
hour_df = pd.read_csv("../data/hour.csv")

datachange = [day_df, hour_df]

for column in datachange:
    column['dteday'] = pd.to_datetime(column['dteday'])

day_df.info()
print("Jumlah Duplikasi", day_df.duplicated().sum())

hour_df.info()
print("Jumlah Duplikasi", hour_df.duplicated().sum())

print(day_df.describe(include=[np.number]))
print(hour_df.describe(include=[np.number]))

# Scale the temperature
day_df['atemp_scaled'] = day_df['atemp'] * 50