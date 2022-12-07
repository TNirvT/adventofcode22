def open_txt(filename: str) -> list[str]:
    with open(filename) as f:
        lines = []
        for line in f:
            lines.append(line.rstrip())
    return lines

def strategy(lines: list[str]) -> int:
    # replace X by A, Y by B, Z by C
    tmp_lines: list[str] = []
    for line in lines:
        tmp_line = line.replace("X", "A").replace("Y", "B").replace("Z", "C")
        tmp_lines.append(tmp_line)

    score = 0
    for line in tmp_lines:
        if line[-1] == "A":
            score += 1
        if line[-1] == "B":
            score += 2
        if line[-1] == "C":
            score += 3

        if line[0] == line[-1]:
            # draw
            score += 3
        elif line == "A B" or line == "B C" or line == "C A":
            # win
            score += 6

    return score

def part2(lines: list[str]) -> int:
    score = 0
    tmp_lines: list[str] = []
    for line in lines:
        if line[-1] == "X":
            # loose
            if line[0] == "A":
                score += 3
            elif line[0] == "B":
                score += 1
            else:
                score += 2
        elif line[-1] == "Y":
            # draw
            score += 3
            if line[0] == "A":
                score += 1
            elif line[0] == "B":
                score += 2
            else:
                score += 3
        else:
            # win
            score += 6
            if line[0] == "A":
                score += 2
            elif line[0] == "B":
                score += 3
            else:
                score += 1

    return score

if __name__ == "__main__":
    lines = open_txt("aoc02.txt")
    # lines = open_txt("test.txt")
    print("part1: ", strategy(lines))
    print("part2: ", part2(lines))
