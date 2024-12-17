def read_file(filename):
    with open(filename, 'rt') as f:
        a = int(f.readline().split(":")[1].strip())
        b = int(f.readline().split(":")[1].strip())
        c = int(f.readline().split(":")[1].strip())
        f.readline()
        program = [int(x) for x in f.readline().split(":")[1].split(",")]
        return a, b, c, program

def combo_operand(operand, a, b, c):
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    elif operand == 7:
        raise ValueError("Invalid combo operand")

def execute(program, a, b, c):
    n = len(program)
    pc = 0
    output = []
    while 0 <= pc < n:
        opcode = program[pc]
        operand = program[pc+1]
        pc += 2
        if opcode == 0:
            operand = combo_operand(operand, a, b, c)
            a = a // (1 << operand)
        elif opcode == 1:
            b = b ^ operand
        elif opcode == 2:
            operand = combo_operand(operand, a, b, c)
            b = operand % 8
        elif opcode == 3:
            if a:
                pc = operand
        elif opcode == 4:
            b = b ^ c
        elif opcode == 5:
            operand = combo_operand(operand, a, b, c)
            output.append(str(operand % 8))
        elif opcode == 6:
            operand = combo_operand(operand, a, b, c)
            b = a // (1 << operand)
        elif opcode == 7:
            operand = combo_operand(operand, a, b, c)
            c = a // (1 << operand)
    ans = ','.join(output)
    return ans

def part1(filename):
    a, b, c, program = read_file(filename)
    ans = execute(program, a, b, c)
    print(ans)
    return ans

def step(a):
    b = a % 8
    b = b ^ 7
    c = a // (1 << b)
    a = a // 8
    b = b ^ c
    b = b ^ 7
    return b % 8

def dfs(program, a, depth, ans):
    if depth == len(program) - 1:
        result = execute(program, a, 0, 0)
        result = [int(x) for x in result.split(",")]
        if result == program:
            ans.append(a)
        return
    if step(a) == program[-(depth + 1)]:
        for i in range(8):
            dfs(program, (a * 8) + i, depth + 1, ans)

def part2(filename):
    _, _, _, program = read_file(filename)
    ans = []
    for i in range(8):
        dfs(program, i, 0, ans)
    print(min(ans))
    return min(ans)
    

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert "4,6,3,5,6,3,5,2,1,0" == main("example.txt", 1)
    main("input.txt", 1)
    main("example2.txt", 2)
    main("input.txt", 2)
