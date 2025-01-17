class cat:
    def __init__ (self,name, age, inaltime):# in loc de pass, o definesti 2 linii joc "int"
         self.name = name
         self.age = age
         self.inaltime= inaltime

    def __str__ (self):
         return f"the cat: {self.name} has {self.age} years"
## create OBJ
cat_obj=cat("Rino",5.5,1.78) 
# aici ii dai nume
print(cat_obj)
print(cat_obj.name)
print(cat_obj.age)
print(cat_obj.inaltime)

#create OBJ2
cat_obj1= cat("Pierr",7.5, 2.88)
print(cat_obj1)
print(cat_obj1.name)
print(cat_obj1.age)
print(cat_obj1.inaltime)