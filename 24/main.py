def parse_initial(line):
    line = line.strip()
    a, b = line.split(": ")
    return (a, int(b))

def parse_gate(line):
    line = line.strip()
    [a, b] = line.split(" -> ")
    return (b, a.split())

def read_file(filename):
    with open(filename, 'rt') as f:
        [initial, gates] = f.read().split("\n\n")
        initial = dict([parse_initial(line) for line in initial.splitlines()])
        gates = dict([parse_gate(line) for line in gates.splitlines()])
        return initial, gates

def process(initial, gates):
    while gates:
        to_delete = []
        for output, [a, operation, b] in gates.items():
            if a in initial and b in initial:
                if operation == "AND":
                    initial[output] = initial[a] & initial[b]
                elif operation == "OR":
                    initial[output] = initial[a] | initial[b]
                elif operation == "XOR":
                    initial[output] = initial[a] ^ initial[b]
                to_delete.append(output)
        for output in to_delete:
            gates.pop(output, None)
    return get_number(initial, 'z')

def part1(filename):
    initial, gates = read_file(filename)
    ans = process(initial, gates)
    print(ans)
    return ans

def get_number(initial, letter):
    ans = 0
    for k, v in initial.items():
        if k.startswith(letter):
            pos = int(k[1:])
            if v:
                ans |= (1 << pos)
    return ans


def part2(filename):
    initial, gates = read_file(filename)
    x = get_number(initial, 'x')
    y = get_number(initial, 'y')
    ans = process(initial, gates)
    for i, (a, b) in enumerate(zip(bin(ans)[2:], bin(x+y)[2:])):
        if a != b:
            print(i)

    return
    
    # Normalize gates X and Y
    for output in gates:
        if gates[output][0] > gates[output][2]:
            gates[output][0], gates[output][2] = gates[output][2], gates[output][0]

    wrong_chips = []
    # Check the first bit for a half adder
    # X00 XOR Y00 -> Z00
    # C0 = X00 AND Y00
    z = {}
    t0 = {}
    t1 = {}
    t2 = {}
    cout = {}
    
    # Check the next 44 bits for a full adder
    # X XOR Y -> T0
    # X AND Y -> T2
    # T0 XOR CIN -> Z
    # T0 AND CIN -> T1
    # T1 OR T2 -> COUT

    for k, v in gates.items():
        if v[0][0] == 'x' and v[1] == 'AND' and v[2][0] == 'y' and v[0][1:] == v[2][1:]:
            t2[int(v[0][1:])] = k
        if v[0][0] == 'x' and v[1] == 'XOR' and v[2][0] == 'y' and v[0][1:] == v[2][1:]:
            t0[int(v[0][1:])] = k
    
    for k, v in gates.items():
        if v[1] == "XOR" and (k[0] != 'z' and v[0][0] != 'x'):
            print(' '.join(v), "->", k)
        if k != 'z45' and k[0] == 'z' and v[1] != 'XOR':
            print(' '.join(v), "->", k)




    


def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    # assert 4 == main("example.txt", 1)
    # assert 2024 == main("example2.txt", 1)
    # assert 51657025112326 == main("input.txt", 1)
    main("input.txt", 2)

