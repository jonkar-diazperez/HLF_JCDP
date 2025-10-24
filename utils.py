import numpy as np
import random as r

def crear_tablero(relleno:str):
    tablero = np.full((10,10), relleno)
    return tablero

def ver_tableros(tablero_1,tablero_2):
    print("TABLERO JUGADOR\n",tablero_1)
    print("\n", "_"*40, "\n")
    print("TABLERO CONTRARIO\n",tablero_2)

    return True

def disparar(tablero, fila, columna):
    """
    for barco in flota:
        if (fila,columna) in barco.barco_status:
            print("Barco Tocado")
            print(fila)
            print(columna)
            print(barco.barco_status)
    """
    if tablero[fila,columna] == "O":
        print("Tocado posición ",fila,columna)
        tablero[fila,columna] = "X"

    else:
        print("AGUA")
        tablero[fila,columna] = "#"
    return tablero[fila,columna]

def check_flota(flota):
    flota_KO = True
    for barco_flota in flota:
        if not barco_flota.hundido: flota_KO = False
    return flota_KO

class barco:
        
        #Atributo para determinar el estado del barco
        hundido = False
        barco_pos = [(0,0),False]
        barco_status =[]
        """
        Clase para representar los barcos del juego.
        Tendrán como parámetro la eslora, como una lista.
        """
        def __init__(self, eslora:int):
            """

            """
            self.eslora = eslora

        def crear_barco(self):
            self.barco_status = []
            for i in range(self.eslora):
                self.barco_status.append(self.barco_pos)
            #print(barco_status)
            return self.barco_status
        
        def colocar_barco(self, tablero):
            barco_pos_OK = False
            
            while not barco_pos_OK:
                #pos_x_ini = input("Indica la fila de la posicion inicial en el tablero donde quieres colocar el barco (X):")
                #pos_y_ini = input("Indica la columna de la posicion inicial en el tablero donde quieres colocar el barco (Y):")
                #or_ini = input("Indica si quieres colocar el barco en posición vertical (V) u horizontal (H)")
                pos_x_ini = r.randint(0,9)
                pos_y_ini = r.randint(0,9)               
                or_ini = r.choice(['H','V'])
                print(pos_x_ini, pos_y_ini,or_ini)

                if (pos_x_ini+self.eslora)>=9 or (pos_y_ini+self.eslora)>=9:
                    print("Fuera de rango.")
                
                elif or_ini == "H":
                    if (pos_y_ini+self.eslora) > 9: print("Barco fuera tablero en Y") 
                    elif "O" in tablero[pos_x_ini][pos_y_ini:pos_y_ini+self.eslora]: print("Posiciones ocupadas. Elige otra.")
                    
                    else:
                        for n,s in enumerate(self.barco_status):
                            s = [(pos_x_ini,pos_y_ini+n),False]
                            print(s)
                            self.barco_status[n] = s
                            tablero[pos_x_ini][pos_y_ini+n] = "O"
                        barco_pos_OK = True
                elif or_ini == "V":
                    if (pos_x_ini+self.eslora) > 9: print("Barco fuera tablero en X") 
                    elif "O" in tablero[pos_x_ini:pos_x_ini+self.eslora][pos_y_ini]: print("Posiciones ocupadas. Elige otra.")
                    
                    else:
                        for n,s in enumerate(self.barco_status):
                            s = [(pos_x_ini+n,pos_y_ini),False]
                            print(s)
                            self.barco_status[n] = s
                            tablero[pos_x_ini+n][pos_y_ini] = "O"
                        barco_pos_OK = True
                else:
                    "ERROR CREANDO BARCO"
            #print("TABLERO ACTUALIZADO\n", tablero)
            print(self.barco_status)
            return tablero
        
        def barco_tocado(self, pos_x, pos_y):
            s = [(pos_x,pos_y),False]
            print(s)
            hundido_upd = True
            for i,posicion in enumerate(self.barco_status):
                #print(posicion)
                if posicion == s: self.barco_status[i] = [(pos_x,pos_y),True] 
                elif not posicion[1]: hundido_upd = False
                #self.barco_status[n] = s
            if hundido_upd == True: barco.hundido = True
            print(self.barco_status)
            print(hundido_upd)

            return barco.hundido
             
            

    




