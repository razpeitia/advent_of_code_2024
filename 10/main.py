from collections import deque

def read_file(filename):
    with open(filename, 'rt') as f:
        return [line.strip() for line in f]

def score_trail(grid, m, n, i, j):
    score = 0
    stack = [(i, j)]
    visited = set()
    positions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while stack:
        i, j = stack.pop()
        visited.add((i, j))
        for di, dj in positions:
            ni, nj = di + i, dj + j
            if (0 <= ni < m) and \
               (0 <= nj < n) and \
               (ni, nj) not in visited and \
               grid[ni][nj].isdigit() and \
               (int(grid[i][j]) + 1) == int(grid[ni][nj]):
                if grid[ni][nj] == "9":
                    score += 1
                visited.add((ni, nj))
                stack.append((ni, nj))
    return score

def part1(filename):
    grid = read_file(filename)
    m = len(grid)
    n = len(grid[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "0":
                score = score_trail(grid, m, n, i, j)
                ans += score
    print(ans)
    return ans

def neighbors(grid, m, n, i, j, level):
    positions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    for di, dj in positions:
        ni, nj = di + i, dj + j
        if (0 <= ni < m) and (0 <= nj < n) and grid[ni][nj].isdigit() and grid[ni][nj] == level:
            yield ni, nj

def get_sum(grid, rate_grid, m, n, i, j, level):
    positions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    s = 0
    for di, dj in positions:
        ni, nj = di + i, dj + j
        if (0 <= ni < m) and (0 <= nj < n) and grid[ni][nj] == level:
            s += rate_grid[ni][nj]
    return s

def rate_trail(grid, m, n, i, j):
    rate = 0
    rate_grid = [[0] * n for _ in range(m)]
    rate_grid[i][j] = 1
    queue = deque([(i, j)])
    level = 0
    while queue:
        x = len(queue)
        updates = []
        for _ in range(x):
            i, j = queue.popleft()
            for ni, nj in neighbors(grid, m, n, i, j, str(level+1)):
                s = get_sum(grid, rate_grid, m, n, ni, nj, str(level))
                updates.append((ni, nj, s))
                queue.append((ni, nj))
        level += 1
        for i, j, s in updates:
            rate_grid[i][j] = s
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "9":
                rate += rate_grid[i][j]
    return rate

def part2(filename):
    grid = read_file(filename)
    m = len(grid)
    n = len(grid[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "0":
                rate = rate_trail(grid, m, n, i, j)
                ans += rate
    print(ans)
    return ans

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 1 == main("example1.txt", 1)
    assert 2 == main("example2.txt", 1)
    assert 4 == main("example3.txt", 1)
    assert 3 == main("example4.txt", 1)
    assert 36 == main("example5.txt", 1)
    assert 746 == main("input.txt", 1)
    assert 3 == main("example6.txt", 2)
    assert 13 == main("example7.txt", 2)
    assert 227 == main("example8.txt", 2)
    assert 81 == main("example9.txt", 2)
    assert 1541 == main("input.txt", 2)

