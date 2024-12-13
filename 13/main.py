import re

def parse_block(block: str):
    [button_a, button_b, prize] = block.splitlines()
    button_a = [int(x) for x in re.findall(r"\d+", button_a)]
    button_b = [int(x) for x in re.findall(r"\d+", button_b)]
    prize = [int(x) for x in re.findall(r"\d+", prize)]
    return [button_a, button_b, prize]

def read_file(filename):
    with open(filename, 'rt') as f:
        return [parse_block(block) for block in f.read().split("\n\n")]

def solve(problem):
    determinant = problem[0][0] * problem[1][1] - problem[0][1] * problem[1][0]
    if determinant == 0:
        return 0
    determinant_x = problem[0][0] * problem[2][1] - problem[0][1] * problem[2][0]
    determinant_y = problem[1][1] * problem[2][0] - problem[1][0] * problem[2][1]
    if not (determinant_x % determinant == 0 and determinant_y % determinant == 0):
        return 0
    x = determinant_x // determinant
    y = determinant_y // determinant
    return x + 3*y

def part1(filename):
    ans = sum(solve(problem) for problem in read_file(filename))
    print(ans)
    return ans

def fix(problem):
    problem[2][0] += 10000000000000
    problem[2][1] += 10000000000000
    return problem

def part2(filename):
    ans = sum(solve(fix(problem)) for problem in read_file(filename))
    print(ans)
    return ans

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    assert 480 == main("example.txt", 1)
    assert 31589 == main("input.txt", 1)
    assert 875318608908 == main("example.txt", 2)
    assert 98080815200063 == main("input.txt", 2)
