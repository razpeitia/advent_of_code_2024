from collections import defaultdict
from itertools import combinations

def read_file(filename):
    with open(filename, 'rt') as f:
        return [line.strip() for line in f]

def count_antinodes(n, m, positions, antinodes):
    for (y1, x1), (y2, x2) in combinations(positions, 2):
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        x3 = max(x1, x2) + dx
        y3 = max(y1, y2) + dy
        x4 = min(x1, x2) - dx
        y4 = min(y1, y2) - dy
        for x, y in [(x3, y3), (x3, y4), (x4, y3), (x4, y4)]:
            if (0 <= x < m) and (0 <= y < n) and (x1 * (y2 - y) + x2 * (y - y1) + x * (y1 - y2)) == 0:
                antinodes.add((y, x))
        

def part1(filename):
    world = read_file(filename)
    n = len(world)
    m = len(world[0])
    antenas = defaultdict(list)
    for i in range(n):
        for j in range(m):
            if world[i][j].isalnum():
                antenas[world[i][j]].append((i, j))
    antinodes = set()
    for antena, positions in antenas.items():
        if len(positions) >= 2:
            count_antinodes(n, m, positions, antinodes)
    ans = len(antinodes)
    print(ans)
    return ans

def count_antinodes2(n, m, positions, antinodes):
    for (y1, x1), (y2, x2) in combinations(positions, 2):
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        x3 = max(x1, x2) + dx
        y3 = max(y1, y2) + dy
        x4 = min(x1, x2) - dx
        y4 = min(y1, y2) - dy
        for x, ndx, y, ndy in [(x3, dx, y3, dy), (x3, dx, y4, -dy), (x4, -dx, y3, dy), (x4, -dx, y4, -dy)]:
            if (0 <= x < m) and (0 <= y < n) and (x1 * (y2 - y) + x2 * (y - y1) + x * (y1 - y2)) == 0:
                while (0 <= x < m) and (0 <= y < n):
                    antinodes.add((y, x))
                    x += ndx
                    y += ndy

def part2(filename):
    world = read_file(filename)
    n = len(world)
    m = len(world[0])
    antenas = defaultdict(list)
    antinodes = set()
    for i in range(n):
        for j in range(m):
            if world[i][j].isalnum():
                antenas[world[i][j]].append((i, j))
                antinodes.add((i, j))
    for antena, positions in antenas.items():
        if len(positions) >= 2:
            count_antinodes2(n, m, positions, antinodes)
    ans = len(antinodes)
    print(ans)
    return ans

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 2 == main("example1.txt", 1)
    assert 4 == main("example2.txt", 1)
    assert 4 == main("example3.txt", 1)
    assert 14 == main("example.txt", 1)
    assert 214 == main("input.txt", 1)
    assert 9 == main("example5.txt", 2)
    assert 34 == main("example6.txt", 2)
    assert 809 == main("input.txt", 2)
