# class> keyword
# convention> clas name are capitals

class cat:
    pass
## create OBJ
cat_obj = cat("rino")
# aici ii dai nume 
print(cat_obj)

## create OBJ2
cat_obj1=cat("pierr")
print(cat_obj1)
#______________________________


class cat:
    def __init__ (self,name, age):# in loc de pass, o definesti 2 linii joc "int"
         self.name = name
## create OBJ
cat_obj=cat("Rino") 
# aici ii dai nume
print(cat_obj)
print(cat_obj.name)


## create OBJ2
cat_obj1=cat("pierr")
print(cat_obj1)