# %%
import random
import numpy as np

# Configuración del tablero
TAMANO_TABLERO = 10

# Barcos (10 barcos)
BARCOS = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]

# Símbolos del tablero
AGUA = "~"
BARCO = "B"
TOCADO = "X"
FALLO = "O"

# Resultados de los disparos
RESULTADO_TOCADO = "tocado"
RESULTADO_AGUA = "agua"
RESULTADO_REPETIDO = "repetido"


class Tablero:

    def __init__(self):
        self.tamano = TAMANO_TABLERO
        self.casillas = np.full((self.tamano, self.tamano), AGUA)

    def colocar_barcos(self):
        """Coloca los barcos en el tablero."""
        
        lista_barcos = [
            [(0, 0)],
            [(0, 2)],
            [(0, 4)],
            [(0, 6)],
            [(2, 0), (2, 1)],
            [(2, 3), (2, 4)],
            [(2, 6), (2, 7)],
            [(4, 0), (4, 1), (4, 2)],
            [(4, 4), (4, 5), (4, 6)],
            [(6, 0), (6, 1), (6, 2), (6, 3)],
        ]

        for barcos in lista_barcos:
            tablero_temp = self.casillas.copy()
            valido = True
            """ Para luego colocar los random necesitamos asegurarnos que entran en el tablero
            de momento sabemos que el tablero va de 0 a 9 """
            for pieza in barcos:
                fila = pieza[0]
                columna = pieza[1]

                if fila < 0 or fila > TAMANO_TABLERO - 1:
                    valido = False
                elif columna < 0 or columna > TAMANO_TABLERO - 1:
                    valido = False
                elif self.casillas[pieza] == BARCO:  """ si intenta colocar donde ya hay barco """
                    valido = False
                else:
                    tablero_temp[pieza] = BARCO

            if valido:
                self.casillas = tablero_temp

    def recibir_disparo(self, fila, columna): 
        if self.casillas[fila, columna] == BARCO:
            self.casillas[fila, columna] = TOCADO
            return RESULTADO_TOCADO
        
        if self.casillas[fila, columna] == AGUA:
            self.casillas[fila, columna] = FALLO
            return RESULTADO_AGUA
        
        else:
            RESULTADO_REPETIDO

    def mostrar(self):
        print(self.casillas)

# %%
