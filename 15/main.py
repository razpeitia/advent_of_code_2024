def parse_grid(grid: str) -> list[list[str]]:
    return [list(row) for line in grid.splitlines() if (row := line.strip())]

def transform_grid(grid: list[list[str]]) -> list[list[str]]:
    new_grid = []
    for row in grid:
        new_row = []
        for x in row:
            if x == "#":
                new_row.append("#")
                new_row.append("#")
            elif x == "O":
                new_row.append("[")
                new_row.append("]")
            elif x == ".":
                new_row.append(".")
                new_row.append(".")
            elif x == "@":
                new_row.append("@")
                new_row.append(".")
        new_grid.append(new_row)
    return new_grid

def read_file(filename: str) -> tuple[list[list[str]], str]:
    with open(filename, 'rt') as f:
        [grid, steps] = f.read().split("\n\n")
        steps = steps.replace("\n", "")
        grid = parse_grid(grid)
        return grid, steps

def update(grid: list[list[str]], m: int, n: int, step: str, pos: list[int, int]):
    [i, j] = pos
    direction = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    di, dj = direction[step]
    ni, nj = i+di, j+dj
    if grid[ni][nj] == ".":
        grid[ni][nj] = '@'
        grid[i][j] = '.'
        pos[0] = ni
        pos[1] = nj
    elif grid[ni][nj] == "O":
        oi, oj = ni, nj
        while grid[ni][nj] == "O":
            ni += di
            nj += dj
        if grid[ni][nj] == ".":
            grid[ni][nj] = "O"
            grid[oi][oj] = "@"
            grid[i][j] = "."
            pos[0] = oi
            pos[1] = oj

def find_robot(grid: list[list[str]], m: int, n: int) -> tuple[int, int]:
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                return i, j

def count_box_distances(grid: list[list[str]], m: int, n: int, box:str="O") -> int:
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == box:
                ans += i * 100 + j
    return ans

def print_grid(grid):
    for line in grid:
        print(''.join(line))
    print()

def part1(filename):
    grid, steps = read_file(filename)
    m: int = len(grid)
    n: int = len(grid[0])
    i, j = find_robot(grid, m, n)
    pos = [i, j]
    for step in steps:
        update(grid, m, n, step, pos)
    ans = count_box_distances(grid, m, n)
    print(ans)
    return ans

def get_boxes(grid, i, j, di, dj):
    boxes = set()
    can_move = True
    stack = [(i, j), (i, j+1)] if grid[i][j] == "[" else [(i, j-1), (i, j)]
    while stack:
        i1, j1 = stack.pop()
        i2, j2 = stack.pop()
        boxes.add((i1, j1))
        boxes.add((i2, j2))
        ni1, nj1 = i1+di, j1+dj
        ni2, nj2 = i2+di, j2+dj
        if grid[ni1][nj1] == '#' or grid[ni2][nj2] == "#":
            can_move = False
            break
        if grid[ni1][nj1] in "[]":
            if (ni1, nj1) not in boxes:
                if grid[ni1][nj1] == "[":
                    stack.append((ni1, nj1))
                    stack.append((ni1, nj1+1))
                    boxes.add((ni1, nj1))
                    boxes.add((ni1, nj1+1))
                else:
                    stack.append((ni1, nj1-1))
                    stack.append((ni1, nj1))
                    boxes.add((ni1, nj1-1))
                    boxes.add((ni1, nj1))
        if grid[ni2][nj2] in "[]":
            if (ni2, nj2) not in boxes:
                if grid[ni2][nj2] == "[":
                    stack.append((ni2, nj2))
                    stack.append((ni2, nj2+1))
                    boxes.add((ni2, nj2))
                    boxes.add((ni2, nj2+1))
                else:
                    stack.append((ni2, nj2-1))
                    stack.append((ni2, nj2))
                    boxes.add((ni2, nj2-1))
                    boxes.add((ni2, nj2))
            
    return boxes, can_move

def update2(grid: list[list[str]], m: int, n: int, step: str, pos: list[int, int]):
    [i, j] = pos
    direction = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
    di, dj = direction[step]
    ni, nj = i+di, j+dj
    if grid[ni][nj] == ".":
        grid[ni][nj] = '@'
        grid[i][j] = '.'
        pos[0] = ni
        pos[1] = nj
    elif grid[ni][nj] in "[]":
        boxes, can_move = get_boxes(grid, ni, nj, di, dj)
        if can_move:
            tmp = {(box_i, box_j) for box_i, box_j in boxes if grid[box_i][box_j] == "["}
            # Clear boxes
            for box_i, box_j in boxes:
                grid[box_i][box_j] = '.'
            # Set boxes
            for box_i, box_j in tmp:
                grid[box_i+di][box_j+dj] = "["
                grid[box_i+di][box_j+dj+1] = "]"
            grid[i][j] = "."
            grid[ni][nj] = "@"
            pos[0] = ni
            pos[1] = nj

def part2(filename):
    grid, steps = read_file(filename)
    grid = transform_grid(grid)
    # print_grid(grid)
    m: int = len(grid)
    n: int = len(grid[0])
    i, j = find_robot(grid, m, n)
    pos = [i, j]
    for step in steps:
        update2(grid, m, n, step, pos)
        # print(f"Move {step}")
        # print_grid(grid)
    ans = count_box_distances(grid, m, n, box='[')
    print(ans)
    return ans

def main(filename, part):
    if part == 1:
        return part1(filename)
    elif part == 2:
        return part2(filename)


if __name__ == "__main__":
    grid = parse_grid("""
        ########
        #.@O.O.#
        ##..O..#
        #...O..#
        #.#.O..#
        #...O..#
        #......#
        ########""")
    pos = [1, 2]
    update(grid, len(grid), len(grid[0]), ">", pos)
    assert [1, 3] == pos
    assert grid[1][2] == "."
    assert grid[1][3] == "@"
    assert grid[1][4] == "O"
    assert 2028 == main("example1.txt", 1)
    assert 10092 == main("example2.txt", 1)
    assert 1495147 == main("input.txt", 1)
    assert 9021 == main("example2.txt", 2)
    main("input.txt", 2)

