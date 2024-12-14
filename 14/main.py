def parse(line):
    p, v = line.split()
    p = [int(x) for x in p[2:].split(",")]
    v = [int(x) for x in v[2:].split(",")]
    return [p, v]

def read_file(filename):
    with open(filename, 'rt') as f:
        return [parse(line.strip()) for line in f]

def update(robot, w, h):
    [[x, y], [vx, vy]] = robot
    x = (x + vx) % w
    y = (y + vy) % h
    robot[0][0] = x
    robot[0][1] = y

def get_cuadrant(x, y, w, h):
    cuadrant = 0
    cuadrant |= (x <= (w // 2))
    cuadrant <<= 1
    cuadrant |= (y <= (h // 2))
    return cuadrant

def part1(filename, w, h):
    robots = read_file(filename)
    for _ in range(100):
        for robot in robots:
            update(robot, w, h)
    grid = [[0] * w for _ in range(h)]
    for [[x, y], _] in robots:
        grid[y][x] += 1

    cuadrants = [0] * 4
    for [[x, y], _] in robots:
        if (w & 1 and x == (w // 2)) or (y & 1 and y == (h // 2)):
            continue
        cuadrant = get_cuadrant(x, y, w, h)
        cuadrants[cuadrant] += 1
    ans = cuadrants[0] * cuadrants[1] * cuadrants[2] * cuadrants[3]
    print(ans)
    return ans

def part2(filename, w, h):
    from itertools import groupby
    robots = read_file(filename)
    i = 0
    while True:
        for robot in robots:
            update(robot, w, h)
        i += 1
        grid = [[0] * w for _ in range(h)]
        for [[x, y], _] in robots:
            grid[y][x] = 1
        for y in range(h):
            for v, l in groupby(grid[y]):
                if v == 1 and len(list(l)) >= 10:
                    print(i)
                    return i


def main(filename, part, w, h):
    if part == 1:
        return part1(filename, w, h)
    elif part == 2:
        return part2(filename, w, h)


if __name__ == "__main__":
    robot = [[2, 4], [2, -3]] 
    update(robot, 11, 7)
    assert [4, 1] == robot[0]
    update(robot, 11, 7)
    assert [6, 5] == robot[0]
    update(robot, 11, 7)
    assert [8, 2] == robot[0]
    update(robot, 11, 7)
    assert [10, 6] == robot[0]
    update(robot, 11, 7)
    assert [1, 3] == robot[0]
    assert 12 == main("example.txt", 1, 11, 7)
    assert 214400550 == main("input.txt", 1, 101, 103)
    main("input.txt", 2, 101, 103)

