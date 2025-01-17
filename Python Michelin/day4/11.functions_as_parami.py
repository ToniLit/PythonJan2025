def add (a,b):
    return a+ b

def diff(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a,b):
    return a/b

def do_oper (a,b, func):
    return func(a,b)

print(do_oper(30,50,add))
print(do_oper(3,1,mult))
print(do_oper(100,500,div))