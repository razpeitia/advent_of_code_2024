from collections import defaultdict

def read_file(filename):
    with open(filename, 'rt') as f:
        return [int(line.strip()) for line in f]

def generate(secret_number, num):
    for _ in range(num):
        secret_number = (secret_number * 64) ^ secret_number
        secret_number = secret_number % 16777216
        secret_number = (secret_number // 32) ^ secret_number
        secret_number = secret_number % 16777216
        secret_number = (secret_number * 2048) ^ secret_number
        secret_number = secret_number % 16777216
    return secret_number

def generate_all(secret_number, num):
    results = [secret_number]
    for _ in range(num):
        secret_number = (secret_number * 64) ^ secret_number
        secret_number = secret_number % 16777216
        secret_number = (secret_number // 32) ^ secret_number
        secret_number = secret_number % 16777216
        secret_number = (secret_number * 2048) ^ secret_number
        secret_number = secret_number % 16777216
        results.append(secret_number)
    return results

def part1(filename):
    ans = 0
    for secret_number in read_file(filename):
        ans += generate(secret_number, 2000)
    print(ans)
    return ans

def fill_sequences(secret_numbers, sequences):
    visited = set()
    for i in range(4, len(secret_numbers)):
        x = secret_numbers[i-4] % 10
        a = secret_numbers[i-3] % 10
        b = secret_numbers[i-2] % 10
        c = secret_numbers[i-1] % 10
        d = secret_numbers[i] % 10
        sequence = (a - x, b - a, c - b, d - c)
        if sequence not in visited:
            visited.add(sequence)
            sequences[sequence] += d

def part2(filename):
    sequences = defaultdict(int)
    for secret_number in read_file(filename):
        secret_numbers = generate_all(secret_number, 2000)
        fill_sequences(secret_numbers, sequences)
    _, max_bananas = max(sequences.items(), key=lambda x: x[1])
    print(max_bananas)
    return max_bananas

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 15887950 == generate(123, 1)
    assert 16495136 == generate(123, 2)
    assert 527345 == generate(123, 3)
    assert 704524 == generate(123, 4)
    assert 1553684 == generate(123, 5)
    assert 12683156 == generate(123, 6)
    assert 11100544 == generate(123, 7)
    assert 12249484 == generate(123, 8)
    assert 7753432 == generate(123, 9)
    assert 5908254 == generate(123, 10)
    assert 37327623 == main("example.txt", 1)
    main("input.txt", 1)
    assert 23 == main("example2.txt", 2)
    main("input.txt", 2)
