with open("input.txt") as fp:
    global file_content
    file_contents = fp.read()

def solve(chars: int):
    x = 0
    while len(set(file_contents[x:x+chars])) != chars:
        x += 1
    return (x+chars)

def part1():
    return solve(4)

def part2():
    return solve(14)


if __name__ == '__main__':
    print(part1())
    print(part2())