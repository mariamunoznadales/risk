# Planificador de Ataques para Risk

Este programa genera estrategias para planificar ataques en el juego Risk. Calcula combinaciones de tropas, órdenes de ataque, y representa el tablero de juego, según las necesidades del usuario.

## Instrucciones de Uso

 **Entrada:**
   - Máximo de puntos disponibles para entrenar tropas.
   - Número de territorios enemigos.
   - Fuerza de defensa de cada territorio.
   - Fuerza y costo de cada tipo de tropa:
     - Infantería
     - Caballería
     - Artillería


***EJEMPLO DE ENTRADA***

Introduce el máximo de puntos disponibles para tropas: 100

Introduce el número de territorios enemigos: 3

Introduce la fuerza de defensa del Territorio 1: 50

Introduce el tipo del Territorio 1 (plano/montañoso/otro): plano

Introduce la fuerza de defensa del Territorio 2: 30

Introduce el tipo del Territorio 2 (plano/montañoso/otro): montañoso

Introduce la fuerza de defensa del Territorio 3: 40

Introduce el tipo del Territorio 3 (plano/montañoso/otro): otro

Fuerza de Infantería: 10

Costo de Infantería: 5

Fuerza de Caballería: 20

Costo de Caballería: 10

Fuerza de Artillería: 30

Costo de Artillería: 15


 **Salida:**
   - Combinaciones posibles de tropas según el presupuesto.
   - Permutaciones posibles del orden de ataque a los territorios.
   - Representación del tablero con información sobre cada territorio.


***EJEMPLO DE SALIDA***

Combinaciones posibles de tropas (10 encontradas):

{'Infantería': 5, 'Caballería': 2, 'Artillería': 1}

...

Tablero representado:

{'territorio': 1, 'defensa': 50, 'tipo': 'plano'}

{'territorio': 2, 'defensa': 30, 'tipo': 'montañoso'}

{'territorio': 3, 'defensa': 40, 'tipo': 'otro'}

Mejor estrategia encontrada:

Combinación de tropas: {'Infantería': 6, 'Caballería': 2, 'Artillería': 1}

Orden de ataque: (2, 3, 1)

Máximo de conquistas: 3

