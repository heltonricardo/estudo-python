import            pandas as pd
import             numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('base.csv')
print(df.head())
print()
print(df.head(n=8))
print()
print(df.tail())
