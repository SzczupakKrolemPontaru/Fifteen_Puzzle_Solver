
import queue

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)
def kurwa(puzzle):
    kolejka = queue.Queue()

    if puzzle.check():
        print("za pierwszym kurwa")
        return puzzle
    kolejka.put(puzzle)

    while not kolejka.empty():

        current = kolejka.get()

        if current.check():
            return current

        if  current.findIndexOfNum(0)[0] != 0:
            temp = current
            temp.move(UP)
            if temp.check():
                return temp
            kolejka.put(temp)

        if  current.findIndexOfNum(0)[1] != 0:
            temp = current
            temp.move(LEFT)
            if temp.check():
                return temp
            kolejka.put(temp)

        if  current.findIndexOfNum(0)[0] != current.rows:
            temp = current
            temp.move(DOWN)
            if temp.check():
                return temp
            kolejka.put(temp)


        if  current.findIndexOfNum(0)[1] != current.columns:
            temp = current
            temp.move(RIGHT)
            if temp.check():
                return temp
            kolejka.put(temp)

