from collections import deque

class Walker:
    x = 0
    y = 0
    visited = set()

    __lastQuePos = 0
    __lastDirecion = "N"
    __dirque = deque('NESW')

    def __init__(self):
        self.visited.add((0,0))

    def walk(self, inst):
        dir = inst[0]
        dist = int(inst[1])
        dispatcher = {'N': self.__goY, 'E': self.__goX, 'S': self.__goY, 'W': self.__goX}

        if(dir is "R"):
            self.__lastQuePos = (self.__lastQuePos + 1) % 4
        if(dir is "L"):
            self.__lastQuePos = (self.__lastQuePos - 1) % 4
            
        direction = self.__dirque[self.__lastQuePos]

        if(direction is "S" or direction is "W"):
            dist = -dist
        
        pointOld = (self.x, self.y)
        dispatcher[direction](dist)

        return self.__addPoints(pointOld, (self.x, self.y))


    def __goY(self, dist):
        self.y = self.y + dist

    def __goX(self, dist):
        self.x = self.x + dist

    def __addPoints(self, pointOld, pointNew):
        newPoints = []
        deltaX = pointNew[0] - pointOld[0]
        deltaY = pointNew[1] - pointOld[1]
        direct = -1 if deltaY < 0 or deltaX < 0 else 1

        if(deltaX is 0): 
            for i in range(pointOld[1] + direct, pointNew[1] + direct, direct):
                newPoints.append((pointOld[0], i))

        if(deltaY is 0): 
            for i in range(pointOld[0] + direct, pointNew[0] + direct, direct):
                newPoints.append((i, pointOld[1]))

        for point in newPoints:
            if(point in self.visited):
                print("visited point!:" + str(point))    
            self.visited.add(point)


    def getPosition(self):
        return (self.x, self.y)