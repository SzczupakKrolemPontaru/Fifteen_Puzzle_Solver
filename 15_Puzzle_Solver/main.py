from PuzzleState import PuzzleState
# import Algorithms.Algorithm_AStar as AStar
from Algorithms.Broad import bfs
from Algorithms.Depth import dfs


def loadPuzzle():
    puzzle = []

    file = open('4x4_01_0001.txt', 'r')
    temp = file.readline()
    cols = temp.split(" ")[0]
    rows = temp.split(" ")[1].split()[0]

    for line in file.readlines():
        numbers = line.strip().split()
        numbers = [int(number) for number in numbers]
        puzzle.append(numbers)

    return rows, cols, puzzle


puzzle = PuzzleState(*loadPuzzle())


# print(AStar.HammingDistance(puzzle))
# print(AStar.ManhattanDistance(puzzle))

print(bfs(puzzle, "LRUD"))
print(dfs(puzzle, "RLUD"))
