def read_file(filename):
    with open(filename, 'rt') as f:
        return [line.strip() for line in f]

def calculate(grid, m, n, i, j, visited):
    region = grid[i][j]
    positions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    stack = [(i, j)]
    area = 0
    perimeter = 0
    while stack:
        i, j = stack.pop()
        if (i, j) not in visited:
            area += 1
            visited.add((i, j))
            for di, dj in positions:
                ni, nj = i + di, j + dj
                if not ((0 <= ni < m) and (0 <= nj < n) and region == grid[ni][nj]):
                    perimeter += 1
        for di, dj in positions:
            ni, nj = i + di, j + dj
            if (0 <= ni < m) and (0 <= nj < n) and region == grid[ni][nj] and (ni, nj) not in visited:
                stack.append((ni, nj))
    return [area, perimeter]

def part1(filename):
    grid = read_file(filename)
    m = len(grid)
    n = len(grid[0])
    visited = set()
    regions = []
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                region = calculate(grid, m, n, i, j, visited)
                regions.append(region)
    ans = sum([region[0] * region[1] for region in regions])
    print(ans)
    return ans

def calculate2(grid, m, n, i, j, visited):
    from collections import deque
    region = grid[i][j]
    # right, down, up, left
    positions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    queue = deque([(i, j)])
    sides = {}
    area = 0
    perimeter = 0
    while queue:
        i, j = queue.popleft()
        if (i, j) not in visited:
            area += 1
            visited.add((i, j))
            for di, dj in positions:
                ni, nj = i + di, j + dj
                if not ((0 <= ni < m) and (0 <= nj < n) and region == grid[ni][nj] and (i,j,di,dj) not in sides):
                    sides[i,j,di,dj] = 1
                    sides[i+di,j+dj,-di,-dj] = 1
                    if di:
                        if (i,j+1,di,dj) not in sides and (i,j-1,di,dj) not in sides:
                            perimeter += 1
                    else:
                        if (i+1,j,di,dj) not in sides and (i-1,j,di,dj) not in sides:
                            perimeter += 1
            for di, dj in positions:
                ni, nj = i + di, j + dj
                if (0 <= ni < m) and (0 <= nj < n) and region == grid[ni][nj] and (ni, nj) not in visited:
                    queue.append((ni, nj))
    return [area, perimeter]

def part2(filename):
    grid = read_file(filename)
    m = len(grid)
    n = len(grid[0])
    visited = set()
    regions = []
    for i in range(m):
        for j in range(n):
            if (i, j) not in visited:
                region = calculate2(grid, m, n, i, j, visited)
                regions.append(region)
    ans = sum([region[0] * region[1] for region in regions])
    print(ans)
    return ans

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 140 == main("example1.txt", 1)
    assert 772 == main("example2.txt", 1)
    assert 1930 == main("example3.txt", 1)
    assert 1370258 == main("input.txt", 1)
    
    assert 80 == main("example1.txt", 2)
    assert 436 == main("example2.txt", 2)
    assert 1206 == main("example3.txt", 2)
    assert 236 == main("example4.txt", 2)
    assert 368 == main("example5.txt", 2)
    assert 805814 == main("input.txt", 2)
    