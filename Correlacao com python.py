import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr

X = np.array([10, 15, 17, 5, 20]) # Tempo de estudo\
Y = np.array([70,75,76,50,90]) #Nota

corr, _ = pearsonr(X, Y)

plt.figure(figsize = (10, 8), dpi = 80)
plt.plot(X, Y, 'o')
plt.title('Estudo Vs Nota')
plt.xlabel('Tempo de estudo (X)')
plt.ylabel('Nota (Y)')
plt.show()

print(f'Coeficiente de Pearson = {corr}')