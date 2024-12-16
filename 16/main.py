from collections import deque

ROTATE = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def read_file(filename):
    with open(filename, 'rt') as f:
        return [list(line.strip()) for line in f]

def neighbors(i, j, di, dj, score):
    x = ROTATE.index((di, dj))
    clockwise = ROTATE[(x + 1) % len(ROTATE)]
    counterclockwise = ROTATE[(x - 1) % len(ROTATE)]
    return [((i+di, j+dj), (di, dj), score+1),
            ((i, j), clockwise, score+1000),
            ((i, j), counterclockwise, score+1000)]

def bfs(grid, s, direction, e):
    queue = deque([(s, direction, 0)])
    visited = {}
    min_score = float("inf")
    while queue:
        ((i, j), (di, dj), score) = queue.popleft()
        key = ((i, j), (di, dj))
        visited[key] = score if key not in visited else min(visited[key], score)
        if (i, j) == e:
            min_score = min(min_score, score)
        for ((i, j), (di, dj), score) in neighbors(i, j, di, dj, score):
            key = ((i, j), (di, dj))
            if grid[i][j] != '#':
                if key not in visited:
                    visited[key] = score
                    queue.append(((i, j), (di, dj), score))
                elif visited[key] > score:
                    visited[key] = score
                    queue.append(((i, j), (di, dj), score))
    return min_score

def part1(filename):
    grid = read_file(filename)
    m = len(grid)
    n = len(grid[0])
    s = m - 2, 1
    e = 1, n - 2
    ans = bfs(grid, s, (0, 1), e)
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
    assert 7036 == main("example1.txt", 1)
    assert 11048 == main("example2.txt", 1)
    assert 73404 == main("input.txt", 1)

