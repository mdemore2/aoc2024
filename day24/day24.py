def parse_input(filename: str) -> tuple:
    start_values = {}
    connections = {}
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            wire, value = line.split(':')
            start_values[wire] = int(value.strip())
            line = f.readline()
        line = f.readline()  # get past line break for connections
        while line:
            inputs, output = line.split('->')
            connections[inputs.strip()] = output.strip()

    return start_values, connections


def route(values: dict, connections: dict) -> dict:
    for connection in connections.keys():
        if connection.startswith('x') or connection.startswith('y'):
            input = connection
            output = logical_operation(values, input)
            values[connections[connection]] = output


def logical_operation(values: dict, input: str) -> int:
    wire_1, operator, wire_2 = input.split()
    input_1 = values[wire_1]
    input_2 = values[wire_2]
    match operator:
        case 'AND':
            output = logical_and(input_1, input_2)
        case 'OR':
            output = logical_or(input_1, input_2)
        case 'XOR':
            output = logical_xor(input_1, input_2)
    return output


def logical_xor(input_1: int, input_2: int) -> int:
    if input_1 != input_2:
        return 1
    else:
        return 0


def logical_and(input_1: int, input_2: int) -> int:
    if input_1 == input_2:
        return 1
    else:
        return 0


def logical_or(input_1: int, input_2: int) -> int:
    if (input_1 + input_2) >= 1:
        return 1
    else:
        return 0
