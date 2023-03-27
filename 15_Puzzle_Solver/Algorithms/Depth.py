import collections
import copy
import time


def dfs(puzzle, the_way):
    maxdepth = 20

    kolejka = collections.deque()
    start = copy.deepcopy(puzzle)
    przetworzone = 0
    odwiedzone = 0
    kolejka.append(start)
    start = time.time()
    visited = {
        puzzle.hashme(): puzzle.deep - 1
    }

    def moveandcheck(array, direction):
        temp = copy.deepcopy(array)
        temp.move(direction)
        if temp.hashme() in visited and visited[temp.hashme()] > temp.deep or temp.hashme() not in visited:
            visited[temp.hashme()] = array.deep
            temp.path += direction
            temp.deep += 1
            kolejka.append(temp)

    def move_way(array, direction):
        if direction == "U":
            if array.findIndexOfNum(0)[0] != 0:
                moveandcheck(array, "U")
                return 1
        elif direction == "D":
            if array.findIndexOfNum(0)[0] != array.rows - 1:
                moveandcheck(array, "D")
                return 1
        elif direction == "R":
            if array.findIndexOfNum(0)[1] != array.columns - 1:
                moveandcheck(array, "R")
                return 1
        elif direction == "L":
            if array.findIndexOfNum(0)[1] != 0:
                moveandcheck(array, "L")
                return 1
        else:
            return 0

    while kolejka:
        current = kolejka.pop()
        przetworzone += 1
        if current.deep - 1 == maxdepth:
            continue

        if current.check():
            end = time.time()
            return len(current.path), current.path, odwiedzone, przetworzone, current.deep, round((end - start), 3)

        for i in range(4):
            if move_way(current, the_way[i]) == 1:  # this is the Way
                odwiedzone += 1
