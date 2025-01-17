
amnt =input("enter amount:")
amnt = int(amnt)

banknotes = [100,50,20,5,1]

for note in banknotes:

    value = (amnt //note)
    print("banknote" , note, ":",value)
    print(f"bamknotes of {note}: {value}")
    amnt= amnt % note
print ("initial_amnt",amnt)



