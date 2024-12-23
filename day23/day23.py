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
    sets_of_3t = []
    print(list(graph.degree()))
    for clique in nx.enumerate_all_cliques(graph):
        if len(clique) == 3:
            print('clique size 3')
            if any('t' in node for node in list(clique)):
                sets_of_3t.append(set(list(clique)))
    return len(sets_of_3t)
