import heapq
with open('entrada.txt', 'r') as archivo:
    cantidad_nodos, cantidad_aristas = map(int, archivo.readline().split())
    G= [[] for _ in range(cantidad_nodos+5)]
    for i in range(cantidad_aristas):
        a, b, c = map(int, archivo.readline().split())
        G[a].append((b,c))


def dijsktra(nodo):
    distancia = [float('inf') for _ in range(cantidad_nodos+5)]
    distancia[nodo] = 0
    cola = [(0, nodo)]
    while cola:
        dist, nodo = heapq.heappop(cola)
        if distancia[nodo] < dist:
            continue
        for vecino, peso in G[nodo]:
            if dist + peso < distancia[vecino]:
                distancia[vecino] = dist + peso
                heapq.heappush(cola, (distancia[vecino], vecino))
    return distancia

res=dijsktra(1)
for i in range(1, cantidad_nodos+1):
    print(i," ",res[i])