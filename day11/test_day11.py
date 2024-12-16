from day11 import algo

input_test = [125, 17]


def test_algo():
    assert algo(input_test, 3) == [512072, 1, 20, 24, 28676032]


def test_solve():
    my_input = [5, 127, 680267, 39260, 0, 26, 3553, 5851995]
    blinks = 75
    result = algo(my_input, blinks)
    print(len(result))
    assert False
