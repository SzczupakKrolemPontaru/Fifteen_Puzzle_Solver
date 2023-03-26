import collections
import copy
import time

def dfs(puzzle, the_way):
    maxdepth = 15

    kolejka = collections.deque()
    visited = set()
    start = puzzle
    iteration = 1


    kolejka.append(start)
    start = time.time()
    def checking(array, direction):
        temp = copy.deepcopy(array)
        temp.move(direction)
        if temp.hashme() not in visited:
            visited.add(temp.hashme())
            temp.path += direction
            temp.lastmove = direction
            temp.deep += 1
            kolejka.append(temp)

    def move_way(array, direction):
        if direction == "U":
            if array.findIndexOfNum(0)[0] != 0 and array.lastmove != "D":
                checking(array, "U")
        elif direction == "D":
            if array.findIndexOfNum(0)[0] != array.rows - 1 and array.lastmove != "U":
                checking(array, "D")
        elif direction == "R":
            if array.findIndexOfNum(0)[1] != array.columns - 1 and array.lastmove != "L":
                checking(array, "R")
        elif direction == "L":
            if array.findIndexOfNum(0)[1] != 0 and array.lastmove != "R":
                checking(array, "L")

    while kolejka:
        iteration += 1
        current = kolejka.pop()
        if current.deep-1 == maxdepth:
            continue

        if current.check():

            #print("iteracje: ", iteration)
            #print(current.path)
            #print("glebokosc rekursji: ",current.deep)
            #print("stany odwiedzone: ", len(visited))
            end = time.time()
            #print("czas",end - start)
            return len(current.path), current.path, len(visited), iteration, current.deep-1, round((end-start),3)

        for i in range(4):
            move_way(current, the_way[i])   # this is the Way
