import collections
import copy


def dfs(puzzle):
    maxdepth = 9

    class depp_class:
        krotek = puzzle
        path = ""
        deep = 1

        def __init__(self, tablica):
            self.krotek = tablica

    kolejka = collections.deque()
    visited = set()

    start = depp_class(puzzle)

    if start.krotek.check():
        print("układ rozwiazany bez ruchu")
        return start.krotek

    kolejka.append(start)

    while kolejka:
        current = kolejka.pop()
        if current.deep == maxdepth:
            continue

        if current.krotek.check():
            print(iter)
            print(current.path)
            print(current.deep)
            return current.krotek

        if current.krotek.findIndexOfNum(0)[0] != 0:
            if current.path == "" or current.path[-1] != "D":
                temp = copy.deepcopy(current)
                temp.krotek.move(temp.krotek.UP)
                if tuple(map(tuple, temp.krotek.array)) not in visited:
                    visited.add(tuple(map(tuple, temp.krotek.array)))
                    temp.path += "U"
                    temp.deep += 1
                    kolejka.append(temp)

        if current.krotek.findIndexOfNum(0)[1] != 0:
            if current.path == "" or current.path[-1] != "R":
                temp = copy.deepcopy(current)
                temp.krotek.move(temp.krotek.LEFT)
                if tuple(map(tuple, temp.krotek.array)) not in visited:
                    visited.add(tuple(map(tuple, temp.krotek.array)))
                    temp.path += "L"
                    temp.deep += 1
                    kolejka.append(temp)

        if current.krotek.findIndexOfNum(0)[0] != current.krotek.rows - 1:
            if current.path == "" or current.path[-1] != "U":
                temp = copy.deepcopy(current)
                temp.krotek.move(temp.krotek.DOWN)
                if tuple(map(tuple, temp.krotek.array)) not in visited:
                    visited.add(tuple(map(tuple, temp.krotek.array)))
                    temp.path += "D"
                    temp.deep += 1
                    kolejka.append(temp)

        if current.krotek.findIndexOfNum(0)[1] != current.krotek.columns - 1:
            if current.path == "" or current.path[-1] != "L":
                temp = copy.deepcopy(current)
                temp.krotek.move(temp.krotek.RIGHT)
                if tuple(map(tuple, temp.krotek.array)) not in visited:
                    visited.add(tuple(map(tuple, temp.krotek.array)))
                    temp.path += "R"
                    temp.deep += 1
                    kolejka.append(temp)
