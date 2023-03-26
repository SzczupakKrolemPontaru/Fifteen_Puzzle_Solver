import collections
import copy
import time


def dfs(puzzle, the_way):
    maxdepth = 20

    kolejka = collections.deque()
    start = copy.deepcopy(puzzle)
    iteration = 1
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
        elif direction == "D":
            if array.findIndexOfNum(0)[0] != array.rows - 1:
                moveandcheck(array, "D")
        elif direction == "R":
            if array.findIndexOfNum(0)[1] != array.columns - 1:
                moveandcheck(array, "R")
        elif direction == "L":
            if array.findIndexOfNum(0)[1] != 0:
                moveandcheck(array, "L")
        return

    while kolejka:
        iteration += 1
        current = kolejka.pop()
        if current.deep - 1 == maxdepth:
            continue

        if current.check():
            # print("iteracje: ", iteration)
            # print(current.path)
            # print("glebokosc rekursji: ",current.deep)
            # print("stany odwiedzone: ", len(visited))
            # print("czas",end - start)
            end = time.time()
<<<<<<< HEAD
            #print("czas",end - start)
            return len(current.path), current.path, len(visited), iteration, current.deep-1, round((end-start),3)
=======
            return len(current.path), current.path, len(visited), iteration, current.deep, round((end - start), 3)
>>>>>>> 0d77bcbc74f31bfb196e6e61463f5709091e78ec

        for i in range(4):
            move_way(current, the_way[i])  # this is the Way
