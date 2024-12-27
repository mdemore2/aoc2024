from day25 import parse_input, fit_combos


def test_example():
    locks, keys = parse_input('example_input.txt')
    print(locks)
    print(keys)
    assert fit_combos(locks, keys) == 3
