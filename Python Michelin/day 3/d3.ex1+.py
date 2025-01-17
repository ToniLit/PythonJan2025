# version 1
vot= {
    1: "insuficient",
    2: "Suficient",
    3: "avrage",
    4: "outstanding",
    5: "exceptional"
    }
value = int(input("select your rate:\n"))
for key in vot:
    if key == value:
        print(vot[value])
    else: 
        print("key not found")
        break


# version1
is_key = False
vot= {
    1: "insuficient",
    2: "Suficient",
    3: "avrage",
    4: "outstanding",
    5: "exceptional"
    }
value = int(input("select your rate:\n"))
for key in vot:
    if key == value:
        print(vot[value])
        is_key= True
if not is_key:
    print("key not find")

# version3
is_key = False
vot= {
    1: "insuficient",
    2: "Suficient",
    3: "avrage",
    4: "outstanding",
    5: "exceptional"
    }
value = int(input("select your rate:\n"))
for key in vot:
    if key == value:
        print(vot[value])
        is_key= True
if not is_key:
    print("key not find")
# Verion 3

if value in vot
    print (vot [value]
else (
    Print[value]
)