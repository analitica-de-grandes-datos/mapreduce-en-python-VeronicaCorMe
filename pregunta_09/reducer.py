#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

lista_datos=[]

def split_lines(line):
    return line.split(",")


if __name__ == "__main__":
    for line in sys.stdin:
        line=line.replace("\n","")
        map_lines = split_lines(line)
        lista_datos.append((int(map_lines[0]),map_lines[1], map_lines[2]))
    lista_datos=sorted(lista_datos)


    for datos in lista_datos[:6]:
        sys.stdout.write("{}\t{}\t{}\n".format( datos[1],datos[2],datos[0]))
    