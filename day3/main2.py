import re
from itertools import zip_longest


def getFile():
    merged = []
    with open('input.txt', 'r') as myfile:
        for lines in zip_longest(*[myfile] * 3):
            merged.append(lines)
    return merged


def readTriangles():
    trianglesText = getFile();
    triangles = []
    for lines in trianglesText:
        trg1 = []
        trg2 = []
        trg3 = []

        for line in lines:    
            for a,b,c in re.findall("(\d.*)\s(\d.*)\s(\d.*)", line):
                trg1.append(int(a))            
                trg2.append(int(b))            
                trg3.append(int(c))

        trg1.sort()
        trg2.sort()
        trg3.sort()

        triangles.append(trg1)
        triangles.append(trg2)
        triangles.append(trg3)
    
    return triangles    

def filterPossibleTringles(triangles):
    return [t for t in triangles if t[0] + t[1] > t[2]]


def main():
    triangles = readTriangles()
    triangles = filterPossibleTringles(triangles)
    print(len(triangles))



if  __name__ =='__main__':main()
