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

#CREACIÓN DE TABLEROS Y SÍMBOLOS

AGUA = "~"
BARCO = "B"
FALLO = "O"
TOCADO = "X"



#EMPEZAMOS EL BUCLE PARA LOS TURNOS

w