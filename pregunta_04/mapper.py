#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


def split_lines(line):
    return line.split()


def blancos(line):
    linea= line.replace("'", "")
    return linea


if __name__ == "__main__":
    for line in sys.stdin:
        
        map_lines = split_lines(line)
       
        sys.stdout.write("{},1\n".format(blancos(map_lines[0])))