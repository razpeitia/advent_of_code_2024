from collections import Counter

def read_file(filename):
    with open(filename, 'rt') as f:
        for line in f:
            line = line.strip()
            yield [int(i) for i in line.split()]

def part1(filename):
    count = 0
    options = (1, 2, 3)
    for line in read_file(filename):
        if line[0] > line[1]:
            if all((a - b) in options for a, b in zip(line[:-1], line[1:])):
                count += 1
        else:
            if all((b - a) in options for a, b in zip(line[:-1], line[1:])):
                count += 1
    print(count)
    return count

def check_brute_force(line):
    if simple_check(line):
        return 1
    for i in range(len(line)):
        if simple_check(line[:i] + line[i+1:]):
            return 1
    return 0

def simple_check(line):
    operations = [(a - b) for a, b in zip(line[:-1], line[1:])]
    operations_set = set(operations)
    if operations_set <= {1, 2, 3} or operations_set <= {-1, -2, -3}:
        return 1
    return 0

def part2(filename):
    count = 0
    for line in read_file(filename):
        count += check_brute_force(line)
    print(count)
    return count

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)

if __name__ == "__main__":
    assert 2 == main("example.txt", 1)
    assert 639 == main("input1.txt", 1)
    assert 4 == main("example.txt", 2)
    assert 674 == main("input1.txt", 2)
