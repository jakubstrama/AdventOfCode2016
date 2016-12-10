import re

MULT_RE = re.compile(r".*\((\d+)x(\d+)\)")
STRICT_RE = re.compile(r"\((\d+)x(\d+)\)")

def get_file():
    with open('input.txt', 'r') as myfile:
        return myfile.read().splitlines()

def get_payload(dump):
    match = STRICT_RE.search(dump)
    instruction_end = int(match.span()[1])
    payload_len = int(match.group(1))
    multiplier = int(match.group(2))
    end = instruction_end + payload_len
    payload = dump[instruction_end:end]

    return multiplier, end, payload

def check_beginning(dump):
    match = STRICT_RE.search(dump)
    start = int(match.span()[0])

    return start, dump[start:]

def count_chars_rec(line):
    dump = line
    if not MULT_RE.match(dump):
        return len(dump)
    else:
        count = 0
        while MULT_RE.match(dump):
            start, dump = check_beginning(dump)
            count += start
            multiplier, end, payload = get_payload(dump)
            dump = dump[end:]
            count += multiplier * count_chars_rec(payload)

        return count

def main():
    count = count_chars_rec(get_file()[0])
    print(count)

if  __name__ == '__main__': main()
# 10964557606