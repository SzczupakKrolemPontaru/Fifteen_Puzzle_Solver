
import collections
import copy

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


def kurwa(puzzle):
    kolejka = collections.deque()

    if puzzle.check():
        print("za pierwszym kurwa")
        return puzzle
    kolejka.append(puzzle)

    while kolejka:

        current = kolejka.popleft()

        if current.check():
            return current

        if current.findIndexOfNum(0)[0] != 0:
            temp = copy.deepcopy(current)
            temp.move(temp.UP)
            kolejka.append(temp)

        if current.findIndexOfNum(0)[1] != 0:
            temp = copy.deepcopy(current)
            temp.move(temp.LEFT)
            kolejka.append(temp)

        if current.findIndexOfNum(0)[0] != current.rows - 1:
            temp = copy.deepcopy(current)
            temp.move(temp.DOWN)
            kolejka.append(temp)

        if current.findIndexOfNum(0)[1] != current.columns - 1:
            temp = copy.deepcopy(current)
            temp.move(temp.RIGHT)
            kolejka.append(temp)
