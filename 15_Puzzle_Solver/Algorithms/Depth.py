import collections
import copy
import time


def dfs(puzzle, the_way):
    MaxDepth = 21

    stack = collections.deque()
    start = copy.deepcopy(puzzle)
    iteration = 1
    stack.append(start)
    start = time.time()
    visited = {
        puzzle.hashState(): puzzle.deep - 1
    }

    def MoveAndCheck(array, direction):
        temp = copy.deepcopy(array)
        temp.move(direction)
        if temp.hashState() in visited and visited[temp.hashState()] > temp.deep or temp.hashState() not in visited:
            visited[temp.hashState()] = array.deep
            temp.path += direction
            temp.deep += 1
            stack.append(temp)

    def move_way(array, direction):
        if direction == "U":
            if array.findIndexOfNum(0)[0] != 0 and array.lastmove != "D":
                MoveAndCheck(array, "U")
        elif direction == "D":
            if array.findIndexOfNum(0)[0] != array.rows - 1 and array.lastmove != "U":
                MoveAndCheck(array, "D")
        elif direction == "R":
            if array.findIndexOfNum(0)[1] != array.columns - 1 and array.lastmove != "L":
                MoveAndCheck(array, "R")
        elif direction == "L":
            if array.findIndexOfNum(0)[1] != 0 and array.lastmove != "R":
                MoveAndCheck(array, "L")
        return

    while stack:
        iteration += 1
        current = stack.pop()
        if current.deep - 1 == MaxDepth:
            continue

        if current.check():
            end = time.time()
            return len(current.path), current.path, len(visited), iteration, current.deep, round((end - start), 3)

        for i in range(4):
            move_way(current, the_way[i])