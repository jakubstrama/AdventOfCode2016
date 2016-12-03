import re
from itertools import zip_longest

def getFile():
    with open('input.txt', 'r') as myfile:
        return myfile.readlines()


def readTriangles():
    trianglesText = getFile();
    triangles = []
    for line in trianglesText:
        for a,b,c in re.findall("(\d.*)\s(\d.*)\s(\d.*)", line):
            trg = [int(a),int(b),int(c)]
            trg.sort()
            triangles.append(trg)
    
    return triangles

 
def filterPossibleTringles(triangles):    
    return [t for t in triangles if t[0] + t[1] > t[2]]


def main():
    triangles = readTriangles()
    triangles = filterPossibleTringles(triangles)
    print(len(triangles))


if  __name__ =='__main__':main()
