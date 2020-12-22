import numpy as np

""" Construye matriz completa """
def Construye_Matriz_Completa(size):
  file = open("levelbefore.txt", "r") # Abre archivo

  # Matriz completa de caracteres
  m_comp = np.chararray((size, size), unicode=True)
  m_comp[:] = ' '

  # Lee char por char
  i = 0 # Fila
  j = 0 # Columna
  k = 0 # Contador para saber si la posicion es par o impar
  while (1):
    char = file.read(1) # Obtiene el caracter
    k = k + 1

    if not char: # Si se acaban los caracteres, termina el ciclo
      break
    
    # Control de indices size-columna y contador
    if (j == size):
      i = i + 1
      j = 0
    if (k == (size * 2) + 1):
      k = 0
    
    # Si el contador es impar, guarda el caracter en la matriz
    # De esta manera se evitan los espacios entre caracteres que existen en el input
    if (k % 2 != 0):
      m_comp[i][j] = char
      j = j + 1

  file.close()
  return m_comp


""" Get Punto de Partida """
def Get_Columna_Punto_Partida(tipodato, m):
  if (tipodato == 'char'):
    a, b = np.where(m == 'p') # a = size, b = columna
    return b
  if (tipodato == 'num'):
    a, b = np.where(m == 2) # a = size, b = columna
    return b
  
  return - 1


""" Punto de partida y salida al interior """
def Punto_PartidaSalida_al_Interior(size):
  m_comp = Construye_Matriz_Completa(size)
  
  b = Get_Columna_Punto_Partida('char', m_comp)
  size_m_comp = m_comp.shape[1] # size de la columna

  m_comp[size_m_comp-2][b] = 'p' # Sube una size el marcador de partida
  m_comp[size_m_comp-1][b] = '*' # 
  m_comp[1][size_m_comp-2] = 's'
  m_comp[1][size_m_comp-1] = '*'

  return m_comp

# Escribe matriz a archivo
#c = np.savetxt('output.txt', m_comp, delimiter =' ', fmt='%s')

""" Construye matriz interior """
def Construye_Matriz_Interior(size, m_comp):
  # Matriz interior de caracteres
  m_int = np.chararray((size-2, size-2), unicode=True)
  m_int[:] = ' '

  m_comp = Punto_PartidaSalida_al_Interior(size)
  size_m_comp = m_comp.shape[1] # size de la columna

  a = 0
  i = 1 # Se salta la primera size ya que tiene solo muros borde
  while (i < size_m_comp - 1): # Recorre la matriz completa saltandose ademas la ultima size
    b = 0
    j = 1 # Se salta la primera columna ya que tiene solo muros borde
    while (j < size_m_comp - 1): # Recorre la matriz completa saltandose ademas la ultima columna
      m_int[a][b] = m_comp[i][j]
      b = b + 1
      j = j + 1
    a = a + 1
    i = i + 1
  
  return m_int


""" Construye matriz numerica """
def Construye_Matriz_Numerica(size):
  # Matriz de enteros de size (size-2)^2
  m = np.zeros((size-2, size-2), dtype=int)
  
  m_comp = Punto_PartidaSalida_al_Interior(size)
  m_int = Construye_Matriz_Interior(size, m_comp)  
  
  size_m_comp = m_comp.shape[1] # size de la columna
  
  #Recorre la matriz interior y segun el caracter dara un valor entero a la matriz numerica
  i = 0
  while (i < size_m_comp - 2):
    j = 0
    while (j < size_m_comp - 2):
      if (m_int[i][j] == '*'): # Si encuentra un muro
        m[i][j] = 1
      elif (m_int[i][j] == 'x'): # Si encuentra una trampa
        m[i][j] = -1
      elif (m_int[i][j] == 'p'): # Si encuentra el punto de partida
        m[i][j] = 2
      else: # Para todos los demas casos (espacios y salida)
        m[i][j] = 0 # Espacio libre
      j = j + 1
    i = i + 1
  
  return m

def Construye_Arreglo_Muros_Interiores(m):
  size = m.shape[1] # size de una columna
 
  #Cuenta el total de muros interiores
  muros = 0
  for x in m:
    for y in x:
      if (y != -1) and (y != 0):
        muros = muros + 1

  # Declara un arreglo de coordenadas con la cantidad calculada
  array = np.zeros((muros, 2), dtype=int)

  k = 0
  i = 0
  while (i < size):
    j = 0
    while (j < size):
      if (m[i][j] == 1):
        array[k] = [i, j]
        k = k + 1
      j = j + 1
    i = i + 1
      
  return array

