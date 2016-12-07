import re, random
from pprint import pprint

def get_file():
    with open('input.txt', 'r') as myfile:
        return myfile.readlines()

def supports_snooping(line):

    prefixes, hypernets = extract_lists(line)
    # print(hypernets)
    # print(prefixes)

    for hypernet in hypernets:
        if contains_abba(hypernet): return False
    for prefix in prefixes:
        if contains_abba(prefix): return True

    return False

def extract_lists(line):
    hypernets = []
    prefix = line.replace("\n", "")

    for hypernet in re.findall(r"\[(.*?)\]", line):
        hypernets.append(hypernet)

    for hypernet in hypernets:
        prefix = prefix.replace(hypernet, "")

    prefix = str.split(prefix, "[]")

    return prefix, hypernets


def contains_abba(word):
    return random.choice([True, False])

def main():
    ips = [ip7 for ip7 in get_file() if supports_snooping(ip7)]
    # supports_snooping(get_file()[0])
    pprint(len(ips))

if  __name__ =='__main__':main()
# wysextplwqpvipxdv[srzvtwbfzqtspxnethm]syqbzgtboxxzpwr[kljvjjkjyojzrstfgrw]obdhcczonzvbfby[svotajtpttohxsh]cooktbyumlpxostt
