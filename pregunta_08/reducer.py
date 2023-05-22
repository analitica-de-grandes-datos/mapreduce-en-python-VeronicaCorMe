#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key= None
conteo=0
suma=0.0

if __name__ == "__main__":
    for line in sys.stdin:
          line=line.replace("\n","")
          key,val = line.split(",")
          val=float(val)
          

          if key == current_key:
            suma = suma+ val
            conteo= conteo+ 1
            promedio= suma/conteo
          else: 
                if current_key is not None:
                    sys.stdout.write("{}\t{}\t{}\n".format(current_key, suma, promedio))
                    suma=0.0
                    promedio=0
                    conteo=0
                current_key = key
                suma=val
                conteo= 1
                promedio=suma/conteo
               
    sys.stdout.write("{}\t{}\t{}\n".format(current_key, suma, promedio))