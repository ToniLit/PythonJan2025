class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__ (self):
        return f"{self.name} is {self.age} years"
    

class Dog(Animal):
    def bark(self):
        print("vav" * self.age)


animal_obj= Animal("Boy",3)
print(animal_obj)

dog_obj= Dog("spike",10)
print(dog_obj)
dog_obj.bark()