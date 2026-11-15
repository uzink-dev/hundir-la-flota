import random


def mostrar_instrucciones():
    """Imprime las instrucciones del juego."""
    print("Bienvenido a Hundir la flota")
    print("Dispara escribiendo fila,columna (de 0 a 9). Ejemplo: 3,4")
    print("Si aciertas, vuelves a disparar. Si das en agua, dispara la máquina.")


def pedir_coordenadas():
    """Pide las coordenadas, valida que sean dos enteros dentro del rango del tablero y devuelve fila y columna."""
    while True:
        coordenadas = input("Introduzca las coordenadas: ")
        try:
            fila,columna = coordenadas.split(",")
            fila = int(fila)
            columna = int(columna)
        except ValueError:
            print("Debe introducir dos numeros enteros separados por una coma")
            continue
        #SUSTITUIR 9 POR TAMANO_TABLERO -1 (variables.py)
        if 0<= fila <=9 and 0<= columna <=9 :
            return fila,columna
        else:
            print("El rango debe estar entre 0 y 9")

        
def disparo_maquina(tablero_rival):
    """Elige una casilla al azar para disparar que no se haya disparado, dispara y devuelve el resultado
    tocado o agua"""
    #sustituir 9 por TAMANO_TABLERO -1 
    while True:
        fila = random.randint(0,9)
        columna = random.randint(0,9)
        resultado = tablero_rival.recibir_disparo(fila,columna)
        if resultado != "repetido":#usar RESULTADO_REPETIDO de variables.py
            return resultado
    