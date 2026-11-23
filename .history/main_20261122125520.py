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

#CREACION TABLEROS Y COLOCACION BARCOS

AGUA = "~"
BARCO = "B"
TOCADO = "X"
FALLO = "O"

tablero_jugador = np.full((10,10), AGUA)
tablero_maquina = np.full((10,10), AGUA)

from clases import Tablero

tablero_jugador = Tablero()
tablero_maquina = Tablero()

tablero_jugador.colocar_barcos()
tablero_maquina.colocar_barcos()

while True:
#EMPIEZA EL JUEGO MOSTRANDO LOS TABLEROS Y PIDIENDO COORDENADAS

    mostrar_tableros(tablero_jugador, tablero_maquina)
# TURNO DEL JUGADOR

    print("\nTu turno:")
    fila, columna = pedir_coordenadas()

#AVISO DE DISPARO REPETIDO
    if tablero_maquina[fila, columna] in ["X","O"]:
        print("Ya has disparado a esta casilla")
        continue

#SI ACERTAMOS
    if tablero_maquina[fila,columna] == "B":
        tablero_maquina[fila, columna] = "X"
        print("Tocado")

    #VEMOS SI HEMOS GANADO, ES DECIR, A LA MAQUINA LE QUEDAN 0 "B" EN EL TABLERO.
        if np.sum(tablero_maquina =="B")== 0:
            print("ENHORABUENA! HAS GANADO!!")
            break

        continue

#SI FALLAMOS
    else:
        tablero_maquina[fila,columna] = "O"
        print("¡Agua!")

#TURNO MAQUINA

    print("\nTurno de la máquina")

    while True:

         resultado = recibir_disparo(tablero_jugador)

         if np.sum(tablero_jugador =="B")== 0:
            break

#SI LA MAQUINA FALLA PIERDE SU TURNO
         if resultado == AGUA:
            break

 #COMPROBAMOS SI LA MAQUINA HA GANADO VIENDO SI EN NUESTRO TABLERO QUEDAN 0 "B"

    if np.sum(tablero_jugador == "B") == 0:
        print("¡Gana la máquina!")
        break


print("\nFin de la partida")




