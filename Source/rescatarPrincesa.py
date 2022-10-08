import networkx as nx
import matplotlib.pyplot as plt

##Creo El Grafo
def crearGrafo(vertices, aristas):
    myGrafo = nx.DiGraph()
    myGrafo.add_nodes_from(vertices)
    myGrafo.add_weighted_edges_from(aristas)
    print('Vertices del Grafo:\n', myGrafo.nodes, '\nAristas:\n', aristas)
    return myGrafo


##Me quedo solo con los nodos que me sirven para resolver el caso.
def grafoDijkstra(myGrafo, fuente, sumidero):
    myGrafoDijkstra = nx.dijkstra_path(myGrafo, fuente, sumidero)
    print('Camino mas Corto:\n', myGrafoDijkstra)
    return myGrafoDijkstra

##Elimino todos los nodos que no estan incluidos en el camino de Dijkstra
def eliminarVertices(myGrafoDijkstra, myGrafo, dragones):
    #tengo que utilizar set para poder comparar los elementos de la lista
    verticesNoIncluidos = set(myGrafo.nodes)
    for element in myGrafoDijkstra:
        if element in verticesNoIncluidos:
            verticesNoIncluidos.remove(element)

    verticesNoIncluidos = list(verticesNoIncluidos)

    for j in dragones:
        verticesNoIncluidos.append(j)
    for i in verticesNoIncluidos:
        if myGrafo.has_node(i):
            myGrafo.remove_node(i)

    return myGrafo


##Mostrar El Grafo por Pantalla.
def mostrarCaminoFinal(myGrafo):
    nx.draw(myGrafo, pos=nx.circular_layout(myGrafo), node_color='y', edge_color='g', with_labels=True)
    plt.show()


##Leo el Archivo y creo los vertices/aristas
def leerArchivo(archivo):
    with open(archivo, 'r') as f:
        fContenido = f.readlines()

    vertices = []
    for i in range(int(fContenido[0][0])):
        vertices.append(str(i+1))

    posicionPrincesa = fContenido[1][0]
    posicionPrincipe = fContenido[1][2]

    ##Conversiones de listas y manejo de str para poder tomar individualmente cada valor de dragon.
    dragones = []
    dragon = fContenido[2].splitlines()
    dragon = dragon[0].split()
    for x in dragon:
        dragones.append(x)

    aristasRaw = fContenido[3:len(fContenido)]
    aristas = []
    ##Cada valor de arista estaba como un unico str, con esto lo spliteo, le remuevo el '\n' y lo transformo en matriz
    ##Asi lo puede tomar luego el metodo add_weighted_edges_from()
    for i in aristasRaw:
        valorArista = i.split()
        aristas.append([valorArista[0], valorArista[1], int(valorArista[2])])

    ##Remuevo Nodos que se generaron sin vertice.
    setVertices = set(vertices)
    for i in setVertices:
        if i not in aristas[0] or i not in aristas[1]:
            vertices.remove(i)

    return vertices, posicionPrincesa, posicionPrincipe, aristas, dragones


def Resolver(archivo):
    vertices, posicionPrincesa, posicionPrincipe, aristas, dragones = leerArchivo(archivo)

    miGrafo = crearGrafo(vertices, aristas)

    mostrarCaminoFinal(miGrafo)

    miGrafoDijkstra = grafoDijkstra(miGrafo, posicionPrincipe, posicionPrincesa)

    miGrafo = eliminarVertices(miGrafoDijkstra, miGrafo, dragones)

    mostrarCaminoFinal(miGrafo)


##La ruta por defecto es la misma en la que se encuentra el archivo .py
##Si los casos de prueba se encuentran en el mismo directorio que myGrafos.py solo poner el nombre \
##de el caso de prueba como parametro en Resolver('casoDePrueba.txt')

#Resolver('caso1.txt')
#Resolver('caso2.txt')
#Resolver('caso3.txt')
#Resolver('caso4.txt')