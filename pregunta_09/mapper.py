#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys


if __name__ == "__main__":
    for line in sys.stdin:
        map_lines = line.split()
        sys.stdout.write("{},{},{}\n".format( map_lines[2],map_lines[0],map_lines[1]))