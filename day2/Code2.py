class Code2:

    code = []
    location = None
    functions = {}

    def __init__(self):
        self.code.append([None,None,1,None,None])
        self.code.append([None,2,3,4,None])
        self.code.append([5,6,7,8,9])
        self.code.append([None,"A","B","D",None])
        self.code.append([None,None,"D",None,None])

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

        if((move is "U" or move is "D") and self.__checkValue(moveVal, self.location[1]) ):
            self.location = (moveVal, self.location[1])    
        if((move is "L" or move is "R") and self.__checkValue(self.location[0], moveVal) ):
            self.location = (self.location[0], moveVal)


    def __checkValue(self, a, b):
        try:
            if a < 0 or b < 0:
                return False

            value = self.code[a][b]

            if(value is None):
                return False

            return True
        except IndexError:
            return False