import numpy as np
a = np.array([[1, 6],
              [2, 8],
              [3, 11], 
              [3, 10], 
              [1, 7]])
# print(a)
mean_a = np.mean(a, axis=0)
# print(mean_a)
a_centered = np.subtract(a, mean_a)
# print(a_centered)
b = a_centered[:, :1]
c = a_centered[:, 1:]
c = c.T
# print(b)
# print(c)
a_centered_sp = c.dot(b)
# print(a_centered_sp)
# print(a_centered_sp.sum())
akov = a_centered_sp.sum() / (len(a) - 1)
print(f'Acording the manual calculation the cov value is {akov}')
akovauto = np.cov(a.T)
akovauto = akovauto[0, 1]
print(f'According to the automatic calculation the cov value is: {akovauto}')
