from __future__ import annotations
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


class Graph:
    def __init__(self, vertices: list[tuple], edges: list[tuple]):
        """
        Parameters
        ----------
        vertices : list[tuple]
            list of vertices coordinates.
        edges : list[tuple]
            list of edges as tuple (id 1, id 2, weight, coordinates 1, coordinates 2).
        """
        self.vertices = vertices
        self.edges = edges
        # Hash des aretes sortant d'un sommet
        self.edges_of_vertex = {}
        for e in edges:
            #hasattr isn't working correctly,so we use try except
            try:
                self.edges_of_vertex[e[0]].append(e)
            except:
                self.edges_of_vertex[e[0]] = [e]
            try:
                self.edges_of_vertex[e[1]].append(e)
            except:
                self.edges_of_vertex[e[1]] = [e]

            #if not hasattr(self.edges_of_vertex,str(e[0])):
            #    self.edges_of_vertex[e[0]] = []
            #if e not in self.edges_of_vertex[e[0]]:
            #    self.edges_of_vertex[e[0]].append(e)
            #if not hasattr(self.edges_of_vertex,str(e[1])):
            #    self.edges_of_vertex[e[1]] = []
            #if e not in self.edges_of_vertex[e[1]]:
            #    self.edges_of_vertex[e[1]].append(e)

    def get_edges_of_vertex(self,vertex):
        return self.edges_of_vertex[vertex]

    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    @staticmethod
    def get_vertices_of_edge(edge):
        return (edge[0],edge[1])

    @staticmethod
    def get_edge_weight(edge):
        return edge[2]

    def sum_weight_edges(self):
        """
        Returns
        -------
        Sum of the edges weights
        """
        sum = 0
        for e in self.edges:
            sum+=e[2]
        return sum

    def plot(self):
        """
        Plot the graph.
        """
        weights = list(set(edge[2] for edge in self.edges))
        colors = plt.cm.get_cmap("viridis", len(weights))
        _, ax = plt.subplots()
        for i, weight in enumerate(weights):
            lines = [[edge[-2][::-1], edge[-1][::-1]] for edge in self.edges if edge[2] == weight]
            ax.add_collection(LineCollection(lines, colors=colors(i), alpha=0.7, label=f"weight {weight}"))
        ax.plot()
        ax.legend()
        plt.title(f"#E={len(self.edges)}, #V={len(self.vertices)}")
        plt.show()
