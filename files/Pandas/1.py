import            pandas as pd
import             numpy as np
import matplotlib.pyplot as plt

notas = pd.Series([2, 7, 5, 10, 7], index=['a', 'b', 'c', 'd', 'e'])
print(notas)
print()
print(notas.values)
print()
print(notas.index)
print()
print(notas['a'])
print('Média:', notas.mean())
print('Desvio padrão:', notas.std())
print()
print(notas.describe())
