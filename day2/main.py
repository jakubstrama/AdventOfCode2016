import re
from Code import Code
from Code2 import Code2

def getFile():
    with open('input.txt', 'r') as myfile:
        return myfile.readlines()
  

def main():
    lines = getFile()
    code = Code()
    code2 = Code2()
    for line in lines:
        print(code.move(line))

    print("*********************** Part Two ***************************")
    for line in lines:
        print(code2.move(line))

    

if  __name__ =='__main__':main()
