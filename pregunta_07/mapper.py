#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

lista_datos = []
lista_ordenada= []
def split_lines(line):
    return line.split()
if __name__ == "__main__":
    for line in sys.stdin:
        map_lines = split_lines(line)
        lista_datos.append((int(map_lines[2]),map_lines[1],map_lines[0]))
    lista_datos = sorted(lista_datos)

    contador=0
    for datos in lista_datos:
        lista_ordenada.append((datos[2], datos[0], datos[1]))
    lista_ordenada=sorted(lista_ordenada)
    for datos in lista_ordenada:
        contador= contador +1
        sys.stdout.write("{}\t{}\t{}\t{}\n".format(datos[0], contador, datos[2],datos[1]))

   