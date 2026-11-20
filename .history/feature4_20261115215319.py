import numpy as np
from funciones import mostrar_instrucciones, pedir_coordenadas, disparo_maquina

#FUNCION PARA MOSTRAR LOS TABLEROS

def mostrar_tableros(tablero_jugador, tablero_maquina):
    print("\nTABLERO DEL JUGADOR")
    print(tablero_jugador)

    print("\nTABLERO DE LA MÁQUINA")
    #PARA QUE NO SE VEAN LOS BARCOS DE LA MAQUINA LO OCULTAMOS CON AGUA
    
    tablero_maquina_oculto = np.where(tablero_maquina == "B", AGUA, tablero_maquina)
    print(tablero_maquina_oculto)

#MOSTRAR MENSAJE DE BIENVENIDA E INSTRUCCIONES (LA FUNCION INCLUYE AMBAS COSAS)
mostrar_instrucciones()

#CREACION TABLEROS

AGUA = "~"
BARCO = "B"
TOCADO = "X"
FALLO = "O"

tablero_jugador = np.full((10,10), AGUA)
tablero_maquina = np.full((10,10), AGUA)

#EMPIEZA EL JUEGO MOSTRANDO LOS TABLEROS Y PIDIENDO COORDENADAS

mostrar_tableros(tablero_jugador, tablero_maquina)
print("\nTu turno:")
fila, columna = pedir_coordenadas

#AVISO DE DISPARO REPETIDO

#SI ACERTAMOS
if tablero_maquina[fila,columna] == "B":
    tablero_maquina[fila, columna] = X
    print("Tocado")
    
