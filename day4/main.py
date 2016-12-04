import re
from collections import Counter

def getFile():
    with open('input.txt', 'r') as myfile:
        return myfile.readlines()
  

def decodeRooms(lines):
    decoded = []
    for line in lines:
        for letters, sectorId, checksum in re.findall("(.*)\-(\d{3,4})\[([a-z]{5})\]", line):
            letters = letters.replace("-", "")
            decoded.append((letters, sectorId, checksum))

    return decoded

def checkRoom(room):
    lettersGrouped = [(v, k) for k, v in Counter(room[0]).items()]
    lettersGrouped.sort(key=lambda roomtmp: roomtmp[0], reverse=True)
    newChecksum = getHighestHits(lettersGrouped)

    return all(letter in newChecksum for letter in room[2])

def getHighestHits(lettersGrouped):
    letters = []
    maxCount = max([count for count, letter in lettersGrouped])
    while(len(letters) < 5):
        batch = sorted([l for c,l in lettersGrouped if c is maxCount])
        letters.extend(batch)
        maxCount = maxCount - 1

    return letters[:5]

def main():
    rooms = decodeRooms(getFile())
    sumOfSectorIds = sum([int(r[1]) for r in rooms if checkRoom(r)])
    print(sumOfSectorIds)

if  __name__ =='__main__':main()
