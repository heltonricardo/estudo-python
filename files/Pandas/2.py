import            pandas as pd
import             numpy as np
import matplotlib.pyplot as plt

notas = pd.Series([2, 7, 5, 10, 7], index=['E', 'D', 'C', 'B', 'A'])
notas = notas ** 2
print(notas)
print()
print(np.log(notas))
