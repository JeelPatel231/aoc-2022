with open("input.txt") as fp:
    global file_contents
    file_contents = fp.read()

chunked = [ sum([int(j) for j in i.split('\n')]) for i in file_contents.split('\n\n') ]

def part1():
    # max takes O(n)
    return max(chunked)

def part2():
    # sort takes O(nlogn)
    chunked.sort()
    return sum(chunked[-3:])

if __name__ == '__main__':
    print(part1())
    print(part2())