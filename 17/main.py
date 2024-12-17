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

def execute2(program, a, b, c):
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
            output.append(operand % 8)
            if len(output) > len(program):
                return False
            elif len(output) <= len(program) and output[-1] != program[len(output)-1]:
                return False
        elif opcode == 6:
            operand = combo_operand(operand, a, b, c)
            b = a // (1 << operand)
        elif opcode == 7:
            operand = combo_operand(operand, a, b, c)
            c = a // (1 << operand)
    return output == program

def part2(filename):
    a, b, c, program = read_file(filename)
    a = 0
    while True:
        if (a & (a - 1)) == 0:
            print(a)
        if execute2(program, a, b, c):
            print(a)
            return a
        a += 1

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

