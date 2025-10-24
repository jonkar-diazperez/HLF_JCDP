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

# 🚢 Hundir la Flota (HLF) – Python

Versión simplificada del clásico juego *Hundir la Flota (Battleship)*, desarrollada en Python como práctica del curso. El programa utiliza **NumPy para representar los tableros** y una **clase `barco`** para gestionar el estado de cada navío durante la partida.

Este proyecto se juega por consola, enfrentando al **jugador vs CPU**, con colocación aleatoria de barcos y turnos alternos de disparo.

---

## 📌 Características

- Tableros de 10x10 representados con `numpy.array`
- Colocación automática de barcos sin solapamientos
- Turnos alternados (jugador / CPU)
- Registro de disparos acertados (`X`) y agua (`#`)
- Clase `barco` con:
  - Posiciones y estado de cada sección
  - Detección de impactos
  - Marcado de barco hundido

---

## 🧠 Reglas del Juego

| Símbolo | Significado |
|---------|------------|
| `_` | Casilla vacía del jugador |
| `*` | Casilla oculta del rival |
| `O` | Parte de un barco |
| `X` | Impacto |
| `#` | Agua |

El objetivo es **hundir la flota rival antes de que hundan la tuya**.

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