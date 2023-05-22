#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


def split_lines(line):
    return line.split()


if __name__ == "__main__":
    for line in sys.stdin:
        map_lines = split_lines(line)
        sys.stdout.write("{},{}\n".format( map_lines[0],map_lines[2]))
