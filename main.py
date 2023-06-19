import heapq
from heapq import *
with open('entrada.txt', 'r') as archivo:
    cantidad_nodos, cantidad_aristas = map(int, archivo.readline().split())
    G= [[] for _ in range(cantidad_nodos+5)]
    for i in range(cantidad_aristas):
        #d is a string
        a, b, c ,d = archivo.readline().split()
        a, b, c = int(a), int(b), int(c)
        #i also wanna append d in the adyacence list
        G[a].append(((b, c), d))



def dijsktra(inicio,destino):
    distancia = [float('inf') for _ in range(cantidad_nodos+5)]
    distancia[inicio] = 0
    
    padre = [None for _ in range(cantidad_nodos+5)]
    nombreCalle = [None for _ in range(cantidad_nodos+5)]
    distanciaRecorrida = [None for _ in range(cantidad_nodos+5)]
    vis = [False for _ in range(cantidad_nodos+5)]

    cola = []
    heapify(cola)
    heappush(cola, (0, inicio))
    while len(cola):
        _,nodo = heappop(cola)
        if vis[nodo]:
            continue
        vis[nodo] = True
        for adyacente in G[nodo]:
            vecino, peso = adyacente[0]
            nombreCalle[vecino] = adyacente[1]
            distanciaRecorrida[vecino] = peso
            #print ("nodo: ",nodo,"vecino: ",vecino,"peso: ",peso,"nombreCalle: ",nombreCalle[vecino])
            if distancia[nodo] + peso < distancia[vecino]:
                distancia[vecino] = distancia[nodo] + peso
                padre[vecino] = nodo
                heappush(cola, (distancia[vecino], vecino))
    #print("la distancia mas corta es:", distancia[destino])
    #print("el tiempo estimado para recorrer es: ", distancia[destino]*6, " segundos")
    
    path = []
    nodo = destino
    while nodo!=inicio:
        #solo quiero los nombres y la distancia recorrida
        path.append((nombreCalle[nodo], distanciaRecorrida[nodo]))
        nodo = padre[nodo]
    path.reverse()
    #print("el camino mas corto es: ", path)
    return (distancia[destino], path)


dis1, path1 = dijsktra(1, 3)
print("la distancia mas corta es:", dis1)
print("el tiempo estimado para recorrer es: ", dis1*6, " segundos")
print("el camino mas corto es: ", path1)

