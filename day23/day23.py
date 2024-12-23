import networkx as nx


def parse_input(filename: str) -> list:
    edges = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            edge = tuple(line.strip().split('-'))
            edges.append(edge)
            line = f.readline()
    return edges


def analyze_graph(edges: list) -> int:
    graph = nx.Graph()
    graph.add_edges_from(edges)
    sets_of_3t = []
    for clique in nx.enumerate_all_cliques(graph):
        if len(clique) == 3:
            if any(node.startswith('t') for node in list(clique)):
                sets_of_3t.append(set(list(clique)))
    return len(sets_of_3t)


def get_password(edges: list) -> str:
    graph = nx.Graph()
    graph.add_edges_from(edges)
    cliques = list(nx.enumerate_all_cliques(graph))
    cliques.sort(key=len)
    max_clique = sorted(cliques[-1])
    return ",".join(max_clique)
