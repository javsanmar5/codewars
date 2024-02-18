def path_finder(maze: str) -> bool:
    found = False
    completed = False
    maze = parse(maze)
    visited = set()
    path = list()

    while not completed and not found:
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if (i,j) not in visited:
                    visited.add((i,j))
                    if maze[i][j] == '.':
                        path.append(maze[i][j])
                    else:
                        path = list()
                if path.contains((len(maze)-1, len(maze[0]-1))): found = True


    






def parse(string: str) -> list:
    string += "\n"
    lista = list()
    aux = list()
    for i in string:
        if i != "\n":
            aux.append(i)
        else:
            lista.append(aux)
            aux = list()

    return lista




maze = "\n".join([
        ".W.",
        ".W.",
        "W.."
    ])

print(parse(maze))