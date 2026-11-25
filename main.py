
from funciones import mostrar_instrucciones, pedir_coordenadas, disparo_maquina
from clases import Tablero
from variables import (
    RESULTADO_TOCADO,
    RESULTADO_AGUA,
    RESULTADO_REPETIDO
)


# FUNCION PARA MOSTRAR LOS TABLEROS

def mostrar_tableros(tablero_jugador, tablero_maquina):
    print("\nTABLERO DEL JUGADOR")
    tablero_jugador.mostrar()

    print("\nTABLERO DE LA MÁQUINA")
    # MOSTRAMOS SOLO LOS DISPAROS, SIN REVELAR LOS BARCOS
    tablero_maquina.mostrar(ocultar_barcos=True)


# MOSTRAR MENSAJE DE BIENVENIDA E INSTRUCCIONES

mostrar_instrucciones()


# CREACION DE TABLEROS Y COLOCACION DE BARCOS

tablero_jugador = Tablero()
tablero_maquina = Tablero()

tablero_jugador.colocar_barcos()
tablero_maquina.colocar_barcos()


# EMPIEZA EL JUEGO

while True:

    # MOSTRAMOS LOS TABLEROS
    mostrar_tableros(tablero_jugador, tablero_maquina)

    # TURNO DEL JUGADOR
    print("\nTu turno:")

    while True:

        fila, columna = pedir_coordenadas()

        # REALIZAMOS EL DISPARO SOBRE EL TABLERO DE LA MÁQUINA
        resultado = tablero_maquina.recibir_disparo(fila, columna)

        # AVISO DE DISPARO REPETIDO
        if resultado == RESULTADO_REPETIDO:
            print("Ya has disparado a esta casilla")
            continue

        # SI ACERTAMOS, VOLVEMOS A DISPARAR
        if resultado == RESULTADO_TOCADO:
            print("¡Tocado!")

            # COMPROBAMOS SI HEMOS GANADO
            if not tablero_maquina.quedan_barcos():
                print("¡ENHORABUENA! ¡HAS GANADO!")
                print("\nFin de la partida")
                quit()

            # MOSTRAMOS LOS TABLEROS ACTUALIZADOS
            mostrar_tableros(tablero_jugador, tablero_maquina)
            continue

        # SI FALLAMOS, TERMINA NUESTRO TURNO
        if resultado == RESULTADO_AGUA:
            print("¡Agua!")
            break

    #  COMIENZA TURNO DE LA MÁQUINA
    print("\nTurno de la máquina")

    while True:

        # LA MÁQUINA ELIGE COORDENADAS Y DISPARA
        resultado = disparo_maquina(tablero_jugador)

        # SI LA MÁQUINA ACIERTA, REPITE EL DISPARO
        if resultado == RESULTADO_TOCADO:
            print("La máquina ha tocado uno de tus barcos")

            # COMPROBAMOS SI LA MÁQUINA HA GANADO
            if not tablero_jugador.quedan_barcos():
                print("¡Gana la máquina!")
                print("\nFin de la partida")
                quit()

            continue

        # SI LA MÁQUINA FALLA, PIERDE SU TURNO
        if resultado == RESULTADO_AGUA:
            print("La máquina ha disparado al agua")
            break


print("\nFin de la partida")
