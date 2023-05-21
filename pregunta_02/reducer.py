#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

current_key= None
max_amount=0

if __name__ == "__main__":
    for line in sys.stdin:
          key,val = line.split("\t")
          val= int(val)
          
          if key == current_key:
               if max_amount<val:
                    max_amount= val

          else: 
                if current_key is not None:
                    sys.stdout.write("{}\t{}\n".format(current_key, max_amount))
                current_key = key
                max_amount= 0
    sys.stdout.write("{}\t{}\n".format(current_key, max_amount))
