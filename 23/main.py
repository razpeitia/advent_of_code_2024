from collections import defaultdict
from itertools import combinations

def read_file(filename):
    graph = defaultdict(list)
    with open(filename, 'rt') as f:
        for line in f:
            [a, b] = line.strip().split("-")
            graph[a].append(b)
            graph[b].append(a)
    return graph

def part1(filename):
    graph = read_file(filename)
    three_set = set()
    for a, v in graph.items():
        for b in v:
            s = set(v)
            s.remove(b)
            for c in s:
                if b in graph[c]:
                    t = tuple(sorted((a, b, c)))
                    three_set.add(t)
    ans = 0
    for i in sorted(three_set):
        if any(x.startswith("t") for x in i):
            ans += 1
    print(ans)
    return ans
            

def part2(filename):
    graph = read_file(filename)
    n_set = set()
    for a, nodes in graph.items():
        for node in nodes:
            n_set.add(tuple(sorted([a, node])))
    
    m_set = n_set
    while 1:
        p_set = set()
        for a in graph:
            for nodes in m_set:
                if all(tuple(sorted([a, node])) in n_set for node in nodes):
                    p_set.add(tuple(sorted([a] + list(nodes))))
        if len(p_set) == 1:
            ans = ','.join(sorted(p_set.pop()))
            print(ans)
            return ans
        m_set = p_set


def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 7 == main("example.txt", 1)
    main("input.txt", 1)
    # assert 'co,de,ka,ta' == main("example.txt", 2)
    main("example.txt", 2)
    main("input.txt", 2)

