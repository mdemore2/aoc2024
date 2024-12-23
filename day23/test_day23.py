from day23 import parse_input, analyze_graph, get_password


def test_example():
    edges = parse_input('example_input.txt')
    assert analyze_graph(edges) == 7


def test_part1():
    edges = parse_input('input.txt')
    print(analyze_graph(edges))
    assert False


def test_example_part2():
    edges = parse_input('example_input.txt')
    assert get_password(edges) == 'co,de,ka,ta'


def test_part2():
    edges = parse_input('input.txt')
    print(get_password(edges))
    assert False
