import re

MULT_RE = re.compile(r"\((\d+)x(\d+)\)")

def get_file():
    with open('input.txt', 'r') as myfile:
        return myfile.read().splitlines()

def decode_line(line):
    line_dump = line
    line_output = []

    while MULT_RE.match(line_dump):
        match = MULT_RE.search(line_dump)

        inst_end = int(match.span()[1])
        payload_len = int(match.group(1))
        multiplier = int(match.group(2))
        payload = line_dump[inst_end:inst_end + payload_len]

        line_output.extend(payload * multiplier)
        line_dump = line_dump[(inst_end + payload_len):]

    line_output.extend(line_dump)
    return "".join(line_output)

def decode_file(lines):
    return [decode_line(line) for line in lines]

def main():
    lines = decode_file(get_file())
    print(sum(len(line) for line in lines))

if  __name__ == '__main__': main()
# 98135