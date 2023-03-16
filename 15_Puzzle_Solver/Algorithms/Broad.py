import collections
import copy


def bfs(puzzle):
    class bfs_class:
        krotek = puzzle
        path = ""


        def __init__(self, tablica):
            self.krotek = tablica

    kolejka = collections.deque()
    visited = set()

    start = bfs_class(puzzle)
    if start.krotek.check():
        print("układ rozwiazany bez ruchu")
        return start.krotek
    kolejka.append(start)

    while kolejka:

        current = kolejka.popleft()

        if current.krotek.check():
            print(iter)
            print(current.path)
            print(current.krotek.deep)
            return current.krotek

        if current.krotek.findIndexOfNum(0)[0] != 0:
                temp = copy.deepcopy(current)
                temp.krotek.move(temp.krotek.UP)
                if hash(temp.krotek.hashme()) not in visited:
                    visited.add(hash((temp.krotek.hashme())))
                    temp.path += "U"
                    temp.krotek.deep += 1
                    kolejka.append(temp)

        if current.krotek.findIndexOfNum(0)[1] != 0:
                temp = copy.deepcopy(current)
                temp.krotek.move(temp.krotek.LEFT)
                if hash(temp.krotek.hashme()) not in visited:
                    visited.add(hash((temp.krotek.hashme())))
                    temp.path += "L"
                    temp.krotek.deep += 1
                    kolejka.append(temp)

        if current.krotek.findIndexOfNum(0)[0] != current.krotek.rows - 1:
                temp = copy.deepcopy(current)
                temp.krotek.move(temp.krotek.DOWN)
                if hash(temp.krotek.hashme()) not in visited:
                    visited.add(hash((temp.krotek.hashme())))
                    temp.path += "D"
                    temp.krotek.deep += 1
                    kolejka.append(temp)

        if current.krotek.findIndexOfNum(0)[1] != current.krotek.columns - 1:
                temp = copy.deepcopy(current)
                temp.krotek.move(temp.krotek.RIGHT)
                if hash(temp.krotek.hashme()) not in visited:
                    visited.add(hash((temp.krotek.hashme())))
                    temp.path += "R"
                    temp.krotek.deep += 1
                    kolejka.append(temp)
