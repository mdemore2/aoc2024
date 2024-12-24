def parse_input(filename: str) -> tuple:
    start_values = {}
    connections = {}
    with open(filename, 'r') as f:
        line = f.readline()
        while not line.isspace():
            wire, value = line.split(':')
            start_values[wire] = int(value.strip())
            line = f.readline()
        line = f.readline()  # get past line break for connections
        while line:
            inputs, output = line.split('->')
            connections[inputs.strip()] = output.strip()
            line = f.readline()

    return start_values, connections


def route(values: dict, connections: dict) -> dict:
    completed = set()
    incomplete = True
    for connection in connections.keys():
        if connection.startswith('x') or connection.startswith('y'):
            input = connection
            output = logical_operation(values, input)
            values[connections[connection]] = output
            completed.add(connections[connection])
    while incomplete:
        incomplete = False
        for connection in connections.keys():
            if connections[connection] not in completed:
                input = connection

                output = logical_operation(values, input)
                if not output:
                    incomplete = True
                    continue
                values[connections[connection]] = output
                completed.add(connections[connection])

    return values


def recursive_route(values: dict, connections: dict) -> dict:
    print(connections)
    for inputs in connections.keys():
        wire_1, operator, wire_2 = inputs.split()
        if wire_1 not in values.keys():
            to_connect = list(connections.keys())[list(
                connections.values()).index(wire_1)]
            values = recursive_connect(to_connect, values, connections)
        if wire_2 not in values.keys():
            to_connect = list(connections.keys())[list(
                connections.values()).index(wire_1)]
            values = recursive_connect(to_connect, values, connections)
        else:
            output = logical_operation(values, inputs)
            values[connections[inputs]] = output
    print(values)
    return values


def recursive_connect(to_connect: str, values: dict, connections: dict) -> dict:
    wire_1, operator, wire_2 = to_connect.split()
    if wire_1 not in values.keys():
        to_connect = list(connections.keys())[list(
            connections.values()).index(wire_1)]
        values = recursive_connect(to_connect, values, connections)
    if wire_2 not in values.keys():
        to_connect = list(connections.keys())[list(
            connections.values()).index(wire_1)]
        values = recursive_connect(to_connect, values, connections)
    else:
        output = logical_operation(values, to_connect)
        values[connections[to_connect]] = output
    return values


def calculate_number(values: dict):
    z_list = []
    for wire in values.keys():
        if wire.startswith('z'):
            z_list.append(f'{wire} {values[wire]}')
    z_list.sort(reverse=True)
    print(z_list)
    bin_str = ''
    for bit in z_list:
        bin_str += str(bit.split()[-1])
    print(bin_str)
    return int(bin_str, 2)


def logical_operation(values: dict, input: str) -> int:
    wire_1, operator, wire_2 = input.split()
    try:
        input_1 = values[wire_1]
        input_2 = values[wire_2]
    except KeyError as e:
        return False
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
