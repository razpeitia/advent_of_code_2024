from collections import deque

def read_file(filename):
    with open(filename, 'rt') as f:
        return [int(c) for c in f.read().strip()]

def part1(filename):
    line = deque(read_file(filename))
    n = len(line)
    lid = 0
    rid = n // 2
    block = 0
    ans = 0
    lfree = 0
    right = 0

    while line:
        if lfree == 0:
            left = line.popleft()
            for _ in range(left):
                ans += lid * block
                block += 1
            lid += 1
            lfree = line.popleft()
        if right == 0:
            right = line.pop()
        if lfree >= right:
            for _ in range(right):
                ans += rid * block
                block += 1
            lfree -= right
            rid -= 1
            right = 0
            # ignoring end space
            if line:
                line.pop()
        else:
            for _ in range(lfree):
                ans += rid * block
                block += 1
            right -= lfree
            lfree = 0
    if right:
        for _ in range(right):
            ans += rid * block
            block += 1
    print(ans)
    return ans

def find_free_space(rstart, rsize, free_index):
    min_start = rstart
    size = 0
    for free_space, spaces in free_index.items():
        if free_space >= rsize:
            if spaces[0] < min_start:
                min_start = spaces[0]
                size = free_space
    return min_start, size

def part2(filename):
    free_index = {}
    fid_index = {}

    line = []
    for i, x in enumerate(read_file(filename)):
        if i & 1 == 0:
            fid_index[i // 2] = (len(line), x)
            for _ in range(x):
                line.append(i // 2)
        else:
            if x == 0: continue
            if x not in free_index:
                free_index[x] = []
            free_index[x].append(len(line))
            for _ in range(x):
                line.append(".")
    rid = line[-1]
    while rid > 0:
        # Left most free space that can fit
        rstart, rsize = fid_index[rid]
        free_start, free_size = find_free_space(rstart, rsize, free_index)
        if free_start < rstart:
            for x in range(rsize):
                line[rstart+x], line[free_start+x] = line[free_start+x], line[rstart+x]
            free_index[free_size].pop(0)
            if not free_index[free_size]:
                free_index.pop(free_size)
            new_free_size = free_size - rsize
            if new_free_size:
                if new_free_size not in free_index:
                    free_index[new_free_size] = []
                free_index[new_free_size].append(free_start + rsize)
                free_index[new_free_size].sort()
        rid -= 1
    ans = sum([i*x for i, x in enumerate(line) if x != "."])
    print(ans)
    return ans

    


def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 1928 == main("example.txt", 1)
    assert 6432869891895 == main("input.txt", 1)
    assert 2858 == main("example.txt", 2)
    assert 6467290479134 == main("input.txt", 2)

