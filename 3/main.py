with open("input.txt") as fp:
    global file_contents
    file_contents = fp.read()

rusksacks = file_contents.split('\n')

def get_priority(c):
    x = ord(c)
    if x >= 97:
        return x - 96
    return x - 38

def part1():
    _sum = 0
    for rsack in rusksacks:
        _len = len(rsack)//2
        common_el = (set(rsack[:_len]).intersection(set(rsack[_len:]))).pop()
        _sum += get_priority(common_el)
    return _sum

def part2():
    _sum = 0
    chunked = [rusksacks[i:i + 3] for i in range(0, len(rusksacks), 3)]
    for chunk in chunked:
        common_el = (set(chunk[0]).intersection(set(chunk[1]).intersection(chunk[2]))).pop()
        _sum += get_priority(common_el)
    
    return _sum

if __name__ == '__main__':
    print(part1())
    print(part2())