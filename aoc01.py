def open_txt(filename: str) -> list[str]:
    with open(filename) as f:
        lines = []
        for line in f:
            lines.append(line.rstrip())
    return lines

def calories(lines: list[str]) -> list[int]:
    calories_list = []
    count = 0
    for line in lines:
        if line:
            count += int(line)
        else:
            calories_list.append(count)
            count = 0
    calories_list.append(count)
    return calories_list

if __name__ == "__main__":
    lines = open_txt("aoc01.txt")
    # lines = open_txt("test.txt")
    calories_list = calories(lines)
    print("part1: ", max(calories_list))
