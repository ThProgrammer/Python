def fatorial (n, show=False):
    f = 1
    for i in range (n, 0, -1):
        f*=i
        if show:
            print(i, end=" ")
            if i > 1:
                print("x", end = " ")
            else:
                print("=", end=" ")
    return f
#

def dobro(n):
    return n*2
#

def triplo(n):
    return n*3
#    