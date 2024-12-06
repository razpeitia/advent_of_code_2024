def read_file(filename):
    with open(filename, 'rt') as f:
        pass

def part1(filename):
    pass

def part2(filename):
    pass

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    main("example.txt", 1)

