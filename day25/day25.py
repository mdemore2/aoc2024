def parse_input(filename: str) -> tuple:
    locks = []
    keys = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            if line.startswith('#'):
                new_lock = [-1, -1, -1, -1, -1]
                while line.strip() != '':
                    for index in range(len(line)):
                        if line[index] == '#':
                            new_lock[index] += 1
                    line = f.readline()
                locks.append(new_lock)
            else:
                new_key = [-1, -1, -1, -1, -1]  # offset start/end line
                while line.strip() != '':
                    for index in range(len(line)):
                        if line[index] == '#':
                            new_key[index] += 1
                    line = f.readline()
                keys.append(new_key)
            line = f.readline()

    return locks, keys


def fit_combos(locks: list, keys: list) -> int:
    num_fits = 0
    for lock in locks:
        for key in keys:
            overlap = False
            for pin in range(len(key)):
                total = key[pin] + lock[pin]
                if total > 5:
                    overlap = True
            if not overlap:
                num_fits += 1

    return num_fits
