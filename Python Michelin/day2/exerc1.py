 

amnt =input("enter amount:")
amnt = int(amnt)
# rest = amnt//10   
# 10_________
tens = (amnt // 10)
rest10 = (amnt % 10)

# 5______
fives= (rest10//5)
rest5 =(rest10 % 5)

#2________
tow = (rest5 // 2)
rest2 = (rest5 % 2)
#1______
one = (rest2 // 1) 

# rest_tens= (amnt % fives)

print("TENS",  tens)
print("FIVES", fives)
print("TOW's", tow)
print("Ones", one)
print("_____________")
print("logic-spate")
print("rest10", rest10)
print("rest5", rest5)
print("rest2",rest2)
