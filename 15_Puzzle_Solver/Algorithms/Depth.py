import collections
import copy


def dfs(puzzle, the_way):
    maxdepth = 20

    class depp_class:
        krotek = puzzle
        path = ""

        def __init__(self, tablica):
            self.krotek = tablica

    kolejka = collections.deque()
    visited = set()
    start = depp_class(puzzle)

    if start.krotek.check():
        print("układ rozwiazany bez ruchu")
        return start.krotek

    kolejka.append(start)

    def function2(array, direction):
        temp = copy.deepcopy(array)
        temp.krotek.move(direction)
        if temp.krotek.hashme() not in visited:
            visited.add(temp.krotek.hashme())
            temp.path += direction
            temp.krotek.deep += 1
            kolejka.append(temp)

    def function(array, direction):
        if direction == "U":
            if array.krotek.findIndexOfNum(0)[0] != 0:
                function2(array, "U")
        elif direction == "D":
            if array.krotek.findIndexOfNum(0)[0] != array.krotek.rows - 1:
                function2(array, "D")
        elif direction == "R":
            if array.krotek.findIndexOfNum(0)[1] != array.krotek.columns - 1:
                function2(array, "R")
        elif direction == "L":
            if array.krotek.findIndexOfNum(0)[1] != 0:
                function2(array, "L")

    while kolejka:
        current = kolejka.pop()
        if current.krotek.deep == maxdepth:
            continue

        if current.krotek.check():
            print(iter)
            print(current.path)
            print(current.krotek.deep)
            return current.krotek

        for i in range(4):
            function(current, the_way[i])
