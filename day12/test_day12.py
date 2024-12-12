from day12 import get_total_price

test_input = [['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'F', 'F']
              ['R', 'R', 'R', 'R', 'I', 'I', 'C', 'C', 'C', 'F']
              ['V', 'V', 'R', 'R', 'R', 'C', 'C', 'F', 'F', 'F']
              ['V', 'V', 'R', 'C', 'C', 'C', 'J', 'F', 'F', 'F']
              ['V', 'V', 'V', 'V', 'C', 'J', 'J', 'C', 'F', 'E']
              ['V', 'V', 'I', 'V', 'C', 'C', 'J', 'J', 'E', 'E']
              ['V', 'V', 'I', 'I', 'I', 'C', 'J', 'J', 'E', 'E']
              ['M', 'I', 'I', 'I', 'I', 'I', 'J', 'J', 'E', 'E']
              ['M', 'I', 'I', 'I', 'S', 'I', 'J', 'E', 'E', 'E']
              ['M', 'M', 'M', 'I', 'S', 'S', 'J', 'E', 'E', 'E']]


def test_algo():
    assert get_total_price(test_input) == 1930
