import numpy as np
import matriz
import BFS

TotalCreditos = 8
i = 0
partida = 0
SIZE = 0
maze = []
solucion = []

# Inicializa variables para backtracking


def Inicializa_Maze_BT(m_size, m):
    global partida
    global SIZE
    global maze
    global solucion

    SIZE = m_size
    maze = np.copy(m)

    partida = matriz.Get_Columna_Punto_Partida('num', maze)
    maze[SIZE-1][partida] = 0  # Cambia el 2 del punto de inicio por un 0

    solucion = np.copy(maze)
    BFS.Set_ROW_COL(SIZE, SIZE)

# Verifica si existe un camino por medio de un BFS


def Hay_Camino_BFS(maze):
    m_size = maze.shape[1]  # size de una columna
    nodo_partida = BFS.Get_Nodo_Partida(m_size-1, partida)
    nodo_salida = BFS.Get_Nodo_Salida(0, m_size-1)

    a = BFS.BFS(maze, nodo_partida, nodo_salida)
    print("¿Hay un camino de inicio a fin? = ", a)
    return a


def Es_Posicion_Valida(row, col):
    if (row >= 0) and (col >= 0) and (row < SIZE) and (col < SIZE):
        return True
    return False

# Funcion para resolver el puzle usando backtracking


def Resolver_Puzle(row, col, lastrow, lastcol):
    global i

    # Si llega a la salida, el puzle se ha resuelto
    if Hay_Camino_BFS(solucion):
        solucion[row][col] = 1
        solucion[lastrow][lastcol] = 0
        return True

    while (i < TotalCreditos):
        # Revisa si es posible visitar la celda
        # Los indices de la celda deben estar entre 0 y SIZE-1
        # El arreglo solucion debe tener un 0 para realizar la accion
        # Un 0 en el puzle indica que es un espacio libre
        # Un 1 en el puzle indica que hay un muro movible
        # Un -1 en el puzle indica que hay un muro inamovible

        # Si es una posicion valida
        if Es_Posicion_Valida(row, col):
            if (solucion[row][col] != solucion[lastrow][lastcol]):
                solucion[row][col] = 1
                solucion[lastrow][lastcol] = 0
            else:
                print("COMENZANDO")

            array_muros = matriz.Construye_Arreglo_Muros_Interiores(solucion)

            # Imprime arreglo de muros
            print("Muros: ", end='')
            for x in array_muros:
                print(x, end=' ')
            print()
            print()

            # Imprime solucion hasta el momento
            print(solucion)
            print()

            # Moverse abajo
            if (row < SIZE-2) and (solucion[row+1][col] == 0):
                print("Movimiento ABAJO con muro [", row, ", ", col, "]")
                i = i + 1
                Resolver_Puzle(row+1, col, row, col)
                return True

            # Moverse a la derecha
            if (col < SIZE-2) and (solucion[row][col+1] == 0):
                print(
                    "Movimiento a la DERECHA con muro [", row, ", ", col, "]")
                i = i + 1
                Resolver_Puzle(row, col+1, row, col)
                return True

            # Moverse arriba
            if (solucion[row-1][col] == 0):
                print("Movimiento ARRIBA con muro [", row, ", ", col, "]")
                i = i + 1
                Resolver_Puzle(row-1, col, row, col)
                return True

            # Moverse a la izquierda
            if (solucion[row][col-1] == 0):
                print(
                    "Movimiento a la IZQUIERDA con muro [", row, ", ", col, "]")
                i = i + 1
                Resolver_Puzle(row, col-1, row, col)
                return True

            # Backtracking
            # Si ninguno de los movimientos anteriores funcionan, deshace el movimiento
            solucion[row][col] = 0
            solucion[lastrow][lastcol] = 1
            print("BACKTRACKING en muro [", row, ", ", col, "]")
            i = i - 1

            return False

        return 0

# Imprime matriz solucion del backtracking


def Imprimir_Solucion(row, col):
    if(Resolver_Puzle(row, col, row, col)):
        print(solucion)
    else:
        print("No tiene solucion")
