import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.somma=0
        self.borghi=DAO.getBorghi()
        self.grafo = nx.Graph()

    def creaGrafo(self, borgo):
        self.nodi=DAO.getNodi(borgo)
        self.grafo.add_nodes_from(self.nodi)
        self.addEdges()

        return self.grafo

    def addEdges(self):
         self.grafo.clear_edges()
         for nodo1 in self.grafo.nodes:
             for nodo2 in self.grafo.nodes:
                 if nodo1!=nodo2 and self.grafo.has_edge(nodo1, nodo2) == False:
                     peso=DAO.getPeso(nodo1,nodo2)
                     if peso>0:
                         self.somma+=peso
                         self.grafo.add_edge(nodo1, nodo2, weight=peso)

    def getNumNodes(self):
        return len(self.grafo.nodes)

    def getNumEdges(self):
        return len(self.grafo.edges)
    def analisi(self):
        lista=[]
        pesoMedio=self.somma/len(self.grafo.edges)
        for arco in self.grafo.edges:
            if self.grafo[arco[0]][arco[1]]["weight"]>pesoMedio:
                lista.append((arco[0],arco[1],self.grafo[arco[0]][arco[1]]["weight"]))
        listaOrdinata=sorted(lista, key=lambda x:x[2],reverse=True)
        return listaOrdinata, round(pesoMedio,3)
