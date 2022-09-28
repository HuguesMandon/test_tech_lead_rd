#######################################################################################
################################# REFLEXIONS ##########################################
#######################################################################################

# Sans avoir le temps de le verifier, j'ai l'intuition que le probleme est NP
# Par consequent, je me concentre sur une heuristique pour avoir "la meilleure solution possible en un temps acceptable"
# plutot que d'essayer de trouver toutes les solutions possibles et ensuite les comparer (surtout que le dernier graphe est gros)

# But 1 : parcourir toutes les aretes
# But 2 : avoir un poids minimum

# Algo simple : on part d'un sommet au hasard, on parcourt le graphe aleatoirement en gardant une liste des aretes non parcourues,
# quand on est bloques on va trouver la prochaine arrete en continuant de parcourir le graphe

# A vu de nez, c'est possible d'avoir quelque chose de bien plus performant, mais comment ?
# Si un sommet a 1 arete, c'est pas top, idealement on aimerait commencer ou finir par lui
# Si un sommet a 2 aretes, on ne fait que passer (donc on aimerait ne pas commencer ou finir par lui)
# Si un sommet a >2 aretes, c'est probable que boucler tres vite pour revenir sur lui soit favorable => En pratique, complique a faire, necessaire de connaitre les boucles
# Associer a chaque sommet ses aretes ?

# Idee 2 d'algo :
# 1- A chaque sommet on associe ses aretes (fait dans graph.py)
# 2- On part d'un sommet au hasard avec un nombre impair d'aretes, de preference faible
# L1- On considere toutes les aretes sortantes et les sommets associes
# L2- Soit (1) on prend l'arete la plus faible non visitee, soit (2) on prend l'arete la plus faible vers un sommet visite non complete, soit (3) on prend l'arete la plus faible vers un sommet non visite
# Vraiment besoin de distinction 2 / 3 ?
# 2 listes (ou autres structures) à avoir : arretes non visitees et sommets visites non completes

# Rafinement d'algo 2, s'inspirant d'Hierholzer :
# Au lieu de boucler L1-L2 en repartant du dernier sommet, on s'autorise a repartir de n'importe quel sommet visite non complete, mais on s'assure de bien revenir dessus
# (ou sur un autre sommet visite)

#######################################################################################
#################################### CODE #############################################
#######################################################################################

from graph import Graph

# Boucle principale de recherche de chemin
def explore(visited_vertices, unvisited_edges, graph, v):
    if v in visited_vertices["uncompleted"]:
        for e in graph.edges_of_vertex[v]:
            if e in unvisited_edges:
                unvisited_edges.remove(e)
                second_vertex = Graph.get_vertices_of_edge(e)[1]
                add_vertex_to_visited(second_vertex,visited_vertices,graph,unvisited_edges)
                return e
    else:
        # v is in visited_vertices["completed"]:
        for e in graph.get_edges_of_vertex(v):
            second_vertex = Graph.get_vertices_of_edge(e)[1]
            if second_vertex not in visited_vertices["completed"]:  # impossible qu'il soit dans uncompleted, il est vide
                add_vertex_to_visited(second_vertex,visited_vertices,graph,unvisited_edges)
                return e
    return None

# fonction qui explore tout le graphe en faisant des boucles
# TODO: bug sur les plus gros graphes, je pense qu'il me manque des cas mais pas eu le temps de me poser
def make_loops(visited_vertices, unvisited_edges, graph, curr_vertex):
    total_weight = 0
    visited_edge = explore(visited_vertices, unvisited_edges, graph, curr_vertex)
    new_vertex = graph.get_vertices_of_edge(visited_edge)[1]
    total_weight = graph.get_edge_weight(visited_edge)
    while new_vertex != curr_vertex and visited_edge!= None:
        visited_edge = explore(visited_vertices, unvisited_edges, graph, new_vertex)
        if visited_edge!=None:
            new_vertex = graph.get_vertices_of_edge(visited_edge)[1]
            total_weight += graph.get_edge_weight(visited_edge)
    if unvisited_edges:
        if visited_vertices["uncompleted"]:
            return total_weight+make_loops(visited_vertices, unvisited_edges, graph,visited_vertices["uncompleted"][0])
        else:
            for v in visited_vertices["completed"]:
                visited_edge = explore(visited_vertices, unvisited_edges, graph, v)
                if visited_edge:
                    return total_weight+make_loops(visited_vertices, unvisited_edges, graph,graph.get_vertices_of_edge(visited_edge)[1])

    else:
        return total_weight

# Todo: backtracking, retrouver le chemin a partir des calculs


# On cherche a ajouter un nouveau sommet aux sommets visites
def add_vertex_to_visited(vertex,visited_vertices,graph,unvisited_edges):
    # Si deja visite, on verifie si on l'a complete ou pas
    if vertex in visited_vertices["uncompleted"]:
        all_edges_visited = True
        for e in graph.get_edges_of_vertex(vertex):
            if e in unvisited_edges:
                all_edges_visited=False
                break
        if all_edges_visited:
            visited_vertices["uncompleted"].remove(vertex)
            visited_vertices["completed"].append(vertex)
    # Si jamais visite, on verifie si on l'a complete ou pas
    if vertex not in visited_vertices["completed"]:
        if len(graph.edges_of_vertex)==1:
            visited_vertices["completed"].append(vertex)
        else:
            visited_vertices["uncompleted"].append(vertex)
    # Si deja complete, rien a faire