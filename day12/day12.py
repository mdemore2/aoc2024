assigned_to_region = []  # SET of TUPLES
regions = []  # LIST of SET of TUPLES


def get_total_price(input_map: list) -> int:
    for x in range(len(input_map)):
        for y in range(len(input_map[x])):
            if (x, y) in assigned_to_region:
                continue
            new_region = explore_region(x, y)
            if new_region:
                regions.append(new_region)
                assigned_to_region += new_region
    price = calc_price()


def explore_region(x, y, input_map) -> list:
    to_explore = []
    if input_map[x][y] == input_map[x+1][y]:
        to_explore.append((x+1, y))
    if input_map[x][y] == input_map[x][y+1]:
        to_explore.append((x, y+1))
    if to_explore:
        return [explore_region(point for point in to_explore)]
    else:
        return [(x, y)]


def calc_price() -> int:
    """ price is area * perimeter
    """
    for region in regions:
        area = len(region)  # area is number of plots in region
        perimeter = 0  # perimeter is number of sides
