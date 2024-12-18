from collections import deque

def read_file(filename):
    with open(filename, 'rt') as f:
        return [[int(x) for x in line.strip().split(",")] for line in f]

def bfs(grid, size):
    queue = deque([[(0, 0)]])
    visited = set()
    positions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while queue:
        path = queue.popleft()
        (x, y) = pos = path[-1]
        visited.add(pos)
        if pos == (size-1, size-1):
            return len(path) - 1
        for dx, dy in positions:
            nx, ny = x+dx, y+dy
            if (0 <= nx < size) and (0 <= ny < size) and (nx, ny) not in visited and grid[ny][nx] != '#':
                visited.add((nx, ny))
                queue.append(path+[(nx, ny)])

def part1(filename, size, limit):
    points = read_file(filename)
    grid = [['.'] * size for _ in range(size)]
    for x, y in points[:limit]:
        grid[y][x] = '#'
    ans = bfs(grid, size)
    print(ans)
    return ans

def part2(filename, size, limit):
    points = read_file(filename)
    grid = [['.'] * size for _ in range(size)]
    for x, y in points[:limit]:
        grid[y][x] = '#'
    for x, y in points[limit:]:
        grid[y][x] = '#'
        ans = bfs(grid, size)
        if ans is None:
            print(f"{x},{y}")
            return x, y

def main(filename, part, size, limit):
    if part == 1:
        return part1(filename, size, limit)
    elif part == 2:
        return part2(filename, size, limit)


if __name__ == "__main__":
    assert 22 == main("example.txt", 1, 7, 12)
    main("input.txt", 1, 71, 1024)
    assert (6,1) == main("example.txt", 2, 7, 12)
    main("input.txt", 2, 71, 1024)

