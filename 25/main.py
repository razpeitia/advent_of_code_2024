from itertools import combinations

def parse_block(block):
    lines = block.split()
    parsed_block = [0] * len(lines[0])
    for line in lines:
        for i, c in enumerate(line):
            if c == "#":
                parsed_block[i] += 1
    if lines[0] == len(lines[0]) * "#":
        return ("UP", parsed_block)
    else:
        return ("DOWN", parsed_block)

def read_file(filename):
    with open(filename, 'rt') as f:
        return [parse_block(block) for block in f.read().split("\n\n")]

def part1(filename):
    blocks = read_file(filename)
    ans = 0
    for (a, b) in combinations(range(len(blocks)), 2):
        block_a = blocks[a]
        block_b = blocks[b]
        if block_a[0] != block_b[0]:
            if all(x + y <= 7 for x, y in zip(block_a[1], block_b[1])):
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
    assert 3 == main("example.txt", 1)
    main("input.txt", 1)

