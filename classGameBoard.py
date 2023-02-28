class GameSpace:
    def __init__(self, pos, fill):
        self.position = pos
        self.fill = fill

    def check_below(self, width, height):
        maxsize = height * width
        if self.position + width > maxsize:
            return False
        else:
            return True

    def check_above(self, width):
        if self.position - width < 0:
            return False
        else:
            return True

    def check_left(self, width):
        if self.position % width == 1:
            return False
        else:
            return True

    def check_right(self, width):
        if self.position % width == 0:
            return False
        else:
            return True

    def print_cords(self, width, height):
        row = int((self.position / width) + 1)
        col = int((self.position % width) + 1)
        newstring = "[" + str(col) + "," + str(row) + "]"
        return newstring


class GameBoard:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.maxsize = width * height
        self.spaces = []
        for x in range(self.maxsize):
            self.spaces.append(GameSpace(x, 0))

    def print_board(self):
        for space in range(len(self.spaces)):
            if (space + 1) % self.width == 0:
                print(self.spaces[space].print_cords(self.width, self.height))
            else:
                print(self.spaces[space].print_cords(self.width, self.height), end=" ")
