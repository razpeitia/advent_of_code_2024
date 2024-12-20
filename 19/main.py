from functools import cache

def read_file(filename):
    with open(filename, 'rt') as f:
        [patterns, designs] = f.read().split("\n\n")
        patterns = tuple([x.strip() for x in patterns.split(",")])
        designs = [x.strip() for x in designs.splitlines()]
        return patterns, designs

@cache
def is_possible(patterns, design, cache):
    if not design:
        return True
    for pattern in patterns:
        if design.startswith(pattern) and is_possible(patterns, design.removeprefix(pattern)):
            return True
    return False

def part1(filename):
    patterns, designs = read_file(filename)
    ans = 0
    for design in designs:
        if is_possible(patterns, design):
            ans += 1
    print(ans)
    return ans

@cache
def count_ways(patterns, design):
    if not design:
        return 1
    count = 0
    for pattern in patterns:
        if design.startswith(pattern):
            count += count_ways(patterns, design.removeprefix(pattern))
    return count


def part2(filename):
    patterns, designs = read_file(filename)
    ans = 0
    for design in designs:
        ans += count_ways(patterns, design)
    print(ans)
    return ans

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 6 == main("example.txt", 1)
    main("input.txt", 1)
    assert 16 == main("example.txt", 2)
    main("input.txt", 2)
