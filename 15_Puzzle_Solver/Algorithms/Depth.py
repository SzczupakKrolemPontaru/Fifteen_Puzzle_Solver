import collections
import copy


def dfs(puzzle, the_way):
    maxdepth = 15

    class depp_class:
        krotek = puzzle
        path = ""
        lastmove = "BASE"

        def __init__(self, tablica):
            self.krotek = tablica

    kolejka = collections.deque()
    visited = set()
    start = depp_class(puzzle)

    if start.krotek.check():
        print("układ rozwiazany bez ruchu")
        return start.krotek

    kolejka.append(start)

    def checking(array, direction):
        temp = copy.deepcopy(array)
        temp.krotek.move(direction)
        if temp.krotek.hashme() not in visited:
            visited.add(temp.krotek.hashme())
            temp.path += direction
            temp.lastmove = direction
            temp.krotek.deep += 1
            kolejka.append(temp)

    def move_way(array, direction):
        if direction == "U":
            if array.krotek.findIndexOfNum(0)[0] != 0 and array.lastmove != "D":
                checking(array, "U")
        elif direction == "D":
            if array.krotek.findIndexOfNum(0)[0] != array.krotek.rows - 1 and array.lastmove != "U":
                checking(array, "D")
        elif direction == "R":
            if array.krotek.findIndexOfNum(0)[1] != array.krotek.columns - 1and array.lastmove != "L":
                checking(array, "R")
        elif direction == "L":
            if array.krotek.findIndexOfNum(0)[1] != 0 and array.lastmove != "R":
                checking(array, "L")

    while kolejka:
        current = kolejka.pop()
        if current.krotek.deep-1 == maxdepth:
            continue

        if current.krotek.check():
            print(iter)
            print(current.path)
            print(current.krotek.deep)
            return current.krotek

        for i in range(4):
            move_way(current, the_way[i])   # this is the Way
