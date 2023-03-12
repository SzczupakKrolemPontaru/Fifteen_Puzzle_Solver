class PuzzleState:
    rows = 0
    columns = 0
    array = []

    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

    directories = {"U", "D", "L", "R"}

    def __init__(self, rows, columns, puzzle):
        self.rows = int(rows)
        self.columns = int(columns)
        self.array = puzzle

    def __str__(self):
        result = ""
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                result += str(self.array[i][j]) + " "
            result += "\n"
        return result

    def move(self, dir):
        newBlank = (self.findIndexOfNum(0)[0] + dir[0], self.findIndexOfNum(0)[1] + dir[1])
        if ((newBlank[0] < 0) or (newBlank[0] >= self.rows) or (newBlank[1] < 0) or (newBlank[1] >= self.columns)):
            return False

        self.array[self.findIndexOfNum(0)[0]][self.findIndexOfNum(0)[1]] = self.array[newBlank[0]][newBlank[1]]
        self.array[newBlank[0]][newBlank[1]] = 0
        return True

    def check(self):
        for i in range(0, self.rows):
            for j in range(0, self.columns):
                if (i == self.rows - 1 and j == self.columns - 1):
                    if (self.array[i][j] != 0):
                        return False
                else:
                    expected = i * self.columns + j + 1
                    if (self.array[i][j] != expected):
                        return False
        return True

    def findIndexOfNum(self, number):
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                if self.array[i][j] == number:
                    return i, j
