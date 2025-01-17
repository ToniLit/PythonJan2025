
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