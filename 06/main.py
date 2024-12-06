def read_file(filename):
    with open(filename, 'rt') as f:
        return [list(line.strip()) for line in f]

def get_start(world):
    n = len(world)
    m = len(world[0])
    for i in range(n):
        for j in range(m):
            if world[i][j] not in ".#":
                return i, j

def part1(filename):
    world = read_file(filename)
    i, j = get_start(world)
    path = set()
    directions = {
        "^": (-1, 0),
        ">": (0, 1),
        "<": (0, -1),
        "v": (1, 0),
    }
    next_direction = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^",
    }
    n = len(world)
    m = len(world[0])
    while (i, j, world[i][j]) not in path:
        direction = world[i][j]
        path.add((i, j, direction))
        ni = i + directions[direction][0]
        nj = j + directions[direction][1]
        if (0 <= ni < n) and (0 <= nj < m):
            if world[ni][nj] == '.':
                world[i][j] = '.'
                world[ni][nj] = direction
                i, j = ni, nj
            else:
                world[i][j] = next_direction[direction]
        else:
            break
    ans = len({(i, j) for i, j, _ in path})
    print(ans)
    return ans

def has_loop(world, n, m, i, j):
    oi, oj = i, j
    odirection = world[i][j]
    path = set()
    directions = {
        "^": (-1, 0),
        ">": (0, 1),
        "<": (0, -1),
        "v": (1, 0),
    }
    next_direction = {
        "^": ">",
        ">": "v",
        "v": "<",
        "<": "^",
    }
    while (i, j, world[i][j]) not in path:
        direction = world[i][j]
        path.add((i, j, direction))
        ni = i + directions[direction][0]
        nj = j + directions[direction][1]
        if (0 <= ni < n) and (0 <= nj < m):
            if world[ni][nj] == '.':
                world[i][j] = '.'
                world[ni][nj] = direction
                i, j = ni, nj
            else:
                world[i][j] = next_direction[direction]
        else:
            world[i][j] = '.'
            world[oi][oj] = odirection
            return False
    world[i][j] = '.'
    world[oi][oj] = odirection
    return True

def part2(filename):
    world = read_file(filename)
    i, j = get_start(world)
    n = len(world)
    m = len(world[0])
    ans = 0
    # Slow: Brute force solution
    # 33s on Mac M1
    for x in range(n):
        for y in range(m):
            if world[x][y] == ".":
                world[x][y] = "#"
                if has_loop(world, n, m, i, j):
                    ans += 1
                world[x][y] = "."
    print(ans)
    return ans

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 41 == main("example.txt", 1)
    assert 5242 == main("input.txt", 1)
    assert 6 == main("example.txt", 2)
    assert 1424 == main("input.txt", 2)
