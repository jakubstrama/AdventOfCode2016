import traceback
class Code:

    code = []
    location = None
    functions = {}

    def __init__(self):
        self.code.append([1,2,3])
        self.code.append([4,5,6])
        self.code.append([7,8,9])

        self.location = (1,1)

        self.functions["U"] = (lambda : self.location[0] - 1)
        self.functions["D"] = (lambda : self.location[0] + 1)
        self.functions["L"] = (lambda : self.location[1] - 1)
        self.functions["R"] = (lambda : self.location[1] + 1)

    def move(self, moves):
        moves = moves.replace("\n", "")
        for move in moves:
            self.__move(move)

        return self.code[self.location[0]][self.location[1]]      


    def __move(self, move):
        moveVal = self.functions[move]()

        if(move is "U" or move is "D"):
            if(not self.__checkValue(moveVal, self.location[1])):
                return
            self.location = (moveVal, self.location[1])    
        if(move is "L" or move is "R"):
            if(not self.__checkValue(self.location[0], moveVal)):
                return
            self.location = (self.location[0], moveVal)

    def __checkValue(self, a, b):
        try:
            if a < 0 or b < 0:
                raise IndexError
            value = self.code[a][b]
            return True
        except IndexError:
            return False

