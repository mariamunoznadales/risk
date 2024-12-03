from itertools import permutations

# Generar combinaciones de tropas
def generar_combinaciones(max_puntos, tropas):
    combinaciones = []
    for inf in range(1, max_puntos + 1):  # Al menos 1 infantería
        for cab in range(1, max_puntos // tropas["Caballería"]["costo"] + 1):  # Al menos 1 caballería
            for art in range(1, max_puntos // tropas["Artillería"]["costo"] + 1):  # Al menos 1 artillería
                costo_total = (
                    inf * tropas["Infantería"]["costo"] +
                    cab * tropas["Caballería"]["costo"] +
                    art * tropas["Artillería"]["costo"]
                )
                if costo_total <= max_puntos:
                    combinaciones.append({"Infantería": inf, "Caballería": cab, "Artillería": art})
    return combinaciones

# Generar permutaciones priorizando territorios más débiles
def generar_permutaciones_prioritarias(defensas):
    defensas_ordenadas = sorted(enumerate(defensas), key=lambda x: x[1])  # Ordenar por defensa
    indices_ordenados = [indice for indice, _ in defensas_ordenadas]
    return list(permutations(indices_ordenados))

# Representar el tablero
def representar_tablero(defensas, tipos_territorio):
    tablero = [{"territorio": i + 1, "defensa": defensa, "tipo": tipo}
               for i, (defensa, tipo) in enumerate(zip(defensas, tipos_territorio))]
    return tablero

# Calcular conquistas con una combinación y un orden específico
def calcular_conquistas(tablero, combinacion, tropas):
    conquistas = 0
    tropas_restantes = combinacion.copy()
    for territorio in tablero:
        tipo = territorio["tipo"]
        defensa = territorio["defensa"]
        
        if tipo == "plano":
            fuerza = tropas_restantes["Caballería"] * tropas["Caballería"]["fuerza"]
        elif tipo == "montañoso":
            fuerza = tropas_restantes["Artillería"] * tropas["Artillería"]["fuerza"]
        else:
            fuerza = tropas_restantes["Infantería"] * tropas["Infantería"]["fuerza"]

        if fuerza >= defensa:
            conquistas += 1
            tropas_restantes = {t: max(0, tropas_restantes[t] - defensa // tropas[t]["fuerza"])
                                for t in tropas_restantes}
    return conquistas

# Optimizar conquistas
def optimizar_conquistas(tablero, combinaciones, tropas):
    mejor_combinacion = None
    mejor_orden = None
    max_conquistas = 0
    
    for combinacion in combinaciones:
        for permutacion in generar_permutaciones_prioritarias([t["defensa"] for t in tablero]):
            tablero_ordenado = [tablero[i] for i in permutacion]
            conquistas = calcular_conquistas(tablero_ordenado, combinacion, tropas)
            if conquistas > max_conquistas:
                max_conquistas = conquistas
                mejor_combinacion = combinacion
                mejor_orden = permutacion
    
    return mejor_combinacion, mejor_orden, max_conquistas

# Entrada de datos dinámica
def entrada_datos():
    max_puntos = int(input("Introduce el máximo de puntos disponibles para tropas: "))
    cantidad_territorios = int(input("Introduce el número de territorios enemigos: "))
    defensas = []
    tipos_territorio = []
    for i in range(cantidad_territorios):
        defensa = int(input(f"Introduce la fuerza de defensa del Territorio {i + 1}: "))
        tipo = input(f"Introduce el tipo del Territorio {i + 1} (plano/montañoso/otro): ")
        defensas.append(defensa)
        tipos_territorio.append(tipo)
    tropas = {
        "Infantería": {"fuerza": int(input("Fuerza de Infantería: ")), "costo": int(input("Costo de Infantería: "))},
        "Caballería": {"fuerza": int(input("Fuerza de Caballería: ")), "costo": int(input("Costo de Caballería: "))},
        "Artillería": {"fuerza": int(input("Fuerza de Artillería: ")), "costo": int(input("Costo de Artillería: "))},
    }
    return max_puntos, defensas, tipos_territorio, tropas

# Ejecutar programa
def main():
    print("Bienvenido al planificador de ataques de Risk.")
    max_puntos, defensas, tipos_territorio, tropas = entrada_datos()
    
    # Generar combinaciones de tropas
    combinaciones = generar_combinaciones(max_puntos, tropas)
    print(f"\nCombinaciones posibles de tropas ({len(combinaciones)} encontradas):")
    for combinacion in combinaciones:
        print(combinacion)

    # Representar el tablero
    tablero = representar_tablero(defensas, tipos_territorio)
    print("\nTablero representado:")
    for territorio in tablero:
        print(territorio)

    # Optimizar conquistas
    mejor_combinacion, mejor_orden, max_conquistas = optimizar_conquistas(tablero, combinaciones, tropas)
    print("\nMejor estrategia encontrada:")
    print(f"Combinación de tropas: {mejor_combinacion}")
    print(f"Orden de ataque: {mejor_orden}")
    print(f"Máximo de conquistas: {max_conquistas}")

if __name__ == "__main__":
    main()
