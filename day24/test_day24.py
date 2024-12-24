from day24 import parse_input, route, calculate_number


def test_tiny_example():
    start_values, connections = parse_input('tiny_example_input.txt')
    print(start_values)
    print(connections)
    values = route(start_values, connections)
    assert calculate_number(values) == 4
