def read_lists(filename):
    with open(filename, 'rt') as f:
        x = []
        y = []
        for line in f:
            [a, b] = line.strip().split()
            a, b = int(a), int(b)
            x.append(a)
            y.append(b)
    return x, y

def part1(filename):
    x, y = read_lists(filename)
    x.sort()
    y.sort()
    ans = sum(abs(a - b) for a, b in zip(x, y))
    print(ans)
    return ans

def part2(filename):
    from collections import Counter
    x, y = read_lists(filename)
    c = Counter(y)
    ans = sum([i * c.get(i, 0) for i in x])
    print(ans)
    return ans


def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)
        

if __name__ == "__main__":
    assert 11 == main("example.txt", 1)
    assert 936063 == main("input1.txt", 1)
    assert 31 == main("example.txt", 2)
    main("input1.txt", 2)
