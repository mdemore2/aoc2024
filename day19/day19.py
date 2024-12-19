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