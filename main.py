import heapq
from heapq import *
with open('entrada.txt', 'r') as archivo:
    cantidad_nodos, cantidad_aristas = map(int, archivo.readline().split())
    G= [[] for _ in range(cantidad_nodos+5)]
    for i in range(cantidad_aristas):
        a, b, c ,d = archivo.readline().split()
        a, b, c = int(a), int(b), int(c)
        G[a].append(((b, c), d))
        G[b].append(((a, c), d))

diccionarioNombres = {}
with open('nombres.txt', 'r') as archivo2:
    cantidad_nombres= int(archivo2.readline())
    for _ in range(cantidad_nombres):
        valores = archivo2.readline().split()
        texto = valores[0]
        n = int(valores[1])
        numeros = list (map(int, valores[2:]))
        diccionarioNombres[texto] = (n, numeros)

def dijsktra(nombreInicio,nombreDestino):
    inicio = diccionarioNombres[nombreInicio][1][0]
    destino = diccionarioNombres[nombreDestino][1][0]

    print("inicio: ",inicio,"destino: ",destino)
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
            #print ("nodo: ",nodo,"vecino: ",vecino,"peso: ",peso,"nombreCalle: ",nombreCalle[vecino])
            if distancia[nodo] + peso < distancia[vecino]:
                distancia[vecino] = distancia[nodo] + peso
                padre[vecino] = nodo
                nombreCalle[vecino] = adyacente[1]
                distanciaRecorrida[vecino] = peso
                heappush(cola, (distancia[vecino], vecino))
    
    path = []
    nodo = destino
    while nodo!=inicio:
        print("nodo  ",nodo)
        path.append((nombreCalle[nodo], distanciaRecorrida[nodo]))
        nodo = padre[nodo]
    print("nodo  ",nodo)
    path.reverse()
    return (distancia[destino], path)


dis1, path1 = dijsktra("OVERTIME","SUPERMARKET")

print("la distancia mas corta es:", dis1)
#el tiempo en segundos es 6 segundos por cada metro, quiero pasarlo a horas, minutos y segundo
hora = dis1*6//3600
minuto = (dis1*6%3600)//60
segundo = (dis1*6%3600)%60
print("el tiempo estimado para recorrer es: ", hora, " horas ", minuto, " minutos ", segundo, " segundos")
#print("el tiempo estimado para recorrer es: ", dis1*6, " segundos")
print("el camino mas corto es: ", path1)
