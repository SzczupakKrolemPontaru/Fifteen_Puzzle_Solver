import collections
import copy

def bfs(puzzle):

    class bfs_class:
        krotek = puzzle
        path = ""
        def __init__(self,puzzle):
            self.krotek = puzzle

    kolejka = collections.deque()
    visited = set()

    start = bfs_class(puzzle)
    if start.krotek.check():
        return start.krotek
    kolejka.append(start)

    while kolejka:

        current = kolejka.popleft()

        if current.krotek.check():
            print(iter)
            print(current.path)
            return current.krotek

        if current.krotek.findIndexOfNum(0)[0] != 0:
            temp = copy.deepcopy(current)
            temp.krotek.move(temp.krotek.UP)
            if tuple(map(tuple, temp.krotek.array)) not in visited:
                visited.add(tuple(map(tuple, temp.krotek.array)))
                temp.path += "U"
                kolejka.append(temp)

        if current.krotek.findIndexOfNum(0)[1] != 0:
            temp = copy.deepcopy(current)
            temp.krotek.move(temp.krotek.LEFT)
            if tuple(map(tuple, temp.krotek.array)) not in visited:
                visited.add(tuple(map(tuple, temp.krotek.array)))
                temp.path += "L"
                kolejka.append(temp)

        if current.krotek.findIndexOfNum(0)[0] != current.krotek.rows - 1:
            temp = copy.deepcopy(current)
            temp.krotek.move(temp.krotek.DOWN)
            if tuple(map(tuple, temp.krotek.array)) not in visited:
                visited.add(tuple(map(tuple, temp.krotek.array)))
                temp.path += "D"
                kolejka.append(temp)

        if current.krotek.findIndexOfNum(0)[1] != current.krotek.columns - 1:
            temp = copy.deepcopy(current)
            temp.krotek.move(temp.krotek.RIGHT)
            if tuple(map(tuple, temp.krotek.array)) not in visited:
                visited.add(tuple(map(tuple, temp.krotek.array)))
                temp.path += "R"
                kolejka.append(temp)