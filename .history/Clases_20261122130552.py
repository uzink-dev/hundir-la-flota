
import random
import numpy as np

from variables import (
    TAMANO_TABLERO,
    BARCOS,
    AGUA,
    BARCO,
    TOCADO,
    FALLO,
    RESULTADO_TOCADO,
    RESULTADO_AGUA,
    RESULTADO_REPETIDO
)


class Tablero:

    def __init__(self):
        # Creamos los dos tableros de 10x10
        self.tamano = TAMANO_TABLERO
        self.casillas = np.full((self.tamano, self.tamano), AGUA)
        self.disparos = np.full((self.tamano, self.tamano), AGUA)

    def colocar_barcos(self):

        # ==========================================
        # COLOCACIÓN MANUAL DE BARCOS (ACTIVA)
        # ==========================================

        # Posiciones fijas para realizar pruebas
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

        # Recorremos los barcos de la lista
        for barco in lista_barcos:
            tablero_temp = self.casillas.copy()
            valido = True

            # Comprobamos cada casilla del barco
            for pieza in barco:
                fila, columna = pieza

                # Comprobamos los límites del tablero
                if not (0 <= fila < self.tamano):
                    valido = False

                elif not (0 <= columna < self.tamano):
                    valido = False

                # Comprobamos que no haya otro barco
                elif self.casillas[fila, columna] == BARCO:
                    valido = False

                else:
                    tablero_temp[fila, columna] = BARCO

            # Si todas las casillas son válidas, colocamos el barco
            if valido:
                self.casillas = tablero_temp

        # ==========================================
        # COLOCACIÓN ALEATORIA (DESACTIVADA)
        # ==========================================

        # Para activar esta versión:
        # 1. Comentar el bloque de colocación manual
        # 2. Descomentar el siguiente bloque

        # self.casillas.fill(AGUA)

        # for longitud in BARCOS:
        #     colocado = False

        #     while not colocado:
        #         # Elegimos una posición aleatoria
        #         fila = random.randint(0, self.tamano - 1)
        #         columna = random.randint(0, self.tamano - 1)

        #         # Elegimos orientación horizontal o vertical
        #         orientacion = random.choice(["H", "V"])

        #         # Calculamos las casillas que ocuparía
        #         if orientacion == "H":
        #             posiciones = [
        #                 (fila, columna + i)
        #                 for i in range(longitud)
        #             ]
        #         else:
        #             posiciones = [
        #                 (fila + i, columna)
        #                 for i in range(longitud)
        #             ]

        #         valido = True

        #         # Comprobamos límites y solapamientos
        #         for f, c in posiciones:
        #             if not (0 <= f < self.tamano):
        #                 valido = False
        #                 break

        #             if not (0 <= c < self.tamano):
        #                 valido = False
        #                 break

        #             if self.casillas[f, c] == BARCO:
        #                 valido = False
        #                 break

        #         # Si es válido, colocamos el barco
        #         if valido:
        #             for f, c in posiciones:
        #                 self.casillas[f, c] = BARCO

        #             colocado = True

    def recibir_disparo(self, fila, columna):

        # Comprobamos si hemos acertado a un barco
        if self.casillas[fila, columna] == BARCO:
            self.casillas[fila, columna] = TOCADO
            self.disparos[fila, columna] = TOCADO
            return RESULTADO_TOCADO

        # Comprobamos si hemos disparado al agua
        elif self.casillas[fila, columna] == AGUA:
            self.casillas[fila, columna] = FALLO
            self.disparos[fila, columna] = FALLO
            return RESULTADO_AGUA

        # Si ya habíamos disparado, devolvemos repetido
        else:
            return RESULTADO_REPETIDO

    def mostrar(self, ocultar_barcos=False):

        # Si ocultamos barcos, mostramos solo los disparos
        if ocultar_barcos:
            print(self.disparos)

        # Si no, mostramos el tablero completo
        else:
            print(self.casillas)

    def quedan_barcos(self):

        # Devuelve True si queda algún barco sin alcanzar
        return np.any(self.casillas == BARCO)
