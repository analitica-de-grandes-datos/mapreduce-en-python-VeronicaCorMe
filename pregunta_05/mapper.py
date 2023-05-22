#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


def split_lines(line):
    return line.split()



if __name__ == "__main__":
    for line in sys.stdin:
        
        map_lines = split_lines(line)
        mes = split_lines(map_lines[1][5:7])
        mes= mes[0]
        sys.stdout.write("{},1\n".format(mes))