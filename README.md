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

 **Salida:**
   - Combinaciones posibles de tropas según el presupuesto.
   - Permutaciones posibles del orden de ataque a los territorios.
   - Representación del tablero con información sobre cada territorio.


## Bonus
 **Aumentar complejidad:**
   - Restricción: El programa puede priorizar atacar territorios más débiles en las permutaciones del orden de ataque.
 **Estrategias específicas:**
   - El programa permite configurar las tropas para diferentes tipos de territorios (por ejemplo, usar más caballería en terrenos planos).
 **Optimización:**
   - Calcula la combinación de tropas y el orden de ataque que maximiza las conquistas con los recursos disponibles.
