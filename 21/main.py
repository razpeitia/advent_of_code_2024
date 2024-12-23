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

def min_len(table1, table2, code):
    m = float("inf")
    for x in table1[code]:
        x = ''.join(x)
        x = "A" + x
        for y in product(*[table2[a1+b1] for a1, b1 in zip(x[:-1], x[1:])]):
            y = ''.join(y)
            y = "A" + y
            for z in product(*[table2[a2+b2] for a2, b2 in zip(y[:-1], y[1:])]):
                z = ''.join(z)
                if len(z) < m:
                    m = len(z)
    return m

def part1(filename):
    codes = read_file(filename)
    table1 = get_all_paths(["789", "456", "123", " 0A"])
    table2 = get_all_paths([" ^A", "<v>"])
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
    pass

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 126384 == main("example.txt", 1)
    main("input.txt", 1)

