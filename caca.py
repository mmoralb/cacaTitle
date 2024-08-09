import random as rd

m = 4
n = 4
M = []
for fila in range(m):
    fila = []
    for c in range(n):
        fila.append(rd.randint(0, 9))