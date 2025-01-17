collection = (1, 2, 3, 4)
print(collection, type (collection))

for i in collection:
    print ("i=",i)

# diferite moduri de vizualizare
## indexing (READ) a value from a tuple

print("colection1",collection[0])#pozitia 0 este valuare  1, mereu incepem de la zero. ca sa aduci 4 de exemplu, pui 3
print("colection-1",collection[-1])
print("len",len(collection))

##Updating  valus from list
collection[2] =33333
print(collection)


