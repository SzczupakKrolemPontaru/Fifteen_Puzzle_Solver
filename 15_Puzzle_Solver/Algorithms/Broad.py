import collections
import copy
import time

def bfs(puzzle, the_way):
    kolejka = collections.deque()
    visited = set()
    start = puzzle
    kolejka.append(start)
    start = time.time()
    iteration = 1

    def checking(array, direction):
        temp = copy.deepcopy(array)
        temp.move(direction)
        if temp.hashme() not in visited:
            visited.add(temp.hashme())
            temp.path += direction
            temp.deep += 1
            kolejka.append(temp)

    def move_way(array, direction):
        if direction == "U":
            if array.findIndexOfNum(0)[0] != 0:
                checking(array, "U")
        elif direction == "D":
            if array.findIndexOfNum(0)[0] != array.rows - 1:
                checking(array, "D")
        elif direction == "R":
            if array.findIndexOfNum(0)[1] != array.columns - 1:
                checking(array, "R")
        elif direction == "L":
            if array.findIndexOfNum(0)[1] != 0:
                checking(array, "L")

    while kolejka:
        iteration += 1
        current = kolejka.popleft()

        if current.check():
            # print("iteracje: ", iteration)
            # print(current.path)
            # print("glebokosc rekursji: ",current.deep)
            # print("stany odwiedzone: ", len(visited))
            # print("czas",end - start)
<<<<<<< HEAD
            return len(current.path), current.path, len(visited), iteration, current.deep-1, round((end-start),3)
=======
            end = time.time()
            return len(current.path), current.path, len(visited), iteration, current.deep, round((end-start),3)
>>>>>>> 0d77bcbc74f31bfb196e6e61463f5709091e78ec

        for i in range(4):
            move_way(current, the_way[i])
