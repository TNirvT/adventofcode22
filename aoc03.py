import string

LETTERS = string.ascii_lowercase + string.ascii_uppercase

def open_txt(filename: str) -> list[str]:
    with open(filename) as f:
        lines = []
        for line in f:
            lines.append(line.rstrip())
    return lines

def find_priority(line: str) -> int:
    sack_size = len(line)
    for item in line:
        if item in line[sack_size//2:]:
            return LETTERS.index(item) + 1

if __name__ == "__main__":
    lines = open_txt("aoc03.txt")
    # lines = open_txt("test.txt")
    result = 0
    for line in lines:
        result += find_priority(line)
    print("part1: ", result)
