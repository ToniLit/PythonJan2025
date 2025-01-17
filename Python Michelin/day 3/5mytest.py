
def ceva(x, y, symbol ="@"):

    print("#" * x)
    
    for _ in range(y - 2):
        print("#" + " " * (x - 2) + "#"+"\n")
    
    print("#" * x)
print(ceva(10, 5))
print (ceva(10, 5))