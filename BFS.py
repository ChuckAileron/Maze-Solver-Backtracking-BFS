import numpy as np
from collections import deque

# Inicializa fila y columna
def Set_ROW_COL(r, c):
  global ROW
  global COL
  ROW = r
  COL = c

# Estructura de nodo para acceder a sus coodenadas
class Nodo:
    def __init__(self,x: int, y: int):
        self.x = x
        self.y = y

# Estructura para nodos agregados a la cola
class Nodo_en_Cola:
    def __init__(self, n: Nodo, dist: int):
        self.nodo = n  # The cordinates of the cell
        self.dist = dist  # Cell's distance from the source

# Obtener nodo de partida
def Get_Nodo_Partida(row, col):
  partida = Nodo(row, col)
  return partida

# Obtener nodo de salida
def Get_Nodo_Salida(row, col):
  salida = Nodo(row, col)
  return salida

# Verifica si la celda es valida o no
def isValid(r, c):
  if (r >= 0) and (r < ROW) and (c >= 0) and (c < COL):
    return True
  else:
    return False

# Arreglos para las posiciones de los vecinos de una celda
rowNum = [-1, 0, 0, 1] 
colNum = [0, -1, 1, 0] 
  
# Funcion para encontrar el camino mas corto desde una celda de inicio a una celda destino
def BFS(maze, p: Nodo, s: Nodo):
  k = 0

  #Cuenta el total de muros interiores
  muros = 0
  for x in maze:
    for y in x:
      if (y == 1):
        muros = muros + 1

  global solucion # Arreglo de coordenadas para la solucion
  solucion = np.zeros((muros, 2), dtype=int)

  # Verifica que el nodo inicial y destino no tengan un muro
  if (maze[p.x][p.y] != 0) or (maze[s.x][s.y] != 0): 
      return False
  
  # Crea matriz de visitados inicializada en Falso
  visitado = np.zeros((ROW, COL), dtype=bool)
  #visitado = [[False for i in range(COL)] for j in range(ROW)]

  # Marca el nodo de partida como visitado
  visitado[p.x][p.y] = True

  q = deque() # Crea una cola

  # Agrega el nodo inicial a la cola (distancia 0)
  start = Nodo_en_Cola(p,0)
  q.append(start)

  # Busqueda en profundida (BFS)
  # Mientras queden nodos en la cola
  while q:
    actual = q.popleft() # Saca el nodo al comienzo de la cola
    
    # Si se ha llegado al nodo de salida, se termina el ciclo
    nodo = actual.nodo
    if (nodo.x == s.x) and (nodo.y) == s.y:
      print(solucion)
      return True
    
    # Si no, revisa los nodos vecinos
    for i in range(4):
        row = nodo.x + rowNum[i]
        col = nodo.y + colNum[i]
        
        # Si el nodo es valido, tiene un espacio libre y no ha sido visitado
        if (isValid(row, col)) and (maze[row][col] == 0) and not (visitado[row][col]):
            visitado[row][col] = True # Marca el nodo como visitado
            # Obtiene el nodo adyacente su distancia
            nodoVecino = Nodo_en_Cola(Nodo(row, col), actual.dist+1)
            q.append(nodoVecino) # Agrega el nodo adyacente a la cola
            solucion[k] = [row, col]
            k = k + 1
  
  print("BFS: ", end='')
  for x in solucion:
    if (np.any(x != [0, 0])):
      print(x, end=' ')
  print()

  # Retorna falso si no se pudo llegar a la salida
  return False
