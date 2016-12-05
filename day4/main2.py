import re

ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def get_file():
    with open('input.txt', 'r') as myfile:
        return myfile.readlines()

def decode_rooms(lines):
    decoded = []
    for line in lines:
        for letters, sector_id, checksum in re.findall(r"(.*)\-(\d{3,4})\[([a-z]{5})\]", line):
            decoded.append((letters, sector_id, checksum))

    return decoded

def decypher_room(room):
    names = room[0].split("-")
    words = []
    for name in names:
        words.append("".join(resolve_letter(l, room[1]) for l in name))

    return (" ".join(words), room[1], room[2])

def resolve_letter(l, sectorId):
    return ABC[(ABC.index(l) + int(sectorId)) % 26]

def main():
    rooms = [decypher_room(room) for room in decode_rooms(get_file())]
    filtered = [room[1] for room in rooms if "northpole" in room[0]]

    print(filtered)

if  __name__ == '__main__': main()
