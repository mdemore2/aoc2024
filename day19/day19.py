def parse_input(filename:str) -> tuple:
    available_list = []
    desired_list = []

    with open(filename, 'r') as f:
        line = f.readline()
        available_list = line.split(',')
        while line:
            line = f.readline()
            if line:
                desired_list.append(line)

    return available_list, desired_list

def count_possible(filename:str) -> int:
    available, desired = parse_input(filename)
    possible = 0
    for pattern in desired:
        avail_index = 0
        pattern_index = 0
        while avail_index < len(available):
            if pattern.startswith(available[avail_index], start=pattern_index, end=len(pattern)):
                pattern_index += len(available[avail_index])
                avail_index += 1
            if pattern_index >= len(pattern):
                possible += 1
    return possible
            
