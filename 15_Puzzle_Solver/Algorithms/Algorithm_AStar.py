import collections
import copy
import time
direction = ["D","U","R",'L']

def aStarPuzzle(puzzle,heuristic):

    class AStarPuzzle:
        krotek = puzzle
        path = ""
        score = 0

        def __init__(self, tablica):
            self.krotek = tablica

        def __lt__(self, other) -> bool:
            return self.score < other.score

    kolejka = []
    visited = set()
    start = AStarPuzzle(puzzle)

    def ManhattanDistance(puzzle):
        h_points = 0
        goalArray = []

        for i in range(0, puzzle.krotek.rows):
            row = []
            for j in range(0, puzzle.krotek.columns):
                row.append(i * puzzle.krotek.columns + j + 1)
                if (i == puzzle.krotek.rows - 1 and j == puzzle.krotek.columns - 1):
                    row.pop()
                    row.append(0)
            goalArray.append(row)

        for i in range(puzzle.krotek.rows):
            for j in range(puzzle.krotek.columns):
                i1, j1 = puzzle.krotek.findIndexOfNum(goalArray[i][j])
                h_points += abs(i - i1) + abs(j - j1)

        return h_points + puzzle.krotek.deep

    def HammingDistance(puzzle):
        h_points = 0

        for i in range(puzzle.krotek.rows):
            for j in range(puzzle.krotek.columns):
                if (i == puzzle.krotek.rows - 1 and j == puzzle.krotek.columns - 1):
                    if (puzzle.krotek.array[i][j] != 0):
                        h_points += 1
                else:
                    expected = i * puzzle.krotek.columns + j + 1
                    if (puzzle.krotek.array[i][j] != expected):
                        h_points += 1

        return h_points + puzzle.krotek.deep   

    if start.krotek.check():
        # print("układ rozwiazany bez ruchu")
        return start.krotek

    kolejka.append(start)
    start = time.time()
    iteration = 1


    while kolejka:
        iteration += 1
        current  = kolejka.pop()
        visited.add(current.krotek.hashState())

        if current.krotek.check():
            end = time.time()
            return len(current.path), current.path, len(visited), iteration, current.krotek.deep-1, round((end-start),3)
        
        for i in range (0,4):
            temp = copy.deepcopy(current)
            temp.krotek.move(direction[i])
            if temp.krotek.hashState() not in visited:
                visited.add(temp.krotek.hashState())
                temp.path += direction[i]
                temp.krotek.deep += 1
                if (heuristic == "manh"):
                    temp.score = ManhattanDistance(temp) + temp.krotek.deep
                elif (heuristic == "hamn"):
                    temp.score = HammingDistance(temp) + temp.krotek.deep
                kolejka.append(temp)

        kolejka.sort(reverse=True)
        
