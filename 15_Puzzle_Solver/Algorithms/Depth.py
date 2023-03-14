import collections
import copy


def dfs(puzzle):
    kolejka = collections.deque()
    visited = set()
    iter = 0
    
    if puzzle.check():
        return puzzle
    kolejka.appendleft(puzzle)

    while kolejka:

        current = kolejka.popleft()

        if current.check():
            return current

        if current.findIndexOfNum(0)[0] != 0:
            temp = copy.deepcopy(current)
            temp.move(temp.UP)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
                kolejka.append(temp)

        if current.findIndexOfNum(0)[1] != 0:
            temp = copy.deepcopy(current)
            temp.move(temp.LEFT)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
                kolejka.append(temp)

        if current.findIndexOfNum(0)[0] != current.rows - 1:
            temp = copy.deepcopy(current)
            temp.move(temp.DOWN)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
                kolejka.append(temp)

        if current.findIndexOfNum(0)[1] != current.columns - 1:
            temp = copy.deepcopy(current)
            temp.move(temp.RIGHT)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
                kolejka.append(temp)

            

        