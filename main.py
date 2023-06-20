import heapq
from heapq import *
with open('./entrada.txt', 'r') as archivo:
    cantidad_nodos, cantidad_aristas = map(int, archivo.readline().split())
    G= [[] for _ in range(cantidad_nodos+5)]
    for i in range(cantidad_aristas):
        a, b, c ,d = archivo.readline().split()
        a, b, c = int(a), int(b), int(c)
        G[a].append(((b, c), d))
        G[b].append(((a, c), d))

diccionarioNombres = {}
with open('./nombres.txt', 'r') as archivo2:
    cantidad_nombres= int(archivo2.readline())
    for _ in range(cantidad_nombres):
        valores = archivo2.readline().split()
        texto = valores[0]
        n = int(valores[1])
        numeros = list (map(int, valores[2:]))
        diccionarioNombres[texto] = (n, numeros)

def dijsktra(nombreInicio,nombreDestino):
    inicio = diccionarioNombres[nombreInicio][1][0]
    listaPosiblesDestinos = diccionarioNombres[nombreDestino][1]
    destino = diccionarioNombres[nombreDestino][1][0]

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
    for i in range(len(listaPosiblesDestinos)):
        if distancia[listaPosiblesDestinos[i]] < distancia[destino]:
            destino = listaPosiblesDestinos[i]
    nodo = destino
    caminoNodos = []
    while nodo!=inicio:
        caminoNodos.append(nodo)
        path.append((nombreCalle[nodo], distanciaRecorrida[nodo]))
        nodo = padre[nodo]
    caminoNodos.append(inicio)
    caminoNodos.reverse()
    path.reverse()
    return ((distancia[destino], path),caminoNodos)


def agenteBasadoEnObjetivos(origen,destino):
    ((distancia,camino),caminoNodos)=dijsktra(origen,destino)
    print("nodos en el camino mas corto: ", caminoNodos)
    print("la distancia mas corta es:", distancia)
    hora=distancia*6//3600
    minuto=(distancia*6%3600)//60
    segundo=(distancia*6%3600)%60
    print("el tiempo estimado para recorrer es: ", hora, " horas ", minuto, " minutos ", segundo, " segundos")
    print("el camino mas corto es: ", camino)


print("efe nomas", diccionarioNombres["Hipermaxi"])
agenteBasadoEnObjetivos("OVERTIME","BANCO_UNION")