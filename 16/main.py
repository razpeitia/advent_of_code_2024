from collections import deque

ROTATE_CLOCKWISE = {(0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0), (-1, 0): (0, 1)}
ROTATE_COUNTERCLOCKWISE = {v: k for k, v in ROTATE_CLOCKWISE.items()}

def read_file(filename):
    with open(filename, 'rt') as f:
        return [list(line.strip()) for line in f]

def neighbors(i, j, di, dj):
    return [((i+di, j+dj), (di, dj), 1),
            ((i, j), ROTATE_CLOCKWISE[di, dj], 1000),
            ((i, j), ROTATE_COUNTERCLOCKWISE[di, dj], 1000)]

def bfs(grid, s, direction, e):
    from collections import defaultdict
    queue = deque([([(s, direction)], 0)])
    visited = {}
    min_score = float("inf")
    paths = defaultdict(list)
    while queue:
        (path, score) = queue.popleft()
        (i, j), (di, dj) = path[-1]
        key = ((i, j), (di, dj))
        visited[key] = score if key not in visited else min(visited[key], score)
        if (i, j) == e:
            min_score = min(min_score, score)
            paths[min_score].append(path)
        for ((ni, nj), (ndi, ndj), weigth) in neighbors(i, j, di, dj):
            key = ((ni, nj), (ndi, ndj))
            if grid[ni][nj] != '#':
                new_score = score + weigth
                if key not in visited or new_score <= visited[key]:
                    visited[key] = new_score
                    queue.append((path + [((ni, nj), (ndi, ndj))], new_score))
    tiles = set()
    for path in paths[min_score]:
        cost = 0
        for ((p1, _), (p2, _)) in zip(path[:-1], path[1:]):
            cost += 1 if p1 != p2 else 1000
        if cost == min_score:
            for (p, _) in path:
                tiles.add(p)
    return min_score, len(tiles)

def main(filename):
    grid = read_file(filename)
    m = len(grid)
    n = len(grid[0])
    s = m - 2, 1
    e = 1, n - 2
    ans = bfs(grid, s, (0, 1), e)
    print(ans)
    return ans


if __name__ == "__main__":
    assert (7036, 45) == main("example1.txt")
    assert (11048, 64) == main("example2.txt")
    assert (73404, 449) == main("input.txt")

