#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


def split_lines(line):
    return line.split(",")

def select_column(line, x):
    return line[x]

def blancos(line):
    linea= line.replace("\n", "")
    linea= linea.replace("\r", "")
    return linea


if __name__ == "__main__":
    for line in sys.stdin:
        line=blancos(line)
        map_lines = split_lines(line)
        col0= select_column(map_lines,1)
        col1= select_column(map_lines,0)
        sys.stdout.write("{},{}\n".format(col0,col1))
