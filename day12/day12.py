from collections import deque


def get_total_price(input_map: list) -> int:
    assigned_to_region = set()  # SET of TUPLES
    regions = []  # LIST of SET of TUPLES
    for x in range(len(input_map)):
        for y in range(len(input_map[x])):
            if (x, y) in assigned_to_region:
                continue
            new_region = flatten_region(explore_region(x, y, input_map))
            if new_region:
                regions.append(new_region)
                assigned_to_region.add(point for point in new_region)
    print(regions)
    price = calc_price(regions)
    return price

def flatten_region(region_list:list) -> set:
    region_set = set()
    for item in region_list:
        while type(item) is list:
            item = item[0]
        region_set.add(item)
    return region_set
        

def explore_region(x, y, input_map) -> list:
    to_explore = []
    try:
        if input_map[x][y] == input_map[x+1][y]:
            to_explore.append((x+1, y))
        if input_map[x][y] == input_map[x][y+1]:
            to_explore.append((x, y+1))
    except IndexError as e:
        pass
    if to_explore:
        return [explore_region(point[0], point[1], input_map) for point in to_explore]
    else:
        return [(x, y)]


def get_perimeter(region) -> int:
    total = 0
    for point in region:
        x = point[0]
        y = point[1]
        total += 4
        for neighbor in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
            if neighbor in region:
                total -=1

    return total

def calc_price(regions) -> int:
    """ price is area * perimeter
    """
    total = 0
    for region in regions:
        area = len(region)  # area is number of plots in region
        perimeter = get_perimeter(region)  # perimeter is number of sides
        total += area * perimeter

    return total
