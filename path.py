from graph import Graph
import path_computing


# TODO: encapsulation avec des getters, ce serait plus propre
class Path:
    def __init__(self, graph: Graph):
        """
        Parameters
        ----------
        graph : Graph
            Graph we need to compute the best path in
        """

        # liste des sommets parcourus dans le bon ordre
        self.vertex_list = []
        # poids total
        self.weight = 0
        # calcul du chemin en suivant l'algo defini dans path_computing.py
        self.compute_path(graph)

    # Algo general du calcul de chemin
    def compute_path(self,graph):
        unvisited_edges = graph.get_edges().copy()
        visited_vertices = {}
        visited_vertices["completed"] = []
        visited_vertices["uncompleted"] = []
        # Initialisation. TODO: une initialisation aleatoire serait interessante
        # TODO: une suite d'initialisations aleatoires aussi, 5 p.ex, ou on selectionne le meilleur point de depart
        visited_vertices["uncompleted"].append(0)
        self.weight = path_computing.make_loops(visited_vertices,unvisited_edges,graph,0)
        #TODO: vertex_list


    # Affichage du chemin
    def visual(self):
        visual_string = ""
        for v in self.vertex_list:
            if visual_string:
                visual_string+="->"
            visual_string+=v
        return visual_string+" (weight: "+str(self.weight)+")"



















