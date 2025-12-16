def load_input():
    grid = []
    with open("input.txt") as file:
        input = file.read()
        for line in input.splitlines():
            row = []
            for char in line:
                row.append(char)
            grid.append(row)
    return grid

def part1(grid: list[list[str]]) -> int:
    paper_roll_count = 0
    for row in grid:
        pass # complete me
    return paper_roll_count

def main():
    grid = load_input()
    print(grid[0])

if __name__ == "__main__":
    main()
