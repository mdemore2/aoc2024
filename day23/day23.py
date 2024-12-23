import networkx as nx


def parse_input(filename: str) -> list:
    edges = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            edge = tuple(line.strip().split('-'))
            # print(edge)
            edges.append(edge)
            line = f.readline()
    return edges


def analyze_graph(edges: list) -> int:
    graph = nx.Graph()
    graph.add_edges_from(edges)
    sets_of_3 = []
    print(list(graph.degree()))
    for clique in nx.enumerate_all_cliques(graph):
        if len(clique) == 3:
            print('clique size 3')
            sets_of_3.append(set(list(clique)))
    return len(sets_of_3)
