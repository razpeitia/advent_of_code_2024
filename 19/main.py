def read_file(filename):
    with open(filename, 'rt') as f:
        [patterns, designs] = f.read().split("\n\n")
        patterns = [x.strip() for x in patterns.split(",")]
        designs = [x.strip() for x in designs.splitlines()]
        return patterns, designs


def is_possible(patterns, design, cache):
    if not design:
        return True
    if design in cache:
        return cache[design]
    for pattern in patterns:
        if design.startswith(pattern):
            suffix = design[len(pattern):]
            if is_possible(patterns, suffix, cache):
                cache[suffix] = True
                return True
            else:
                cache[suffix] = False
    cache[design] = False
    return False

def part1(filename):
    patterns, designs = read_file(filename)
    ans = 0
    cache = {}
    for i, design in enumerate(designs):
        if is_possible(patterns, design, cache):
            ans += 1
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
    assert 6 == main("example.txt", 1)
    main("input.txt", 1)

