with open("input.txt") as fp:
    global file_contents
    file_contents = fp.read()

pairs = file_contents.split('\n')

def part1():
    count = 0
    for pair in pairs:
        x,y = pair.split(',')
        x = list(map(int,x.split('-')))
        y = list(map(int,y.split('-')))

        if (x[0] >= y[0] and x[1] <= y[1]) or (y[0] >= x[0] and y[1] <= x[1]):
            count += 1

    return count

def part2():
    count = 0
    for pair in pairs:
        x,y = pair.split(',')
        x = list(map(int,x.split('-')))
        y = list(map(int,y.split('-')))

        if x[1] >= y[0] and x[0] <= y[1]:
            count += 1

    return count

if __name__ == '__main__':
    print(part1())
    print(part2())