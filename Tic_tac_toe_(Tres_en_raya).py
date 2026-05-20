# ============================================================
#  Tic-Tac-Toe  —  Tres en raya
#  Autor  : Jorge Martín Pérez-Moreno
#  Curso  : PCEP – Certified Entry-Level Python Programmer
#  Fecha  : 2025
# ============================================================
#
#  Reglas:
#   - La máquina juega con 'X', el usuario con 'O'
#   - La máquina siempre empieza colocando 'X' en el centro
#   - Los cuadros se numeran del 1 al 9
#   - La máquina elige su movimiento de forma aleatoria
# ============================================================
 
from random import randrange
 
 
def mostrar_tablero(tablero):
    """Muestra el estado actual del tablero en consola."""
    print("+-------" * 3, "+", sep="")
    for fila in range(3):
        print("|       " * 3, "|", sep="")
        for columna in range(3):
            print("|   " + str(tablero[fila][columna]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")
 
 
def introducir_movimiento(tablero):
    """
    Solicita el movimiento al usuario y lo valida.
    El bucle se repite hasta que:
      - El valor sea un número entre 1 y 9
      - El cuadro elegido esté libre
    """
    ok = False
    while not ok:
        movimiento = input("Ingresa tu movimiento (1-9): ")
 
        # Comprobar que es un dígito válido entre '1' y '9'
        ok = len(movimiento) == 1 and movimiento >= '1' and movimiento <= '9'
        if not ok:
            print("Movimiento erróneo, inténtalo de nuevo.")
            continue
 
        movimiento = int(movimiento) - 1    # Convertir a índice 0-8
        fila = movimiento // 3              # Calcular fila  (0, 1 o 2)
        columna = movimiento % 3            # Calcular columna (0, 1 o 2)
 
        # Comprobar que el cuadro no está ya ocupado
        ok = tablero[fila][columna] not in ['O', 'X']
        if not ok:
            print("¡Cuadro ocupado! Elige otro.")
            continue
 
    # Colocar la 'O' del usuario en el cuadro elegido
    tablero[fila][columna] = 'O'
 
 
def obtener_casillas_libres(tablero):
    """
    Recorre el tablero y devuelve una lista de tuplas (fila, columna)
    con las posiciones que aún están libres (no ocupadas por 'X' u 'O').
    """
    libres = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] not in ['O', 'X']:
                libres.append((fila, columna))
    return libres
 
 
def comprobar_victoria(tablero, simbolo):
    """
    Comprueba si el símbolo dado ha ganado la partida.
    Revisa las 3 filas, las 3 columnas y las 2 diagonales.
 
    Devuelve:
      'maquina'  → ganó la máquina ('X')
      'usuario'  → ganó el usuario ('O')
      None       → nadie ha ganado todavía
    """
    # Determinar a quién pertenece el símbolo
    if simbolo == 'X':
        quien = 'maquina'
    elif simbolo == 'O':
        quien = 'usuario'
    else:
        quien = None
 
    diagonal1 = diagonal2 = True  # Asumir ambas diagonales completas
 
    for rc in range(3):
        # Comprobar fila rc completa
        if tablero[rc][0] == simbolo and tablero[rc][1] == simbolo and tablero[rc][2] == simbolo:
            return quien
 
        # Comprobar columna rc completa
        if tablero[0][rc] == simbolo and tablero[1][rc] == simbolo and tablero[2][rc] == simbolo:
            return quien
 
        # Diagonal principal: (0,0) (1,1) (2,2)
        if tablero[rc][rc] != simbolo:
            diagonal1 = False
 
        # Diagonal secundaria: (0,2) (1,1) (2,0)
        if tablero[2 - rc][2 - rc] != simbolo:
            diagonal2 = False
 
    # Si alguna diagonal está completa, hay ganador
    if diagonal1 or diagonal2:
        return quien
 
    return None  # Nadie ha ganado aún
 
 
def movimiento_maquina(tablero):
    """
    Movimiento de la máquina: elige aleatoriamente
    uno de los cuadros libres y coloca una 'X'.
    """
    libres = obtener_casillas_libres(tablero)
    if len(libres) > 0:
        elegido = randrange(len(libres))    # Índice aleatorio dentro de la lista
        fila, columna = libres[elegido]
        tablero[fila][columna] = 'X'
 
 
# ============================================================
#  PROGRAMA PRINCIPAL
# ============================================================
 
# Crear tablero 3x3 con los números del 1 al 9
# tablero[fila][columna] → 'X', 'O' o número de cuadro libre
tablero = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
 
# La máquina siempre coloca la primera 'X' en el centro
tablero[1][1] = 'X'
 
# Calcular cuadros libres iniciales
libres = obtener_casillas_libres(tablero)
 
turno_humano = True     # El usuario mueve primero tras el centro
ganador = None
 
# Bucle principal: continúa mientras haya cuadros libres
while len(libres):
    mostrar_tablero(tablero)
 
    if turno_humano:
        introducir_movimiento(tablero)
        ganador = comprobar_victoria(tablero, 'O')      # ¿Ganó el usuario?
    else:
        movimiento_maquina(tablero)
        ganador = comprobar_victoria(tablero, 'X')      # ¿Ganó la máquina?
 
    if ganador is not None:
        break                                           # Hay ganador, salir del bucle
 
    turno_humano = not turno_humano                     # Cambiar turno
    libres = obtener_casillas_libres(tablero)           # Actualizar cuadros libres
 
# Mostrar tablero final
mostrar_tablero(tablero)
 
# Mostrar resultado
if ganador == 'usuario':
    print("¡Has ganado! Enhorabuena.")
elif ganador == 'maquina':
    print("¡He ganado! Mejor suerte la próxima vez.")
else:
    print("¡Empate!")
