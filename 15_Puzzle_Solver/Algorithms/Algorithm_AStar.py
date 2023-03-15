import numpy as np


def ManhattanDistance(puzzle):
    h_points = 0
    goalArray = []

    for i in range(0, puzzle.rows):
        row = []
        for j in range(0, puzzle.columns):
            row.append(i * puzzle.columns + j + 1)
            if (i == puzzle.rows - 1 and j == puzzle.columns - 1):
                row.pop()
                row.append(0)
        goalArray.append(row)

    for i in range(puzzle.rows):
        for j in range(puzzle.columns):
            i1, j1 = puzzle.findIndexOfNum(goalArray[i][j])
            h_points += abs(i - i1) + abs(j - j1)

    return h_points


def HammingDistance(puzzle):
    h_points = 0

    for i in range(puzzle.rows):
        for j in range(puzzle.columns):
            if (i == puzzle.rows - 1 and j == puzzle.columns - 1):
                if (puzzle.array[i][j] != 0):
                    h_points += 1
            else:
                expected = i * puzzle.columns + j + 1
                if (puzzle.array[i][j] != expected):
                    h_points += 1

    return h_points
