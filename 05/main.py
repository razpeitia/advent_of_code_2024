def read_file(filename):
    rules = []
    orders = []
    with open(filename, 'rt') as f:
        status = 1
        for line in f:
            line = line.strip()
            if not line:
                status += 1
                continue
            if status == 1:
                rules.append([int(x) for x in line.split("|")])
            else:
                orders.append([int(x) for x in line.split(",")])
    return rules, orders

def part1(filename):
    rules, orders = read_file(filename)
    rule_index = {(a, b) for [a, b] in rules}
    ans = 0
    for order in orders:
        if all(x in rule_index for x in zip(order[:-1], order[1:])):
            ans += order[len(order) // 2]
    print(ans)
    return ans

def fix_order(order, rule_index):
    n = len(order)
    # Bubble sort FTW
    for _ in range(n):
        for i in range(1, n):
            a, b = order[i - 1], order[i]
            if (a, b) not in rule_index and (b, a) in rule_index:
                order[i - 1], order[i] = b, a
        if all(x in rule_index for x in zip(order[:-1], order[1:])):
            return


def part2(filename):
    rules, orders = read_file(filename)
    rule_index = {(a, b) for [a, b] in rules}
    ans = 0
    for order in orders:
        if not all(x in rule_index for x in zip(order[:-1], order[1:])):
            fix_order(order, rule_index)
            ans += order[len(order) // 2]
    print(ans)
    return ans


def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 143 == main("example.txt", 1)
    assert 5208 == main("input1.txt", 1)
    assert 123 == main("example.txt", 2)
    assert 6732 == main("input1.txt", 2)
