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

def all_paths(start):
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
    grid = ["789", "456", "123", " 0A"]
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
            if (0 <= ni < m) and (0 <= nj < n) and grid[ni][nj] != ' ' and ((ni, nj) not in visited or len(new_path) <= len(visited[ni,nj])):
                queue.append(new_path)
                visited[ni,nj] = new_path
                paths[ni,nj].append(new_path)
                paths[ni,nj] = [p for p in paths[ni,nj] if len(new_path) == len(p)]
    paths = {grid[k[0]][k[1]]: [encode_instructions(p) for p in v] for k, v in paths.items()}
    return paths

def get_all_paths():
    table = {}
    grid = ["789", "456", "123", " 0A"]
    for i in range(4):
        for j in range(3):
            if grid[i][j] != " ":
                for k, v in all_paths((i, j)).items():
                    table[grid[i][j] + k] = v
    return table

def part1(filename):
    codes = read_file(filename)
    table1 = get_all_paths()
    for k, v in sorted(table1.items()):
        print(k, v)

def part2(filename):
    pass

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 126384 == main("example.txt", 1)

