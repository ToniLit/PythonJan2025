# List of numbers
no = [3,7,9,2,4,5,12,33,78,0,123]
print("Lista initiala:",no)
# Source

odds = [i for i in no if i no % 2 ==1]
evens = [i for i in no if i no % 2 ==0]


# for number in no:
#     if number % 2 == 0:
#         evens.append(number)
#     else:
#         odds.append(number)
print ("Odds",odds)
print ("evens:",evens)