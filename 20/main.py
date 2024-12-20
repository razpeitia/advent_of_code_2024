from collections import deque, defaultdict
from itertools import combinations

def read_file(filename):
    with open(filename, 'rt') as f:
        return [list(line.strip()) for line in f]

def find(grid, goal):
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c == goal:
                grid[i][j] = "."
                return (i, j)

def precompute(grid, start):
    queue = deque([(start, 0)])
    visited = {start}
    positions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    m = len(grid)
    n = len(grid[0])
    distances = {start: 0}
    while queue:
        (i, j), distance = queue.popleft()
        for di, dj in positions:
            ni, nj = i+di, j+dj
            if (0 <= ni < m) and (0 <= nj < n) and grid[ni][nj] != "#" and (ni, nj) not in visited:
                visited.add((ni, nj))
                distances[ni,nj] = distance+1
                queue.append(((ni, nj), distance+1))
    return distances

def part1(filename):
    grid = read_file(filename)
    end = find(grid, "E")
    distances = precompute(grid, end)
    count = defaultdict(int)
    for p1, p2 in combinations(list(distances.keys()), 2):
        y1, x1 = p1
        y2, x2 = p2
        d = abs(x1 - x2) + abs(y1 - y2) 
        if d == 2:
            savings = (distances[y2,x2] - distances[y1,x1]) - d
            count[savings] += 1
    ans = sum([v for k, v in count.items() if k >= 100])
    print(ans)
    return ans

def part2(filename):
    grid = read_file(filename)
    end = find(grid, "E")
    distances = precompute(grid, end)
    count = defaultdict(int)
    for p1, p2 in combinations(list(distances.keys()), 2):
        y1, x1 = p1
        y2, x2 = p2
        d = abs(x1 - x2) + abs(y1 - y2) 
        if d <= 20:
            savings = (distances[y2,x2] - distances[y1,x1]) - d
            count[savings] += 1
    for k, v in sorted(count.items()):
        print(k, v)
    ans = sum([v for k, v in count.items() if k >= 100])
    print(ans)
    return ans

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    main("example.txt", 1)
    main("input.txt", 1)
    main("input.txt", 2)

