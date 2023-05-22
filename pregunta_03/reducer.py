#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

def split_lines(line):
    return line.split(",")


def blancos(line):
    linea= line.replace("\n", "")
    return linea

if __name__ == "__main__":
    for line in sys.stdin:
        line= blancos(line)
        map_lines = split_lines(line)
        sys.stdout.write("{},{}\n".format(map_lines[1],map_lines[0]))

