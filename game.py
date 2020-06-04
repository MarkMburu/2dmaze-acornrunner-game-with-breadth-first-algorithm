import queue

import player

def Grid():
    grid= []
    grid.append(["*","X","*","*","*","*","*","*","*","*","*","*","*","*","*",])
    grid.append(["*"," "," "," "," "," "," "," ","2"," "," "," "," ","W","*",])
    grid.append(["*"," ","*","*","*"," ","*","*"," ","*","*","*","*"," ","*",])
    grid.append(["*"," ","*"," ","W","W","*","*","*","*","1"," "," ","Y","*",])
    grid.append(["*"," ","*","*","*","*"," "," ","*","*","*","*","*","F","*",])
    grid.append(["*"," "," ","2"," ","*"," "," "," ","*","*"," ","*","F","*",])
    grid.append(["*","W","*","W","W","*","*","*"," "," ","F","F","F","F","*",])
    grid.append(["*"," ","1","*","*","*","*","*","*","*","*","F","F","F","*",])
    grid.append(["*","*","*","*","*","*","*","*","*","*","F","F","F","F","*",])

    return grid


def grid_parser(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "X":
            start = x

    i = start
    j = 0
    pos = set()
    for move in path:
        if move == "A":
            i -= 1

        elif move == "D":
            i += 1

        elif move == "W":
            j -= 1

        elif move == "S":
            j += 1
        pos.add((j, i))
    
    for j, row in enumerate(maze):
        for i, col in enumerate(row):
            if (j, i) in pos:
                print("$ ", end="")
            else:
                print(col + " ", end="")
        print()

def valid(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "X":
            start = x

    i = start
    j = 0
    for move in moves:
        if move == "A":
            i -= 1

        elif move == "D":
            i += 1

        elif move == "W":
            j -= 1

        elif move == "S":
            j += 1

        if not(0 <= i < len(maze[0]) and 0 <= j < len(maze)):
            return False
        elif (maze[j][i] == "*"):
            return False

    return True

maze  = Grid()
nums = queue.Queue()
nums.put("")
add = ""

while not player.player(maze, add): 
    add = nums.get()

    for j in ["A", "D", "W", "S"]:
        put = add + j
        if valid(maze, put):
           nums.put(put)



    