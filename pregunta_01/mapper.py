#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


def split_lines(line):
    return line.split(",")


def select_column(line):
    return line[2]


if __name__ == "__main__":
    for line in sys.stdin:
        map_lines = split_lines(line)
        credit_history = select_column(map_lines)
        sys.stdout.write("{}\t1\n".format(credit_history))
