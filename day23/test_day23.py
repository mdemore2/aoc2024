from day23 import parse_input, analyze_graph


def test_example():
    edges = parse_input('example_input.txt')
    assert analyze_graph(edges) == 12
