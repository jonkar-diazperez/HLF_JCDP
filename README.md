# HUNDIR LA FLOTA 🚢
# (C) by Juan Carlos Díaz Pérez
## Sinopsis Proyecto
El objetivo del proyecto es construir un juego que imite el juego de mesa
HUNDIR LA FLOTA. El juego consiste en destruir la flota de barcos de distinto tamaño del jugador contrario para ganarlo.

Para ello se usan básicamente 2 objetos en el juego, con sus métodos asociados:
    * Barcos: las piezas de juego de cada jugador, que son distintos y de varios tamaños.
    * Tableros: sería "el campo de juego" de cada jugador. Sería donde se muestran los barcos de cada jugador (tablero_jugador) y donde se dispara a los barcos del rival (tablero_rival).

## INTRODUCCIÓN

Para la implementación del juego se utiliza **NumPy para representar los tableros** y una **clase `barco`** para gestionar el estado de cada navío durante la partida.

Para jugar usamos la salida del terminal, enfrentando al **jugador vs CPU**, con colocación aleatoria de barcos y turnos alternos de disparo.

---

## 📌 RESUMEN TÉCNICO

- Tableros de 10x10 representados con `numpy.array`
- Colocación automática de barcos sin solapamientos
- Turnos alternados (jugador / CPU)
- Registro de disparos acertados (`X`) y agua (`#`)
- Clase `barco` con:
  - Posiciones y estado de cada sección
  - Detección de impactos
  - Marcado de barco hundido

## 🧠 TABLA SÍMBOLOS TABLERO

| Símbolo | Significado |
|---------|------------|
| `_` | Casilla vacía del jugador |
| `*` | Casilla oculta del rival |
| `O` | Parte de un barco |
| `X` | Impacto |
| `#` | Agua |

---

## 🖥️ Ejemplo visual del tablero

Al iniciar la partida, se muestran los dos tableros:

TABLERO JUGADOR
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']

TABLERO RIVAL
['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']

Tras disparos, puede verse así:

Jugador dispara a (2, 5) → Impacto!

['*', '*', '*', '*', '*', 'X', '*', '*', '*', '*_*']

### 🧠 FLUJO `main.py`

1. **Inicialización**  
   Se crean los tableros del jugador y del rival, y se muestran por pantalla.

2. **Creación y colocación de barcos**  
   Se generan los barcos de cada jugador usando la clase `barco` y se colocan automáticamente en el tablero sin solaparse.

3. **Control de la partida**  
   Se establece quién dispara primero y se entra en un bucle de turnos alternos:
   - La **CPU dispara automáticamente** eligiendo coordenadas aleatorias.
   - El **jugador introduce las coordenadas manualmente**.
   Tras cada disparo se muestra si se ha hecho “agua” o “impacto”.

4. **Comprobación de estado**  
   Después de cada turno se revisa si quedan barcos en pie mediante `check_flota()`.

5. **Final de partida**  
   El bucle termina cuando una flota es hundida por completo y se declara un ganador, mostrando los tableros finales.

### 🧠 FUNCIONES `utils.py`

El archivo `utils.py` contiene todas las funciones auxiliares del proyecto y la clase `barco`, que encapsula la lógica relacionada con cada los mismos. Su objetivo es proporcionar a `main.py` las herramientas necesarias para gestionar tableros, disparos y el estado de los barcos.

1. **Funciones de tablero**
   - `crear_tablero()`  
     Genera un tablero de 10×10 usando `NumPy`, rellenado inicialmente con un símbolo (`_` para jugador, `*` para rival).
   - `ver_tableros()`  
     Muestra por consola el tablero del jugador y el del rival, separados visualmente.
   - `disparar()`  
     Recibe una coordenada y marca el resultado del disparo:  
       - `X` si impacta en un barco  
       - `#` si es agua  
     También actualiza el tablero en esa posición.
   - `check_flota()`  
     Recorre todos los barcos de una flota y devuelve `True` si están hundidos, o `False` si queda alguno en pie.

2. **Clase `barco`**
   Representa cada barco del juego y gestiona:
   - Su **eslora** (tamaño)
   - Las **posiciones que ocupa en el tablero**
   - Si está **tocado o hundido**

   Métodos principales:
   - `crear_barco()`  
     Inicializa la estructura del barco con tantas secciones como indica su eslora.
   - `colocar_barco()`  
     Asigna aleatoriamente su posición en el tablero (horizontal o vertical) evitando solapamientos.
   - `barco_tocado()`  
     Marca una sección del barco como dañada y comprueba si todas sus partes han sido impactadas para de
