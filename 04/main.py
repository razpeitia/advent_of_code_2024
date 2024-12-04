def read_file(filename):
    with open(filename, 'rt') as f:
        return f.read()

def count_xmas(data, n, m, i, j):
    count = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for di, dj in directions:
        word = []
        for x in range(4):
            ni = di * x
            nj = dj * x
            if 0 <= (i + ni) < n and 0 <= (j + nj) < m:
                word.append(data[i + ni][j + nj])
            else:
                break
        word = ''.join(word)
        if word == "XMAS" or word[::-1] == "XMAS":
            count += 1
    return count

def part1(filename):
    data = read_file(filename).splitlines()
    n = len(data)
    m = len(data[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            ans += count_xmas(data, n, m, i, j)
    # Double counting
    ans = ans // 2
    print(ans)
    return ans

def count_x_mas(data, n, m, i, j):
    options = ("MAS", "SAM")
    w1 = ''.join(data[i+x][j+x] for x in range(3) if 0 <= i+x < n and 0 <= j+x < m)
    w2 = ''.join(data[i+x][j+2-x] for x in range(3) if 0 <= i+x < n and 0 <= j+2-x < m)
    if w1 in options and w2 in options:
        return 1
    return 0

def part2(filename):
    data = read_file(filename).splitlines()
    n = len(data)
    m = len(data[0])
    ans = 0
    for i in range(n):
        for j in range(m):
            ans += count_x_mas(data, n, m, i, j)
    print(ans)
    return ans

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)

if __name__ == "__main__":
    assert 18 == main("example.txt", 1)
    assert 2554 == main("input1.txt", 1)
    assert 9 == main("example.txt", 2)
    main("input1.txt", 2)