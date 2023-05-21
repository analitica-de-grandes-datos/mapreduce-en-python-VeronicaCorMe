#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


def split_lines(line):
    return line.split(",")


def select_column(line, x):
    return line[x]


if __name__ == "__main__":
    for line in sys.stdin:
        map_lines = split_lines(line)
        amount = select_column(map_lines, 4)
        purpose = select_column (map_lines, 3)
        sys.stdout.write("{}\t{}\n".format(purpose, amount))
