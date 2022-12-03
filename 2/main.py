with open("input.txt") as fp:
    global file_contents
    file_contents = fp.read()

chunked = file_contents.split('\n')

def part1():
    """
    A X = ROCK
    B Y = PAPER
    C Z = SCISSOR
    """
    hashmap = {
        'A X' : 1 + 3, # rock x rock -> draw
        'B X' : 1 + 0, # paper x rock -> lose 
        'C X' : 1 + 6, # scissors x rock -> win

        'A Y' : 2 + 6, # rock  x paper -> win
        'B Y' : 2 + 3, # paper x paper -> draw 
        'C Y' : 2 + 0, # scissor x paper -> lose
        
        'A Z' : 3 + 0, # rock x scissor -> lose
        'B Z' : 3 + 6, # paper  x scissor -> win
        'C Z' : 3 + 3, # scissor x scissor -> draw
    }
    
    return sum(map(hashmap.get,chunked))

def part2():
    """
    A = ROCK
    B = PAPER
    C = SCISSOR
    X = LOSE
    Y = DRAW
    Z = WIN
    """
    hashmap = {
        'A X' : 3 + 0, # rock x scissors -> lose
        'B X' : 1 + 0, # paper x rock -> lose 
        'C X' : 2 + 0, # scissors x paper -> lose

        'A Y' : 1 + 3, # rock  x rock -> draw
        'B Y' : 2 + 3, # paper x paper -> draw 
        'C Y' : 3 + 3, # scissor x scissor -> draw
        
        'A Z' : 2 + 6, # rock x paper -> win
        'B Z' : 3 + 6, # paper x scissor -> win
        'C Z' : 1 + 6, # scissor x rock -> win
    }
    
    return sum(map(hashmap.get,chunked))


if __name__ == '__main__':
    print(part1())
    print(part2())