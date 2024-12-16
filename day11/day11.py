import json

def algo(input_list: list, blinks: int, length_only:bool=False) -> list:
    current_list = input_list
    for iter in range(blinks):
        # print(f'Iteration: {iter}')
        new_list = []
        for stone in current_list:
            # print(f'Current Stone: {stone}')
            if stone == 0:
                # print('Rule: is 0')
                new_list.append(1)
            elif len(str(stone)) % 2 == 0:
                # print('Rule: split')
                split_index = int(len(str(stone)) / 2)
                new_list += [int(str(stone)[:split_index]),
                             int(str(stone)[split_index:])]
            else:
                # print('Rule: none of the above')
                new_list.append(stone*2024)
        current_list = new_list
    if length_only:
        return len(current_list)
    return current_list


#def algo_batched(input_list: list, blinks: int) -> list:
#    current_list = input_list
#    current_length = len(input_list)
#    for iter in range(blinks):
#        if len(current_list) > 200000:
#            with open(f"to_process{}.json", "w") as f:
#                json.dump(current_list[100000:], f)
#        # print(f'Iteration: {iter}')
#        new_list = []
#        for stone in current_list:
#            # print(f'Current Stone: {stone}')
#            if stone == 0:
#                # print('Rule: is 0')
#                new_list.append(1)
#            elif len(str(stone)) % 2 == 0:
#                # print('Rule: split')
#                split_index = int(len(str(stone)) / 2)
#                new_list += [int(str(stone)[:split_index]),
#                             int(str(stone)[split_index:])]
#            else:
#                # print('Rule: none of the above')
#                new_list.append(stone*2024)
#        current_list = new_list
#        current_length = len(current_list)
#    return current_length

def simple_algo(input_list:list) -> list:
    new_list = []
    for stone in input_list:
        if stone == 0:
            # print('Rule: is 0')
            new_list.append(1)
        elif len(str(stone)) % 2 == 0:
            # print('Rule: split')
            split_index = int(len(str(stone)) / 2)
            new_list += [int(str(stone)[:split_index]),
                         int(str(stone)[split_index:])]
        else:
            # print('Rule: none of the above')
            new_list.append(stone*2024)
    return new_list