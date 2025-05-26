import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._allNodi = []
        self._idMapAlbum = {}

    def buildGraph(self, durataMin):
        self._allNodi = DAO.getAlbums(durataMin)
        self._graph.add_nodes_from(self._allNodi)
        self._idMapAlbum = {n.AlbumId: n for n in self._allNodi}
        self._allEdges = DAO.getAllEdges(self._idMapAlbum)
        self._graph.add_edges_from(self._allEdges)


    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()
