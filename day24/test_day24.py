from day24 import parse_input, calculate_number, recursive_route
from day24 import logical_xor, logical_and, logical_or
from day24 import find_bad_bits


def test_xor():
    assert logical_xor(1, 1) == 0
    assert logical_xor(0, 1) == 1
    assert logical_xor(1, 0) == 1
    assert logical_xor(0, 0) == 0


def test_and():
    assert logical_and(1, 1) == 1
    assert logical_and(0, 1) == 0
    assert logical_and(0, 1) == 0
    assert logical_and(0, 0) == 0


def test_or():
    assert logical_or(1, 1) == 1
    assert logical_or(0, 1) == 1
    assert logical_or(0, 1) == 1
    assert logical_or(0, 0) == 0


def test_tiny_example():
    start_values, connections = parse_input('tiny_example_input.txt')
    print(start_values)
    print(connections)
    values = recursive_route(start_values, connections)
    assert calculate_number(values) == 4


def test_example():
    start_values, connections = parse_input('example_input.txt')
    print(start_values)
    print(connections)
    values = recursive_route(start_values, connections)
    assert calculate_number(values) == 2024


def test_part1():
    start_values, connections = parse_input('input.txt')
    print(start_values)
    print(connections)
    values = recursive_route(start_values, connections)
    print(calculate_number(values))
    assert True


def test_example_part2():
    start_values, connections = parse_input('input.txt')
    print(start_values)
    print(connections)
    values = recursive_route(start_values, connections)
    bad_bits = find_bad_bits(values)
    print(bad_bits)
    assert False
    # assert output == "z00,z01,z02,z05"
