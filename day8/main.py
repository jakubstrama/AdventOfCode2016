from Screen import Screen
import re

rect_re = re.compile(r"rect\s(\d+)x(\d+)")
col_re = re.compile(r"rotate\scolumn\sx=(\d+)\sby\s(\d+)")
row_re = re.compile(r"rotate\srow\sy=(\d+)\sby\s(\d+)")
screen = Screen(6, 50)

def get_file():
    with open('input.txt', 'r') as myfile:
        return myfile.read().splitlines()

def exec_instructions(instructions):
    for inst in instructions:
        if(rect_re.match(inst)):
            for width, tall in rect_re.findall(inst): screen.rect(tall, width)
        if(col_re.match(inst)):
            for num, by in col_re.findall(inst): screen.rotate_column(num, by)
        if(row_re.match(inst)):
            for num, by in row_re.findall(inst): screen.rotate_row(num, by)
                
def main():
    exec_instructions(get_file())
    print(screen.count_lit())
    screen.print_code()

if  __name__ =='__main__':main()
# 106