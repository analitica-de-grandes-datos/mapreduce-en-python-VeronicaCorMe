#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

lista_datos= []
if __name__ == "__main__":
    for line in sys.stdin:
        map_lines=line.split("\t")
        lista_datos.append((int(map_lines[1]),map_lines[0],map_lines[2],map_lines[3]))
        lista_datos= sorted(lista_datos)
        
    for datos in lista_datos:
        sys.stdout.write("{}\t{}\t{}".format(datos[1], datos[2], datos[3]))