#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_letra=None

if __name__ == "__main__":
    lista_valores= [] 

    for line in sys.stdin:
        line=line.replace("\n","")
        map_lines = line.split(",")
        letra,valor=map_lines
        valor=int(valor)
        
        if letra == current_letra:
           lista_valores.append(valor)
         
        else: 
            if current_letra is not None:
                lista_valores=sorted(lista_valores)
                cadena_valores= ",".join(str(i) for i in lista_valores)              
                sys.stdout.write("{}\t{}\n".format(current_letra, cadena_valores))
                lista_valores=[]
            current_letra = letra
            lista_valores.append(valor)


    lista_valores=sorted(lista_valores)
    cadena_valores= ",".join(str(i) for i in lista_valores)               
    sys.stdout.write("{}\t{}\n".format(current_letra, cadena_valores))