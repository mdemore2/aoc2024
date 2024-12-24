def parse_input(filename: str) -> tuple:
    start_values = []
    connections = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            wire, value = line.split(':')
            start_values.append({wire: int(value.strip())})
            line = f.readline()
        line = f.readline()  # get past line break for connections
        while line:
            inputs, output = line.split('->')
            connections.append({inputs.strip(): output.strip})

    return start_values, connections
