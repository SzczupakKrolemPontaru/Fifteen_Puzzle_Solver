from PuzzleState import PuzzleState
# import Algorithms.Algorithm_AStar as AStar
from Algorithms.Broad import bfs
import sys

argumenty = []
for arg in sys.argv:
    argumenty.append(str(arg))

fSource = '4x4_01_0001.txt'
fSolution = ''
strategy = ''
parameter = ''
fStatistics = ''


def loadPuzzle():
    puzzle = []

    file = open(fSource, 'r')
    temp = file.readline()
    cols = temp.split(" ")[0]
    rows = temp.split(" ")[1].split()[0]

    for line in file.readlines():
        numbers = line.strip().split()
        numbers = [int(number) for number in numbers]
        puzzle.append(numbers)

    return rows, cols, puzzle


puzzle = PuzzleState(*loadPuzzle())

print(bfs(puzzle))
