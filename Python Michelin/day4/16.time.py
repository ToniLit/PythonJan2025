import time
import random


print(time.time())


asteptare= random.randint(1,5)

print("wait for sec:", asteptare)

time.sleep(asteptare)

print (time.time())