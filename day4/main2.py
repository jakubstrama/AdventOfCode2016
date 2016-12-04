import re
from collections import Counter

ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def getFile():
    with open('input.txt', 'r') as myfile:
        return myfile.readlines()
  

def decodeRooms(lines):
    decoded = []
    for line in lines:
        for letters, sectorId, checksum in re.findall("(.*)\-(\d{3,4})\[([a-z]{5})\]", line):
            decoded.append((letters, sectorId, checksum))

    return decoded

def decypherRoom(room):
    names = room[0].split("-")
    words = []
    for name in names:
        word = []
        for l in name:
            word.append(resolveLetter(l, room[1]))
        words.append("".join(word))
    
    joinedName = " ".join(words)
    return (joinedName, room[1], room[2])

def resolveLetter(l, sectorId):
    global ABC
    indexOfLetter = (ABC.index(l) + int(sectorId)) % 26

    return ABC[indexOfLetter]

def main():
    rooms = decodeRooms(getFile())
    rooms = [decypherRoom(room) for room in rooms]
    filtered = [room[1] for room in rooms if "northpole" in room[0]]

    print(filtered)



if  __name__ =='__main__':main()
