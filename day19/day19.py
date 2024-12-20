import itertools


def parse_input(filename: str) -> tuple:
    available_list = []
    desired_list = []

    with open(filename, 'r') as f:
        line = f.readline()
        line = line.strip()
        line = line.replace(" ", "")
        available_list = line.split(',')
        while line:
            line = f.readline()
            if line:
                desired_list.append(line)

    return available_list, desired_list


def count_possible(filename: str) -> int:
    available, desired = parse_input(filename)
    possible = 0
    perms = itertools.permutations(available)
    perms = [''.join(combo) for combo in perms]
    print(perms)
    for pattern in desired:
        if any(pattern in substring for substring in perms):
            print(pattern)
            possible += 1

    return possible
