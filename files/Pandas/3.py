import            pandas as pd
import             numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({'Aluno'  :    ['W', 'A', 'H', 'J', 'C'],
                   'Faltas' :    [ 3 ,  4 ,  2 ,  1 ,  4 ],
                   'Prova'  :    [ 2 ,  7 ,  5 , 10 ,  6 ],
                   'Seminário' : [8.5, 7.5, 9.0, 7.5, 8.0]})
print(df)
print()
print(df.dtypes)
print()
print(df.columns)
print()
print(df['Prova'])
print()
print(df.describe())
print()
print(df.sort_values(by='Seminário'))
print()
print(df.loc[2])
print()
print(df[df['Seminário'] > 8.0])
print()
print(df[(df['Seminário'] > 8.0) & (df['Prova'] > 3)])
