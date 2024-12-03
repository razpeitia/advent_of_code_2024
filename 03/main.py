import re

def read_file(filename):
    with open(filename, 'rt') as f:
        for line in f:
            yield line.strip()

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)

def part1(filename):
    ans = 0
    for line in read_file(filename):
        for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line):
            a, b = int(a), int(b)
            ans += a * b
    print(ans)
    return ans

def part2(filename):
    ans = 0
    enable = True
    for line in read_file(filename):
        for op in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line):
            if op == "don't()":
                enable = False
            elif op == "do()":
                enable = True
            else:
                if not enable:
                    continue
                (a, b) = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", op).groups()
                a, b = int(a), int(b)
                ans += a * b
    print(ans)
    return ans

if __name__ == "__main__":
    assert 161 == main("example1.txt", 1)
    main("input1.txt", 1)
    assert 48 == main("example2.txt", 2)
    main("input1.txt", 2)