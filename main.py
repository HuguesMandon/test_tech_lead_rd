from input import parse_cmd_line, parse_file
from graph import Graph
from path import Path


def main():
    in_file, plot_graph = parse_cmd_line()
    vertices, edges = parse_file(in_file)
    print(f"#E={len(edges)}, #V={len(vertices)}")
    graph = Graph(vertices, edges)
    path = Path(graph)
    print(path.visual())
    if plot_graph:
        graph.plot()


if __name__ == "__main__":
    main()
