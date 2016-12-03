from Walker import Walker
import re

def getFile():
    with open('input.txt', 'r') as myfile:
        data=myfile.read().split(", ")
    return data    

def resolveInstructions(instList, walker):
    instructionsTuple = []
    for inst in instList:
        for direction, distance in re.findall("([L,R])(\d.*)", inst):
            instTuple = (direction, distance)
            instructionsTuple.append(instTuple)
            walker.walk(instTuple)

    return instructionsTuple


def main():
    walker = Walker()
    instructions = resolveInstructions(getFile(), walker)
    pos = walker.getPosition()
    distance = abs(pos[0]) + abs(pos[1])
    print(distance)


if  __name__ =='__main__':main()
