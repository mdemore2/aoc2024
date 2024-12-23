from day01 import calculate_distance, parse_input, calculate_similarity

def test_simple():
    list_1 = [3,4,2,1,3,3]
    list_2 = [4,3,5,3,9,3]
    assert calculate_distance(list_1, list_2) == 11

def test_part1():
    list_1, list_2 = parse_input()
    print(calculate_distance(list_1, list_2))
    assert True

def test_simple_part2():
    list_1 = [3,4,2,1,3,3]
    list_2 = [4,3,5,3,9,3]
    assert calculate_similarity(list_1, list_2) == 31

def test_part2():
    list_1, list_2 = parse_input()
    print(calculate_similarity(list_1, list_2))
    assert True
