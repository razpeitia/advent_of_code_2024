from collections import Counter, defaultdict

def read_file(filename):
    with open(filename, 'rt') as f:
        return [int(x) for x in f.read().strip().split()]

def blink(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            n = len(str(stone)) // 2
            a = int(str(stone)[:n])
            b = int(str(stone)[n:])
            new_stones[a] += count
            new_stones[b] += count
        else:
            new_stones[stone * 2024] += count
    return new_stones

def solve(filename, n):
    stones = read_file(filename)
    stones = Counter(stones)
    for _ in range(n):
        stones = blink(stones)
    ans = sum(stones.values())
    print(ans)
    return ans

def part1(filename):
    return solve(filename, 25)

def part2(filename):
    return solve(filename, 75)

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 55312 == main("example.txt", 1)
    main("input.txt", 1)
    main("input.txt", 2)

