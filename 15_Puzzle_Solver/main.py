from PuzzleState import PuzzleState
from Algorithms.Algorithm_AStar import aStarPuzzle
from Algorithms.Broad import bfs
from Algorithms.Depth import dfs
import sys

plikWejsiowy = '4x4_01_0001.txt'    # default

if len(sys.argv) > 1:
    strategia = sys.argv[1]
    parametr = sys.argv[2]
    plikWejsiowy = sys.argv[3]
    plikWyjsciowy = sys.argv[4]
    statystyki = sys.argv[5]

def loadPuzzle():
    puzzle = []

    file = open(plikWejsiowy, 'r')
    temp = file.readline()
    cols = temp.split(" ")[0]
    rows = temp.split(" ")[1].split()[0]

    for line in file.readlines():
        numbers = line.strip().split()
        numbers = [int(number) for number in numbers]
        puzzle.append(numbers)

    return rows, cols, puzzle

file1 = open(plikWyjsciowy, 'w')


puzzle = PuzzleState(*loadPuzzle())

if (strategia == "bfs"):
    rozwiazania = bfs(puzzle, parametr)

    with open(plikWyjsciowy, 'w') as f:
        print(rozwiazania[0], file=f)
        print(rozwiazania[1], file=f)

    with open(statystyki, 'w') as f:
        print(rozwiazania[0], file=f)
        print(rozwiazania[2], file=f)
        print(rozwiazania[3], file=f)
        print(rozwiazania[4], file=f)   
        print(rozwiazania[5], file=f)  

elif (strategia == "dfs"):
    rozwiazania = dfs(puzzle, parametr)
    with open(plikWyjsciowy, 'w') as f:
        print(rozwiazania[0], file=f)
        print(rozwiazania[1], file=f)

    with open(statystyki, 'w') as f:
        print(rozwiazania[0], file=f)
        print(rozwiazania[2], file=f)
        print(rozwiazania[3], file=f)
        print(rozwiazania[4], file=f)   
        print(rozwiazania[5], file=f)  

elif (strategia == "astr"):
    rozwiazania = aStarPuzzle(puzzle,parametr)

    with open(plikWyjsciowy, 'w') as f:
        print(rozwiazania[0], file=f)
        print(rozwiazania[1], file=f)

    with open(statystyki, 'w') as f:
        print(rozwiazania[0], file=f)
        print(rozwiazania[2], file=f)
        print(rozwiazania[3], file=f)
        print(rozwiazania[4], file=f)   
        print(rozwiazania[5], file=f)  