import unittest
from input import parse_file
from graph import Graph
from path import Path

class testGraph(unittest.TestCase):

    # Pour chaque graphe, s'assurer qu'on a le bon nombre d'aretes et de sommets
    def tests_hardToChose_graph(self):
        vertices, edges = parse_file("../in/hard_to_choose.txt")
        self.assertEqual(35,len(vertices))
        self.assertEqual(595,len(edges))

    def tests_islands_graph(self):
        vertices, edges = parse_file("../in/islands.txt")
        self.assertEqual(60, len(vertices))
        self.assertEqual(760, len(edges))

    def tests_paris_map_graph(self):
        vertices, edges = parse_file("../in/paris_map.txt")
        self.assertEqual(11348, len(vertices))
        self.assertEqual(17958, len(edges))

    # Pour chaque graphe, s'assurer que le chemin obtenu est sup ou egal a la somme des poids des aretes, et inferieur au double de cette somme
    def tests_hardToChose_path(self):
        vertices, edges = parse_file("../in/hard_to_choose.txt")
        graph = Graph(vertices, edges)
        path = Path(graph)
        print(graph.sum_weight_edges())
        self.assertGreaterEqual(path.weight,graph.sum_weight_edges())
        self.assertLess(path.weight, 2*graph.sum_weight_edges())

    def tests_islands_path(self):
        vertices, edges = parse_file("../in/islands.txt")
        graph = Graph(vertices, edges)
        path = Path(graph)
        self.assertGreaterEqual(path.weight,graph.sum_weight_edges())
        self.assertLess(path.weight, 2 * graph.sum_weight_edges())

    def tests_paris_map_path(self):
        vertices, edges = parse_file("../in/paris_map.txt")
        graph = Graph(vertices, edges)
        path = Path(graph)
        self.assertGreaterEqual(path.weight,graph.sum_weight_edges())
        self.assertLess(path.weight, 2 * graph.sum_weight_edges())

