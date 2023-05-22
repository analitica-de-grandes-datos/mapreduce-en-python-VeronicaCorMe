#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key= None
total=0

if __name__ == "__main__":
    for line in sys.stdin:
          key,val = line.split(",")
          val= int(val)
          key=str(key)
          if key == current_key:
               total += val
          else: 
                if current_key is not None:
                    sys.stdout.write("{}\t{}\n".format(current_key, total))
                current_key = key
                total= val
    sys.stdout.write("{}\t{}\n".format(current_key, total))