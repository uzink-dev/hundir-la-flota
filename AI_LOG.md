
# AI_LOG · Team Challenge Hundir la flota

## Equipo de trabajo

| Integrante | Responsabilidad | Archivos |
|---|---|---|
| Santiago González | Scrum Master, configuración y documentación. Revisión. | `variables.py`, `README.md`, `requirements.txt`, `AI_LOG.md` |
| Antonio Diz | Desarrollo de la clase Tablero | `clases.py` |
| Alba Fernández | Funciones auxiliares del juego | `funciones.py` |
| Celia Herrera | Programa principal, integración y pruebas | `main.py` |

## Herramientas de IA utilizadas

Pendiente de revisar y completar con el equipo.

## Resumen por módulo

### Niveles de uso de IA

- **Nivel 0:** Sin utilización de inteligencia artificial.
- **Nivel 1:** Consulta puntual. El código ha sido desarrollado por el equipo.
- **Nivel 2:** La IA ha generado partes del código que posteriormente se han revisado y adaptado.
- **Nivel 3:** La mayor parte del código ha sido generada por IA.

| Módulo | Responsable | Nivel de IA (0-3) | Nº de prompts | ¿Podría repetirlo sin IA? |
|---|---|---|---|---|
| `variables.py` | Santiago González | 2 | 4 | Si, con bastante más tiempo |
| `clases.py` | Antonio Diz | 2 | 3 | Sí, con muchas dudas y más tiempo |
| `funciones.py` | Alba Fernández | 2 | 4 | Sí, con más tiempo |
| ´main.py´ | Celia Herrera | 2 | 4 | Sí, con más tiempo |
| `README.md` | Santiago González | 0 | 0 | Sí |

## Registro de prompts

Este apartado se completará después de revisar el uso de IA con el equipo.

Se utilizará la siguiente plantilla para cada prompt que haya influido en el desarrollo del proyecto.

### Módulo: Revisión de proyecto

- **Responsable:** Santiago González
- **Objetivo:** La app fallaba
- **Prompt utilizado:** dime si hay errores en estos códigos (se adjuntan los archivos)
- **Respuesta relevante:** había algunos errores que se subsanaron:
- **Cambios realizados:** Se corrigió la sintaxis y la estructura de la clase Tablero.
    - Se incorporó un segundo array NumPy para registrar los disparos.
    - Se corrigió la devolución de resultados: tocado, agua y repetido.
    - Se adaptó main.py para utilizar los métodos de la clase Tablero.
    - Se corrigió la gestión de los turnos entre el jugador y la máquina.
    - Se centralizó el uso de constantes en variables.py.
    - Se preparó la lógica de colocación aleatoria de barcos, manteniendo temporalmente la colocación manual para realizar pruebas.


## Módulo: clases.py

- **Responsable:** Antonio Diz
- **Objetivo:** ir comparando mi código con una versión de referencia, corregir mis errores y resolver dudas paso a paso.
- **Prompt utilizado:** “Sigue este ejemplo en cuanto a lógica programacional, utiliza una programación lo más simple posible”, y “transformar .ipynb a .py y revisar errores” más preguntas sueltas sobre el porqué de cada línea.
- **Respuesta relevante:** Me explicó tablero_temp = self.casillas.copy(), por qué pieza[0] y pieza[1], el -1 en los límites y por qué recibir_disparo recibe fila y columna. Me señaló errores de mi versión (colocar_barco en vez de colocar_barcos, barcos en vez de barco en el bucle, valido sin inicializar, self.casilla[,] y falta de return) y me dio el .py corregido.
- **Cambios realizados:** fui comparando la referencia con mi código y corregí mis errores y ejecuté el código, verificando “tocado”, “repetido” y “agua”.
- Comprobación:** comparé línea a línea mi versión con la de referencia.
- **Decisión propia:** colocación manual de barcos.

## Módulo: funciones.py

- **Responsable:** Alba Fernández
- **Objetivo:** pedir y validar coordenadas (pedir_coordenadas), que la máquina dispare sin repetir casilla (disparo_maquina) e imprimir las instrucciones (mostrar_instrucciones).
- **Prompt utilizado:** “guíame sin darme el código hecho, y dime qué falla en mis versiones”.
- **Respuesta relevante:** Me explicó split, try/except ValueError y el bucle con !=. Me señaló errores de mis versiones (except sin tipo, for y segundo input que sobraban, return mal colocado, condición al revés). Me ayudó con el texto de mostrar_instrucciones. pedir_coordenadas y disparo_maquina las escribí yo por capas y las probé.
- **Comprobaciones:** probé 4,5, a,b, 4, 11,2 y Enter vacío, y un tablero de pega que devolvía “repetido” dos veces y luego “agua”.

## Módulo: main.py

- **Responsable:** Celia Herrera
- **Objetivo:** crear el bucle principal del juego, es decir, el desarrollo de los turnos sucesivos del jugador y de la máquina aplicando las variables y clases creadas por el resto del equipo.
- **Prompt utilizado:** “Sin darme el código, explícame cómo sería el desarrollo lógico  de una partida del juego” “Corrige este código y explícame por qué no funciona o de que otra forma podría hacerlo”
- **Respuesta relevante:**
    - Me explicó la solución if np.sum(tablero_maquina == "B") == 0 para indicar que no quedan barcos en el tablero y se ha perdido la partida y np.where(condicion, valor_si_verdadero, valor_si_falso) para poder ocultar el tablero de la máquina.
    - Me señaló errores de mi versión, como errores en la tabulación del bucle principal while True
- **Cambios realizados:** cambios en la estructura, tabulado y sintaxis del código para corregir errores y adaptarlo al trabajo de los compañeros.
- **Comprobación:** comparación del código con las referencias.