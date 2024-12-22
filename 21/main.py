from collections import deque, defaultdict
from itertools import product

def read_file(filename):
    with open(filename, 'rt') as f:
        return [line.strip() for line in f]

def encode_instructions(path):
    table = {(0, 1): ">", (0, -1): "<", (1, 0): "v", (-1, 0): "^"}
    instructions = []
    for (i, j), (ni, nj) in zip(path[:-1], path[1:]):
        a = (i - ni)
        b = (j - nj)
        instructions.append(table[a,b])
    return ''.join(instructions) + "A"

def all_paths():
    """
    +---+---+---+
    | 7 | 8 | 9 |
    +---+---+---+
    | 4 | 5 | 6 |
    +---+---+---+
    | 1 | 2 | 3 |
    +---+---+---+
        | 0 | A |
        +---+---+
    """
    return {
        "78": ['<A'],
        "74": ['^A'],
        "79": ['<<A'],
        "75": ['<^A', '^<A'],
        "71": ['^^A'],
        "76": ['<<^A', '<^<A', '^<<A'],
        "72": ['<^^A', '^<^A', '^^<A'],
        "73": ['<<^^A', '<^<^A', '<^^<A', '^<<^A', '^<^<A', '^^<<A'],
        "70": ['<^^^A', '^<^^A', '^^<^A', '^^^<A'],
        "7A": ['<<^^^A', '<^<^^A', '<^^<^A', '<^^^<A', '^<<^^A', '^<^<^A', '^<^^<A', '^^<<^A', '^^<^<A', '^^^<<A'],
        "89": ['<A'],
        "85": ['^A'],
        "87": ['>A'],
        "86": ['<^A', '^<A'],
        "82": ['^^A'],
        "84": ['^>A', '>^A'],
        "83": ['<^^A', '^<^A', '^^<A'],
        "80": ['^^^A'],
        "81": ['^^>A', '^>^A', '>^^A'],
        "8A": ['<^^^A', '^<^^A', '^^<^A', '^^^<A'],
        "96": ['^A'],
        "98": ['>A'],
        "93": ['^^A'],
        "95": ['^>A', '>^A'],
        "97": ['>>A'],
        "9A": ['^^^A'],
        "92": ['^^>A', '^>^A', '>^^A'],
        "94": ['^>>A', '>^>A', '>>^A'],
        "90": ['^^^>A', '^^>^A', '^>^^A', '>^^^A'],
        "91": ['^^>>A', '^>^>A', '^>>^A', '>^^>A', '>^>^A', '>>^^A'],
        "45": ['<A'],
        "41": ['^A'],
        "47": ['vA'],
        "46": ['<<A'],
        "42": ['<^A', '^<A'],
        "48": ['<vA', 'v<A'],
        "43": ['<<^A', '<^<A', '^<<A'],
        "49": ['<<vA', '<v<A', 'v<<A'],
        "40": ['<^^A', '^<^A', '^^<A'],
        "4A": ['<<^^A', '<^<^A', '<^^<A', '^<<^A', '^<^<A', '^^<<A'],
        "56": ['<A'],
        "52": ['^A'],
        "58": ['vA'],
        "54": ['>A'],
        "53": ['<^A', '^<A'],
        "59": ['<vA', 'v<A'],
        "50": ['^^A'],
        "51": ['^>A', '>^A'],
        "57": ['v>A', '>vA'],
        "5A": ['<^^A', '^<^A', '^^<A'],
        "63": ['^A'],
        "69": ['vA'],
        "65": ['>A'],
        "6A": ['^^A'],
        "62": ['^>A', '>^A'],
        "68": ['v>A', '>vA'],
        "64": ['>>A'],
        "60": ['^^>A', '^>^A', '>^^A'],
        "61": ['^>>A', '>^>A', '>>^A'],
        "67": ['v>>A', '>v>A', '>>vA'],
        "12": ['<A'],
        "14": ['vA'],
        "13": ['<<A'],
        "10": ['<^A', '^<A'],
        "15": ['<vA', 'v<A'],
        "17": ['vvA'],
        "1A": ['<<^A', '<^<A', '^<<A'],
        "16": ['<<vA', '<v<A', 'v<<A'],
        "18": ['<vvA', 'v<vA', 'vv<A'],
        "19": ['<<vvA', '<v<vA', '<vv<A', 'v<<vA', 'v<v<A', 'vv<<A'],
        "23": ['<A'],
        "20": ['^A'],
        "25": ['vA'],
        "21": ['>A'],
        "2A": ['<^A', '^<A'],
        "26": ['<vA', 'v<A'],
        "28": ['vvA'],
        "24": ['v>A', '>vA'],
        "29": ['<vvA', 'v<vA', 'vv<A'],
        "27": ['vv>A', 'v>vA', '>vvA'],
        "3A": ['^A'],
        "36": ['vA'],
        "32": ['>A'],
        "30": ['^>A', '>^A'],
        "39": ['vvA'],
        "35": ['v>A', '>vA'],
        "31": ['>>A'],
        "38": ['vv>A', 'v>vA', '>vvA'],
        "34": ['v>>A', '>v>A', '>>vA'],
        "37": ['vv>>A', 'v>v>A', 'v>>vA', '>vv>A', '>v>vA', '>>vvA'],
        "0A": ['<A'],
        "02": ['vA'],
        "03": ['<vA', 'v<A'],
        "05": ['vvA'],
        "01": ['v>A', '>vA'],
        "06": ['<vvA', 'v<vA', 'vv<A'],
        "08": ['vvvA'],
        "04": ['vv>A', 'v>vA', '>vvA'],
        "09": ['<vvvA', 'v<vvA', 'vv<vA', 'vvv<A'],
        "07": ['vvv>A', 'vv>vA', 'v>vvA', '>vvvA'],
        "A3": ['vA'],
        "A0": ['>A'],
        "A6": ['vvA'],
        "A2": ['v>A', '>vA'],
        "A9": ['vvvA'],
        "A5": ['vv>A', 'v>vA', '>vvA'],
        "A1": ['v>>A', '>v>A', '>>vA'],
        "A8": ['vvv>A', 'vv>vA', 'v>vvA', '>vvvA'],
        "A4": ['vv>>A', 'v>v>A', 'v>>vA', '>vv>A', '>v>vA', '>>vvA'],
        "A7": ['vvv>>A', 'vv>v>A', 'vv>>vA', 'v>vv>A', 'v>v>vA', 'v>>vvA', '>vvv>A', '>vv>vA', '>v>vvA', '>>vvvA'],
    }

def all_paths2():
    """
        +---+---+---+
        |   | ^ | A |
        +---+---+---+
        | < | v | > |
        +---+---+---+
    """
    return {
        "AA": ["A"],
        "^^": ["A"],
        "<<": ["A"],
        ">>": ["A"],
        "vv": ["A"],
        "A^": ["<A"],
        "Av": ["<vA", "v<A"],
        "A<": ["v<<A", "<v<A", "<<vA"],
        "A>": ["vA"],
        "^A": [">A"],
        "^v": ["vA"],
        "^<": ["<vA", "v<A"],
        "^>": [">vA", "v>A"],
        "vA": ["^>A", ">^A"],
        "v^": ["^A"],
        "v<": ["<A"],
        "v>": [">A"],
        "<A": [">>^A", ">^>A", "^>>A"],
        "<^": ["^>A", ">^A"],
        "<v": [">A"],
        "<>": [">>A"],
        ">A": ["^A"],
        ">^": ["^<A", "<^A"],
        ">v": ["<A"],
        "><": ["<<A"],
    }

def shortest_paths(table, code):
    return [''.join(path) for path in product(*[table[a+b] for a, b in zip(code[:-1], code[1:])])]

def expand(table2, path):
    return [''.join(p) for p in product(*[table2[a+b] for a, b in zip(path[:-1], path[1:])])]

def part1(filename):
    codes = read_file(filename)
    table = all_paths()
    table2 = all_paths2()
    ans = 0
    for code in codes:
        paths = shortest_paths(table, code)
        ##
        paths = [expand(table2, path) for path in paths]
        paths = sum(paths, [])
        paths = list(set(paths))
        min_path = min(paths)
        print(min_path)
        paths = [min_path]
        ## 
        paths = [expand(table2, path) for path in paths]
        paths = sum(paths, [])
        paths = list(set(paths))
        min_path = min(paths)
        print(min_path)
        paths = [min_path]
        ##
        paths = [expand(table2, path) for path in paths]
        paths = sum(paths, [])
        paths = list(set(paths))
        min_path = min(paths)
        print(min_path)
        paths = [min_path]
        print(code, len(min_path), int(code[:3]))
        ans += len(min_path) * int(code[:3])
    print(ans)
    return ans

def part2(filename):
    pass

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 126384 == main("example.txt", 1)

