class CAT:
    def __init__(self,name):
        self.name = name
    def __str__(self,):
        return f"{self.name}"
    def __call__(self, *args, **kwds):
        print("yes, I am here master")


rino= CAT("Rino")
print(rino)
value = 10
rino()