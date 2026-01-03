### Ham kiem tra snduong a is so Armstrong:
# Quy tac: tong luy thua bac k = chinh nó, k la so chu so
import math

def is_armstrong(a):
    ## Lay k
    k = len(str(a))

    ## Tinh tong luy thua
    sum = 0
    for char in str(a):
        # Ep ve int
        num = int(char)
        sum += math.pow(num, k)

    return int(sum) == a


print(is_armstrong(153))
