with open('input.txt','r') as fp:
    global file_lines
    file_lines = fp.read().split('\n')

top_down = []
line_index = 0
for idx,val in enumerate(file_lines):
    tmp = []
    for steps in range(1,len(val),4):
        tmp.append(val[steps])

    if val[1] == '1': break
    line_index = idx + 3
    top_down.append(tmp)

n_stacks = len(top_down[0])

def stack_maker():
    stacks = [ [] for _ in range(n_stacks) ]
    for idx in reversed(range(len(top_down))):
        container = top_down[idx]
        for i in range(n_stacks):
            if container[i] != ' ':
                stacks[i].append(container[i])

    return stacks

def part1():
    stacks = stack_maker()
    for op in file_lines[line_index:]:
        op = list(map(int, filter(str.isdigit,op.split(' '))))
        for _ in range(op[0]):
            stacks[op[2]-1].append(stacks[op[1]-1].pop())

    ans = ''
    for i in range(n_stacks):
        ans += stacks[i].pop()

    return ans

def part2():
    stacks = stack_maker()
    for op in file_lines[line_index:]:
        op = list(map(int, filter(str.isdigit,op.split(' '))))
        picked_up = reversed([stacks[op[1]-1].pop() for _ in range(op[0])])
        
        stacks[op[2]-1].extend(picked_up)

    ans = ''
    for i in range(n_stacks):
        ans += stacks[i].pop()

    return ans

if __name__ == '__main__':
    print(part1())
    print(part2())