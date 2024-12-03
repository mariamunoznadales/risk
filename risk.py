from itertools import permutations

# Generar combinaciones de tropas respetando los recursos disponibles
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
    print(f"Combinaciones generadas: {combinaciones}")  # Depuración
    return combinaciones


# Generar permutaciones del orden de ataque, con opción de atacar primero los más débiles
def generar_permutaciones(cantidad_territorios, defensas, restricciones=None):
    permutaciones = list(permutations(range(cantidad_territorios)))
    if restricciones == "territorios_mas_debiles":
        permutaciones.sort(key=lambda perm: sum([defensas[territorio] for territorio in perm]))
    return permutaciones

# Evaluar combinación según restricciones de tropas y territorios
def evaluar_combinacion(combinacion, permutacion, defensas, tropas):
    fuerza_total = sum(combinacion[tipo] * tropas[tipo]["fuerza"] for tipo in tropas)
    print(f"Fuerza total de la combinación {combinacion}: {fuerza_total}")  # Depuración
    conquistas = 0
    for idx in permutacion:
        print(f"Evaluando contra la defensa del territorio {idx + 1}: {defensas[idx]}")  # Depuración
        if fuerza_total >= defensas[idx]:
            fuerza_total -= defensas[idx]
            conquistas += 1
        else:
            print(f"No se puede conquistar el territorio {idx + 1}")  # Depuración
            break
    return conquistas


# Optimizar estrategias, eligiendo la combinación de tropas que maximiza las conquistas

def optimizar_estrategia(max_puntos, defensas, tropas):
    combinaciones = generar_combinaciones(max_puntos, tropas)
    print(f"\nCombinaciones de tropas generadas: {combinaciones}")  # depuración
    permutaciones = generar_permutaciones(len(defensas), defensas, restricciones="territorios_mas_debiles")
    print(f"Permutaciones generadas: {permutaciones}")  # depuración
    mejor_estrategia = {"conquistas": 0, "combinacion": {}, "permutacion": []}

    for combinacion in combinaciones:
        for permutacion in permutaciones:
            conquistas = evaluar_combinacion(combinacion, permutacion, defensas, tropas)
            print(f"Evaluando combinacion: {combinacion} con permutacion: {permutacion} -> conquistas: {conquistas}")  # Depuración
            if conquistas > mejor_estrategia["conquistas"]:
                mejor_estrategia = {"conquistas": conquistas, "combinacion": combinacion, "permutacion": permutacion}

    return mejor_estrategia


# Representar el tablero con los territorios y su defensa
def representar_tablero(defensas):
    tablero = [{"territorio": i + 1, "defensa": defensa} for i, defensa in enumerate(defensas)]
    return tablero

# Entrada dinámica de datos
def entrada_datos():
    max_puntos = int(input("Introduce el máximo de puntos disponibles para tropas: "))
    cantidad_territorios = int(input("Introduce el número de territorios enemigos: "))
    defensas = []
    for i in range(cantidad_territorios):
        defensa = int(input(f"Introduce la fuerza de defensa del Territorio {i + 1}: "))
        defensas.append(defensa)
    
    tropas = {}
    for tipo in ["Infantería", "Caballería", "Artillería"]:
        fuerza = int(input(f"Fuerza de {tipo}: "))
        costo = int(input(f"Costo de {tipo}: "))
        while costo <= 0:
            print("El costo debe ser mayor que 0.")
            costo = int(input(f"Costo de {tipo}: "))
        tropas[tipo] = {"fuerza": fuerza, "costo": costo}
    
    return max_puntos, defensas, tropas

# Ejecutar el programa
def main():
    print("Planificador de Ataque para Risk")
    max_puntos, defensas, tropas = entrada_datos()
    
    # Representar el tablero
    tablero = representar_tablero(defensas)
    print("\nTablero representado:")
    for territorio in tablero:
        print(territorio)

    # Generar combinaciones de tropas
    combinaciones = generar_combinaciones(max_puntos, tropas)
    print(f"\nCombinaciones posibles de tropas ({len(combinaciones)} encontradas):")
    for combinacion in combinaciones:
        print(combinacion)

    # Generar permutaciones del orden de ataque
    permutaciones = generar_permutaciones(len(defensas), defensas, restricciones="territorios_mas_debiles")
    print(f"\nPermutaciones posibles del orden de ataque ({len(permutaciones)} encontradas):")
    for perm in permutaciones:
        print(perm)

    # Optimizar estrategia
    mejor_estrategia = optimizar_estrategia(max_puntos, defensas, tropas)
    print("\nMejor estrategia optimizada:")
    print(f"- Conquistas logradas: {mejor_estrategia['conquistas']}")
    print(f"- Combinación de tropas: {mejor_estrategia['combinacion']}")
    print(f"- Orden de ataque: {mejor_estrategia['permutacion']}")

if __name__ == "__main__":
    main()
