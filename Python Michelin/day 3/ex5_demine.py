# def ceva (x,y):
#     print("#"* x)

#     for _ in range(y -2):
#         print("#" + "" * (x-2)+ "#")
#     print("#" * x)


def ceva(x, y):

    print("#" * x)
    
    for _ in range(y - 2):
        print("#" + " " * (x - 2) + "#"+"\n")
    
    print("#" * x)
ceva(10, 5)