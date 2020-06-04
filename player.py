import game

def player(maze, moves):
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

    if maze[j][i] == "Y":
        print("The path Found: " + moves)
        game.grid_parser(maze, moves)
        return True

    return False