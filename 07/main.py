import itertools

def read_file(filename):
    with open(filename, 'rt') as f:
        for line in f:
            line = line.strip()
            [a, b] = line.split(":")
            yield int(a), [int(x) for x in b.split()]

def evaluate(val, operands):
    ans = operands[0]
    for n in operands[1:]:
        x = val & 1
        val >>= 1
        if x == 0:
            ans += n
        else:
            ans *= n
    return ans

def is_possible(result, operands):
    operators = len(operands) - 1
    for i in range(1 << operators):
        if result == evaluate(i, operands):
            return True
    return False

def part1(filename):
    ans = 0
    for result, operands in read_file(filename):
        if is_possible(result, operands):
            ans += result
    print(ans)
    return ans

def evaluate2(t, operands):
    ans = operands[0]
    for op, n in zip(t, operands[1:]):
        if op == 0:
            ans += n
        elif op == 1:
            ans *= n
        else:
            ans = int(str(ans) + str(n))
    return ans

def is_possible2(result, operands):
    for t in itertools.product([0, 1, 2], repeat=len(operands)-1):
        if result == evaluate2(t, operands):
            return True
    return False

def part2(filename):
    ans = 0
    for result, operands in read_file(filename):
        if is_possible(result, operands):
            ans += result
        elif is_possible2(result, operands):
            ans += result
    print(ans)
    return ans

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 3749 == main("example.txt", 1)
    assert 1582598718861 == main("input.txt", 1)
    assert 11387 == main("example.txt", 2)
    assert 165278151522644 == main("input.txt", 2)

