import numpy as np
import backtracking as bt
import matriz
import random

size = 8 # Size del puzle
size = size + 1

m = matriz.Construye_Matriz_Numerica(size)
m_size = m.shape[1]

array_muros = matriz.Construye_Arreglo_Muros_Interiores(m)

#print(array_muros)

r = random.randrange(m_size)
s = m_size-1

muro = array_muros[r]
row = np.take(muro, 0)
col = np.take(muro, 1)

#print("row = ", row)
#print("col = ", col)

bt.Inicializa_Maze_BT(m_size, m)
bt.Imprimir_Solucion(row, col)
