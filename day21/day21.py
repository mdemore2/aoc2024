def parse_input(filename:str)-> list:
    codes = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            codes.append(line)
    return codes

def get_code_path(code):
    pass

def get_directional_path(directions):
    pass