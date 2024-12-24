from collections import deque, defaultdict
from itertools import product

def read_file(filename):
    with open(filename, 'rt') as f:
        return [line.strip() for line in f]

def encode_instructions(path):
    table = {(0, 1): "<", (0, -1): ">", (1, 0): "^", (-1, 0): "v"}
    instructions = []
    for (i, j), (ni, nj) in zip(path[:-1], path[1:]):
        a = (i - ni)
        b = (j - nj)
        instructions.append(table[a,b])
    return ''.join(instructions) + "A"

def all_paths(grid, start):
    m, n = len(grid), len(grid[0])
    queue = deque([[start]])
    visited = {start: []}
    paths = defaultdict(list)
    while queue:
        path = queue.popleft()
        (i, j) = path[-1]
        for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            ni, nj = i+di, j+dj
            new_path = path+[(ni, nj)]
            if (0 <= ni < m) and (0 <= nj < n) and grid[ni][nj] != " " and ((ni, nj) not in visited or len(new_path) <= len(visited[ni,nj])):
                queue.append(new_path)
                visited[ni,nj] = new_path
                paths[ni,nj].append(new_path)
                paths[ni,nj] = [p for p in paths[ni,nj] if len(new_path) == len(p)]
    paths = {grid[k[0]][k[1]]: [encode_instructions(p) for p in v] for k, v in paths.items()}
    return paths

def get_all_paths(grid):
    table = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != " ":
                table[grid[i][j]+grid[i][j]] = ["A"]
                for k, v in all_paths(grid, (i, j)).items():
                    table[grid[i][j]+k] = v
    return table

def min_len(table1, table2, code, steps=2):
    x = table1[code][0]
    for i in range(steps):
        x = ''.join(x)
        x = "A" + x
        x = [table2[a1+b1][0] for a1, b1 in zip(x[:-1], x[1:])]
        print(i, len(x))
    x = ''.join(x)
    return len(x)

def part1(filename):
    codes = read_file(filename)
    table1 = {'A0': ['<A'], '0A': ['>A'], 'A1': ['^<<A'], '1A': ['>>vA'], 'A2': ['<^A'], '2A': ['v>A'], 'A3': ['^A'], '3A': ['vA'], 'A4': ['^^<<A'], '4A': ['>>vvA'], 'A5': ['<^^A'], '5A': ['vv>A'], 'A6': ['^^A'], '6A': ['vvA'], 'A7': ['^^^<<A'], '7A': ['>>vvvA'], 'A8': ['<^^^A'], '8A': ['vvv>A'], 'A9': ['^^^A'], '9A': ['vvvA'], '01': ['^<A'], '10': ['>vA'], '02': ['^A'], '20': ['vA'], '03': ['^>A'], '30': ['<vA'], '04': ['^<^A'], '40': ['>vvA'], '05': ['^^A'], '50': ['vvA'], '06': ['^^>A'], '60': ['<vvA'], '07': ['^^^<A'], '70': ['>vvvA'], '08': ['^^^A'], '80': ['vvvA'], '09': ['^^^>A'], '90': ['<vvvA'], '12': ['>A'], '21': ['<A'], '13': ['>>A'], '31': ['<<A'], '14': ['^A'], '41': ['vA'], '15': ['^>A'], '51': ['<vA'], '16': ['^>>A'], '61': ['<<vA'], '17': ['^^A'], '71': ['vvA'], '18': ['^^>A'], '81': ['<vvA'], '19': ['^^>>A'], '91': ['<<vvA'], '23': ['>A'], '32': ['<A'], '24': ['<^A'], '42': ['v>A'], '25': ['^A'], '52': ['vA'], '26': ['^>A'], '62': ['<vA'], '27': ['<^^A'], '72': ['vv>A'], '28': ['^^A'], '82': ['vvA'], '29': ['^^>A'], '92': ['<vvA'], '34': ['<<^A'], '43': ['v>>A'], '35': ['<^A'], '53': ['v>A'], '36': ['^A'], '63': ['vA'], '37': ['<<^^A'], '73': ['vv>>A'], '38': ['<^^A'], '83': ['vv>A'], '39': ['^^A'], '93': ['vvA'], '45': ['>A'], '54': ['<A'], '46': ['>>A'], '64': ['<<A'], '47': ['^A'], '74': ['vA'], '48': ['^>A'], '84': ['<vA'], '49': ['^>>A'], '94': ['<<vA'], '56': ['>A'], '65': ['<A'], '57': ['<^A'], '75': ['v>A'], '58': ['^A'], '85': ['vA'], '59': ['^>A'], '95': ['<vA'], '67': ['<<^A'], '76': ['v>>A'], '68': ['<^A'], '86': ['v>A'], '69': ['^A'], '96': ['vA'], '78': ['>A'], '87': ['<A'], '79': ['>>A'], '97': ['<<A'], '89': ['>A'], '98': ['<A'], '<^': ['>^A'], '^<': ['v<A'], '<v': ['>A'], 'v<': ['<A'], '<>': ['>>A'], '><': ['<<A'], '<A': ['>>^A'], 'A<': ['v<<A'], '^v': ['vA'], 'v^': ['^A'], '^>': ['v>A'], '>^': ['<^A'], '^A': ['>A'], 'A^': ['<A'], 'v>': ['>A'], '>v': ['<A'], 'vA': ['^>A'], 'Av': ['<vA'], '>A': ['^A'], 'A>': ['vA']}
    table2 = {'^^': ['A'], '^A': ['>A'], '^v': ['vA'], '^>': ['v>A'], '^<': ['v<A'], 'AA': ['A'], 'A>': ['vA'], 'A^': ['<A'], 'Av': ['<vA'], 'A<': ['v<<A'], '<<': ['A'], '<v': ['>A'], '<>': ['>>A'], '<^': ['>^A'], '<A': ['>>^A'], 'vv': ['A'], 'v>': ['>A'], 'v^': ['^A'], 'v<': ['<A'], 'vA': ['^>A'], '>>': ['A'], '>A': ['^A'], '>v': ['<A'], '>^': ['<^A'], '><': ['<<A']}
    ans = 0
    for code in codes:
        new_code = "A" + code
        l = 0
        for c in zip(new_code[:-1], new_code[1:]):
            c = ''.join(c)
            l += min_len(table1, table2, c)
        ans += l * int(code[:3])
    print(ans)
    return ans


def part2(filename):
    codes = read_file(filename)
    table1 = {'A0': ['<A'], '0A': ['>A'], 'A1': ['^<<A'], '1A': ['>>vA'], 'A2': ['<^A'], '2A': ['v>A'], 'A3': ['^A'], '3A': ['vA'], 'A4': ['^^<<A'], '4A': ['>>vvA'], 'A5': ['<^^A'], '5A': ['vv>A'], 'A6': ['^^A'], '6A': ['vvA'], 'A7': ['^^^<<A'], '7A': ['>>vvvA'], 'A8': ['<^^^A'], '8A': ['vvv>A'], 'A9': ['^^^A'], '9A': ['vvvA'], '01': ['^<A'], '10': ['>vA'], '02': ['^A'], '20': ['vA'], '03': ['^>A'], '30': ['<vA'], '04': ['^<^A'], '40': ['>vvA'], '05': ['^^A'], '50': ['vvA'], '06': ['^^>A'], '60': ['<vvA'], '07': ['^^^<A'], '70': ['>vvvA'], '08': ['^^^A'], '80': ['vvvA'], '09': ['^^^>A'], '90': ['<vvvA'], '12': ['>A'], '21': ['<A'], '13': ['>>A'], '31': ['<<A'], '14': ['^A'], '41': ['vA'], '15': ['^>A'], '51': ['<vA'], '16': ['^>>A'], '61': ['<<vA'], '17': ['^^A'], '71': ['vvA'], '18': ['^^>A'], '81': ['<vvA'], '19': ['^^>>A'], '91': ['<<vvA'], '23': ['>A'], '32': ['<A'], '24': ['<^A'], '42': ['v>A'], '25': ['^A'], '52': ['vA'], '26': ['^>A'], '62': ['<vA'], '27': ['<^^A'], '72': ['vv>A'], '28': ['^^A'], '82': ['vvA'], '29': ['^^>A'], '92': ['<vvA'], '34': ['<<^A'], '43': ['v>>A'], '35': ['<^A'], '53': ['v>A'], '36': ['^A'], '63': ['vA'], '37': ['<<^^A'], '73': ['vv>>A'], '38': ['<^^A'], '83': ['vv>A'], '39': ['^^A'], '93': ['vvA'], '45': ['>A'], '54': ['<A'], '46': ['>>A'], '64': ['<<A'], '47': ['^A'], '74': ['vA'], '48': ['^>A'], '84': ['<vA'], '49': ['^>>A'], '94': ['<<vA'], '56': ['>A'], '65': ['<A'], '57': ['<^A'], '75': ['v>A'], '58': ['^A'], '85': ['vA'], '59': ['^>A'], '95': ['<vA'], '67': ['<<^A'], '76': ['v>>A'], '68': ['<^A'], '86': ['v>A'], '69': ['^A'], '96': ['vA'], '78': ['>A'], '87': ['<A'], '79': ['>>A'], '97': ['<<A'], '89': ['>A'], '98': ['<A'], '<^': ['>^A'], '^<': ['v<A'], '<v': ['>A'], 'v<': ['<A'], '<>': ['>>A'], '><': ['<<A'], '<A': ['>>^A'], 'A<': ['v<<A'], '^v': ['vA'], 'v^': ['^A'], '^>': ['v>A'], '>^': ['<^A'], '^A': ['>A'], 'A^': ['<A'], 'v>': ['>A'], '>v': ['<A'], 'vA': ['^>A'], 'Av': ['<vA'], '>A': ['^A'], 'A>': ['vA']}
    table2 = {'^^': ['A'], '^A': ['>A'], '^v': ['vA'], '^>': ['v>A'], '^<': ['v<A'], 'AA': ['A'], 'A>': ['vA'], 'A^': ['<A'], 'Av': ['<vA'], 'A<': ['v<<A'], '<<': ['A'], '<v': ['>A'], '<>': ['>>A'], '<^': ['>^A'], '<A': ['>>^A'], 'vv': ['A'], 'v>': ['>A'], 'v^': ['^A'], 'v<': ['<A'], 'vA': ['^>A'], '>>': ['A'], '>A': ['^A'], '>v': ['<A'], '>^': ['<^A'], '><': ['<<A']}
    ans = 0
    for code in codes:
        new_code = "A" + code
        l = 0
        for c in zip(new_code[:-1], new_code[1:]):
            c = ''.join(c)
            l += min_len(table1, table2, c, steps=25)
        ans += l * int(code[:3])
    print(ans)
    return ans

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 126384 == main("example.txt", 1)
    main("input.txt", 1)
    main("input.txt", 2)

