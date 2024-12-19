

def parse_input() -> tuple:
    input_1 = []
    input_2 = []
    with open('input.txt','r') as f:
        line = f.readline()
        while line:
            part_1, part_2 = line.split()
            input_1.append(int(part_1))
            input_2.append(int(part_2))
            line = f.readline()
    return input_1, input_2


def calculate_distance(input_1: list, input_2: list) -> int:
    input_1.sort()
    input_2.sort()
    distance = 0
    for index in range(len(input_1)):
        distance += abs(input_1[index] - input_2[index])
    return distance

def calculate_similarity(input_1: list, input_2: list) -> int:
    similarity = 0
    for num in input_1:
        appearances = input_2.count(num)
        similarity += num * appearances
    return similarity
