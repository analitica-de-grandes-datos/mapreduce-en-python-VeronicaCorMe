#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key= None
maximo=0
minimo=10000

if __name__ == "__main__":
    for line in sys.stdin:
          key,val = line.split(",")
          val=float(val)
          key=str(key)
          if key == current_key:
            if val>=maximo:
                maximo = val
            if val<= minimo:
                minimo = val
          else: 
                if current_key is not None:
                    sys.stdout.write("{}\t{}\t{}\n".format(current_key, maximo, minimo))
                current_key = key
                maximo=val
                minimo=val
    sys.stdout.write("{}\t{}\t{}\n".format(current_key, maximo, minimo))