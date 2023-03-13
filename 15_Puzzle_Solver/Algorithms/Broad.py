import collections
import copy

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def kurwa(puzzle):
    kolejka = collections.deque()
    visited = set()
    iteration = 0

    if puzzle.check():
        print("za pierwszym kurwa")
        return puzzle
    kolejka.append(puzzle)

    while kolejka:

        current = kolejka.popleft()

        if current.check():
            print(iteration)
            return current

        if current.findIndexOfNum(0)[0] != 0:
            temp = copy.deepcopy(current)
            temp.move(temp.UP)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
                kolejka.append(temp)
                iteration += 1

        if current.findIndexOfNum(0)[1] != 0:
            temp = copy.deepcopy(current)
            temp.move(temp.LEFT)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
                kolejka.append(temp)
                iteration += 1

        if current.findIndexOfNum(0)[0] != current.rows - 1:
            temp = copy.deepcopy(current)
            temp.move(temp.DOWN)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
                kolejka.append(temp)
                iteration += 1

        if current.findIndexOfNum(0)[1] != current.columns - 1:
            temp = copy.deepcopy(current)
            temp.move(temp.RIGHT)
            if tuple(map(tuple, temp.array)) not in visited:
                visited.add(tuple(map(tuple, temp.array)))
                kolejka.append(temp)
                iteration += 1
