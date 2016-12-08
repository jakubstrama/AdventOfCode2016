import re
from collections import Counter

reg = re.compile(r"\[(.*?)\]")

def get_file():
    with open('input.txt', 'r') as myfile:
        return myfile.readlines()

def supports_snooping(line):
    prefixes, hypernets = extract_lists(line)
    for hypernet in hypernets:
        if contains_abba(hypernet): return False
    for prefix in prefixes:
        if contains_abba(prefix): return True

    return False

def extract_lists(line):
    hypernets = [h for h in reg.findall(line)]
    prefix = line.replace("\n", "")
    for hypernet in hypernets:
        prefix = prefix.replace(hypernet, "")

    prefix = str.split(prefix, "[]")
    return prefix, hypernets

def contains_abba(word):
    for i in range(0, len(word) - 3):
        text = word[i:i+4]
        if Counter(text).get(text[0]) is 4: 
            return False
        if text[0:2] == text[2:4][::-1]: 
            return True

    return False

def main():
    ips = [ip7 for ip7 in get_file() if supports_snooping(ip7)]
    print(len(ips))

if  __name__ =='__main__':main()
# 118
