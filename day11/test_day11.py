from day11 import algo
import json
import gc



#def test_algo():
#   input_test = [125, 17]
#    assert algo(input_test, 3) == [512072, 1, 20, 24, 28676032]
#
#
#def test_solve():
#    my_input = [5, 127, 680267, 39260, 0, 26, 3553, 5851995]
#    blinks = 25
#    result = algo(my_input, blinks)
#    with open('output_25.json','w') as f:
#        json.dump(result, f)
#    print(len(result))
#    assert False


def test_solve_part2():
    my_input = [5, 127, 680267, 39260, 0, 26, 3553, 5851995]
    blinks = 75
    final_length = 0
    for stone in my_input:
        final_length += algo([stone], 75, length_only=True)
        gc.collect()

    print(final_length)
    assert False





    



