POSSIBLE_MOVEMENTS = {
    'A': ['B', 'D', 'E', 'F', 'H'],
    'B': ['A', 'C', 'D', 'E', 'F', 'G', 'I'],
    'C': ['B', 'D', 'E', 'F', 'H'],
    'D': ['A', 'B', 'C', 'E', 'G', 'H', 'I'],
    'E': ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I'],
    'F': ['A', 'B', 'C', 'E', 'G', 'H', 'I'],
    'G': ['B', 'D', 'E', 'F', 'H'],
    'H': ['A', 'C', 'D', 'E', 'F', 'G', 'I'],
    'I': ['B', 'D', 'E', 'F', 'H']
}

def main(firstPoint: str, length: int) -> list:
    return dfs(firstPoint, length, set(), [], [])

def dfs(point: str, length: int, visited: set, path: list, all_paths: list) -> list:
    # Base case
    if length == 1:
        all_paths.append(path + [point])
        return all_paths
    
    visited.add(point)
    for neighbour in POSSIBLE_MOVEMENTS[point]:
        if neighbour not in visited:
            dfs(neighbour, length - 1, visited, path + [point], all_paths)
    visited.remove(point)

    return all_paths 



if __name__ == '__main__':
    print(main('E', 4))