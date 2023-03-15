import collections
import copy

<<<<<<< HEAD
UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def bfs(puzzle):
=======
def bfs(puzzle):

    class bfs_class:
        krotek = puzzle
        path = ""
        def __init__(self,puzzle):
            self.krotek = puzzle

>>>>>>> parent of 946534d (bfs huczy)
    kolejka = collections.deque()
    visited = set()
    iteration = 0

<<<<<<< HEAD
    if puzzle.check():
        return puzzle
    kolejka.append(puzzle)
=======
    start = bfs_class(puzzle)
    if start.krotek.check():
        return start.krotek
    kolejka.append(start)
>>>>>>> parent of 946534d (bfs huczy)

    while kolejka:

        current = kolejka.popleft()

<<<<<<< HEAD
        if current.check():
            print(iteration)
            return current
=======
        if current.krotek.check():
            print(iter)
            print(current.path)
            return current.krotek
>>>>>>> parent of 946534d (bfs huczy)

        if current.findIndexOfNum(0)[0] != 0:
            temp = copy.deepcopy(current)
<<<<<<< HEAD
            temp.move(temp.UP)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
=======
            temp.krotek.move(temp.krotek.UP)
            if tuple(map(tuple, temp.krotek.array)) not in visited:
                visited.add(tuple(map(tuple, temp.krotek.array)))
                temp.path += "U"
>>>>>>> parent of 946534d (bfs huczy)
                kolejka.append(temp)
                iteration += 1

        if current.findIndexOfNum(0)[1] != 0:
            temp = copy.deepcopy(current)
<<<<<<< HEAD
            temp.move(temp.LEFT)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
=======
            temp.krotek.move(temp.krotek.LEFT)
            if tuple(map(tuple, temp.krotek.array)) not in visited:
                visited.add(tuple(map(tuple, temp.krotek.array)))
                temp.path += "L"
>>>>>>> parent of 946534d (bfs huczy)
                kolejka.append(temp)
                iteration += 1

        if current.findIndexOfNum(0)[0] != current.rows - 1:
            temp = copy.deepcopy(current)
<<<<<<< HEAD
            temp.move(temp.DOWN)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
=======
            temp.krotek.move(temp.krotek.DOWN)
            if tuple(map(tuple, temp.krotek.array)) not in visited:
                visited.add(tuple(map(tuple, temp.krotek.array)))
                temp.path += "D"
>>>>>>> parent of 946534d (bfs huczy)
                kolejka.append(temp)
                iteration += 1

        if current.findIndexOfNum(0)[1] != current.columns - 1:
            temp = copy.deepcopy(current)
<<<<<<< HEAD
            temp.move(temp.RIGHT)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
                kolejka.append(temp)
                iteration += 1
=======
            temp.krotek.move(temp.krotek.RIGHT)
            if tuple(map(tuple, temp.krotek.array)) not in visited:
                visited.add(tuple(map(tuple, temp.krotek.array)))
                temp.path += "R"
                kolejka.append(temp)
>>>>>>> parent of 946534d (bfs huczy)
