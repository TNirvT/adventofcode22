def open_txt(filename: str) -> list[str]:
    with open(filename) as f:
        lines = []
        for line in f:
            lines.append(line.rstrip())
    return lines

def get_calories(lines: list[str]) -> list[int]:
    calories = []
    count = 0
    for line in lines:
        if line:
            count += int(line)
        else:
            calories.append(count)
            count = 0
    calories.append(count)
    return calories

def top3_sum(calories: list[int]) -> int:
    result = 0
    for i in range(3):
        tmp = max(calories)
        result += tmp
        calories.remove(tmp)
    return result

if __name__ == "__main__":
    lines = open_txt("aoc01.txt")
    # lines = open_txt("test.txt")
    calories = get_calories(lines)
    print("part1: ", max(calories))
    print("part2: ", top3_sum(calories))
