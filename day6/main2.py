from collections import Counter

def get_file():
    with open('input.txt', 'r') as myfile:
        return myfile.readlines()

def decode_messages(lines):
    length = len(lines[0].replace("\n", ""))
    decoded = [[] for i in range(0, length)]

    for line in lines:
        line = line[:length]
        for i in range(0, length):
            decoded[i].append(line[i])

    letters = [Counter(dec).most_common()[-1] for dec in decoded]
    return "".join([l for l, c in letters])

def main():
    print(decode_messages(get_file()))

if  __name__ =='__main__':main()
# aovueakv