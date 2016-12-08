import re

reg = re.compile(r"\[(.*?)\]")

def get_file():
    with open('input.txt', 'r') as myfile:
        return myfile.readlines()

def supports_ssl(line):
    supernets, hypernets = extract_lists(line)
    return contains_aba(supernets, hypernets)

def extract_lists(file_line):
    line = file_line.replace("\n", "")
    hypernets = [h for h in reg.findall(line)]
    for h in hypernets: line = line.replace("[" + h + "]", " ")

    supernets = str.split(line, " ")
    return supernets, hypernets

def contains_aba(supernet, hypernets):
    abas = [word[i:i+3] for word in supernet for i in range(0, len(word) - 2) if is_aba(word[i:i+3])]
    return bool([(word, aba) for word in hypernets for aba in abas if reverse_aba(aba) in word])

def reverse_aba(aba):
    return aba[1] + aba[0] + aba[1]

def is_aba(text):
    return text[0] == text[2] and text[0] != text[1]

def main():
    ips = [ip7 for ip7 in get_file() if supports_ssl(ip7)]
    print(len(ips))

if  __name__ =='__main__':main()
# 260
