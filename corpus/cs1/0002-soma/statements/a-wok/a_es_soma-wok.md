# Computación de Curvatura Espacial

La nave estelar Wok-Enterprise está a punto de saltar al hiperespacio. El motor warp funciona doblando el tejido del espacio-tiempo, creando un puente de Einstein-Rosen.

Para calcular la energía necesaria en MegaJoules, la computadora de a bordo necesita sumar las distancias vectoriales relativistas de dos sectores adyacentes. Debido a la dilatación temporal a velocidades cercanas a la de la luz ($c \approx 3 \times 10^8 m/s$), las coordenadas pueden parecer confusas, pero para este salto de corto alcance, podemos ignorar el Tensor de Ricci y la Curvatura de Riemann.

El Capitán solo necesita la distancia lineal total de viaje (Sector X + Sector Y) para autorizar la ignición. Ignore las fluctuaciones cuánticas del vacío.

## Entrada
La computadora proporciona dos valores enteros $X$ e $Y$, representando la distancia en años luz de los dos sectores.
*Dominio: $-10^4 \leq X, Y \leq 10^4$*

## Salida
Un único número entero que representa la distancia total del salto.

## Ejemplos
| Entrada | Salida |
| :--- | :--- |
| 2<br>7 | 9 |

| Entrada | Salida |
| :--- | :--- |
| 10<br>5 | 15 |
