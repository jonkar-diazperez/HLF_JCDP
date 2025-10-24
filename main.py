import numpy as np
import utils as u
import random as r
import os

"""
Inicializamos el entorno del juego
"""
tablero_jugador = u.crear_tablero("_")
tablero_rival = u.crear_tablero("*")

#tablero_jugador = np.full((10,10), "_")
#tablero_rival = np.full((10,10), "*")

u.ver_tableros(tablero_jugador,tablero_rival)

barco_4 = u.barco(4)
barco_4.crear_barco()
rival_4 = u.barco(4)
rival_4.crear_barco()

input("Pulsa una tecla para ver el barco en tu tablero.")

# Clear screen based on OS
os.system('cls' if os.name == 'nt' else 'clear')
tablero_jugador = barco_4.colocar_barco(tablero_jugador)
tablero_rival = rival_4.colocar_barco(tablero_rival)
#os.system('cls' if os.name == 'nt' else 'clear')
u.ver_tableros(tablero_jugador,tablero_rival)
print(barco_4.barco_status)
print(rival_4.barco_status)

flota_jugador = np.array([barco_4])
flota_rival = np.array([rival_4])
"""
PARTIDA: a partir de este punto se ejecuta el flujo para jugar la partida
"""

flota_KO_jugador = False
flota_KO_rival = False
fin_partida = False

# Sorteo turno inicio. 0 = Jugador ; 1 = Rival
input("Pulsa una tecla para sortear el turno de inicio de la partida.")
#turno = r.randint(0,1)
turno = 0
while not fin_partida:
    if turno:
        print("TURNO DE LA CPU") 
        fila_c = r.randint(0,9)
        columna_c = r.randint(0,9)
        print("DISPARO CPU", fila_c, columna_c)
        input("Pulsa una tecla para continuar.")
        if u.disparar(tablero_jugador,fila_c,columna_c) == "X":
                print("BARCO JUGADOR TOCADO")
                pos = (fila_j,columna_j)
                print(pos)
                for u.barco_jugador in flota_rival:
                    print(u.barco_jugador.barco_status)
                    for pos in u.barco_jugador.barco_status[0:]:
                         print("Actualizando estado barco en", fila_j, columna_j)
                         u.barco_jugador.barco_tocado(fila_j,columna_j)
                         break
        else: turno = False
        flota_KO_jugador = u.check_flota(flota_jugador)
        if flota_KO_jugador: print("CPU GANADOR")     
    else:
            fila_j = int(input("Indica coordenada fila X (0-9):"))
            columna_j = int(input("Indica coordenada columna Y (0-9):"))
            if u.disparar(tablero_rival,fila_j,columna_j) == "X":
                print("BARCO RIVAL TOCADO")
                pos = (fila_j,columna_j)
                print(pos)
                for u.barco_rival in flota_rival:
                    print(u.barco_rival.barco_status)
                    for pos in u.barco_rival.barco_status[0:]:
                         print("Actualizando estado barco en", fila_j, columna_j)
                         u.barco_rival.barco_tocado(fila_j,columna_j)
                         break
            else: turno = True
            flota_KO_rival = u.check_flota(flota_rival)
            if flota_KO_rival: 
                 print("JUGADOR GANADOR")
               
    if flota_KO_rival or flota_KO_jugador: fin_partida = True
u.ver_tableros(tablero_jugador,tablero_rival)
