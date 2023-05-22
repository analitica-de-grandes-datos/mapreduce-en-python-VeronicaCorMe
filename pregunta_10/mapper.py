#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    
    for line in sys.stdin:
        line = line.replace("\r","")
        line = line.replace("\n","")
        map_line = line.split("\t")
        map_line[1]= map_line[1].split(",")
        for x in map_line[1]:
            sys.stdout.write("{},{}\n".format(x,map_line[0]))