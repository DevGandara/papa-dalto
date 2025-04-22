# ================================================================
# Autor: David Ivan Gándara Vázquez
# Materia: Teoria de la Complejidad Computacional
# Fecha: 08/04/2025
# Descripción: Implementación del algoritmo glotón (greedy) para resolver una instancia del Problema del Viajante (TSP).
# ================================================================

def tsp_greedy(distancias, inicio=0):
    # Inicializacion de recursos
    n = len(distancias)
    visitadas = [False] * n
    ruta = [inicio]
    actual = inicio
    visitadas[actual] = True
    distancia_total = 0

    for _ in range(n - 1): #Para visitar todas las ciudades
        siguiente = None
        menor_dist = float('inf') # Inicializa la menor distancia con infinito

        # Busca la ciudad no visitada mas cercana
        for ciudad in range(n):
            if not visitadas[ciudad] and distancias[actual][ciudad] < menor_dist:
                menor_dist = distancias[actual][ciudad]
                siguiente = ciudad
        
        ruta.append(siguiente)
        distancia_total += menor_dist
        visitadas[siguiente] = True
        actual = siguiente
    
    #Regresa a la ciudad del inicio para cerrar el ciclo
    distancia_total += distancias[actual][inicio]
    ruta.append(inicio)

    return ruta, distancia_total


# Matriz de distancias entre 4 ciudades
distancias = [
    [0, 8 , 13, 25],
    [8, 0, 35, 32 ],
    [13, 35, 0, 40],
    [25, 32, 40, 0]
]

#Ejecuta el algoritmo
ruta, distancia = tsp_greedy(distancias)

# Muestra los resultados
print("Ruta encontrada (glotón):", ruta)
print("Distancia total:", distancia)