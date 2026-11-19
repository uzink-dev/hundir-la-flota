import numpy as np
from funciones import mostrar_instrucciones, pedir_coordenadas, disparo_maquina

#1. MOSTRAR MENSAJE DE BIENVENIDA E INSTRUCCIONES (LA FUNCION INCLUYE AMBAS COSAS)
mostrar_instrucciones()


#CREACIÓN DE TABLEROS Y SÍMBOLOS

AGUA = "~"
BARCO = "B"
FALLO = "O"
TOCADO = "X"

tablero_jugador = np.full((10,10), AGUA)
tablero_maquina = np.full((10,10)), AGUA)
