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
            # connections[inputs.strip()] = output.strip()
            # need to flip this mapping because multiple wires have same input connection
            # cant have duplicate keys
            connections[output.strip()] = inputs.strip()
            line = f.readline()

    return start_values, connections


def recursive_route(values: dict, connections: dict) -> dict:
    for inputs in connections.values():
        # print('trying to connect ', inputs)
        # print('for ', list(connections.keys())[
        #      list(connections.values()).index(inputs)])
        # print('with current values ', values)
        wire_1, operator, wire_2 = inputs.split()
        if wire_1 not in list(values.keys()):
            new_connect = list(connections.values())[list(
                connections.keys()).index(wire_1)]
            values = recursive_connect(new_connect, values, connections)
        if wire_2 not in list(values.keys()):
            new_connect = list(connections.values())[list(
                connections.keys()).index(wire_2)]
            values = recursive_connect(new_connect, values, connections)
        output = logical_operation(values, inputs)
        values[list(connections.keys())[
            list(connections.values()).index(inputs)]] = output

    for output in connections.keys():
        if output not in values.keys():
            value = logical_operation(values, connections[output])
            values[output] = value
            print('connecting for ', output)
    return values


def recursive_connect(to_connect: str, values: dict, connections: dict) -> dict:
    # print('trying to connect ', to_connect)
    # print('for ', list(connections.keys())[
    #      list(connections.values()).index(to_connect)])
    # print('with current values ', values)
    wire_1, operator, wire_2 = to_connect.split()
    if wire_1 not in list(values.keys()):
        new_connect = list(connections.values())[list(
            connections.keys()).index(wire_1)]
        values = recursive_connect(new_connect, values, connections)
    if wire_2 not in list(values.keys()):
        new_connect = list(connections.values())[list(
            connections.keys()).index(wire_2)]
        values = recursive_connect(new_connect, values, connections)
    output = logical_operation(values, to_connect)
    values[list(connections.keys())[
        list(connections.values()).index(to_connect)]] = output
    return values


def calculate_number(values: dict):
    z_list = []
    for wire in values.keys():
        if wire.startswith('z'):
            z_list.append(f'{wire} {values[wire]}')
    z_list.sort(reverse=True)
    bin_str = ''
    for bit in z_list:
        bin_str += str(bit.split()[-1])
    return int(bin_str, 2)


def logical_operation(values: dict, input: str) -> int:
    wire_1, operator, wire_2 = input.split()
    try:
        input_1 = values[wire_1]
        input_2 = values[wire_2]
    except KeyError as e:
        print('cant connect', input)
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
    if input_1 + input_2 == 2:
        return 1
    else:
        return 0


def logical_or(input_1: int, input_2: int) -> int:
    if (input_1 + input_2) >= 1:
        return 1
    else:
        return 0


def get_x_number(values: dict) -> int:
    x_list = []
    for wire in values.keys():
        if wire.startswith('x'):
            x_list.append(f'{wire} {values[wire]}')
    x_list.sort(reverse=True)
    bin_str = ''
    for bit in x_list:
        bin_str += str(bit.split()[-1])
    return int(bin_str, 2)


def get_y_number(values: dict) -> int:
    y_list = []
    for wire in values.keys():
        if wire.startswith('y'):
            y_list.append(f'{wire} {values[wire]}')
    y_list.sort(reverse=True)
    bin_str = ''
    for bit in y_list:
        bin_str += str(bit.split()[-1])
    return int(bin_str, 2)


def find_bad_bits(values: dict) -> list:
    x = get_x_number(values)
    y = get_y_number(values)
    goal_z = x + y
    bin_goal_z = bin(goal_z).replace("0b", "")
    current_z = calculate_number(values)
    bin_current_z = bin(current_z).replace("0b", "")
    num_bits = len(bin_goal_z)
    bad_bits = []
    for index in range(len(bin_goal_z)):
        if bin_current_z[index] != bin_goal_z[index]:
            bad_bits.append(num_bits - index)
    return bad_bits


def find_swap(bad_bit: str, values: dict, connections: dict) -> list:
    z_wire = "z" + "{:02d}".format(bad_bit)
    print(z_wire)
    current_val = values[z_wire]
    current_input = connections[z_wire]
    pass
