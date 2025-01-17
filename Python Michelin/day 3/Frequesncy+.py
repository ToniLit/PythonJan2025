

numbers= [101,202,303,202,404, 404,]
frq = {}
for no in numbers:
        if no %2 == 0:
                frq[no] = frq.get(no,1) +1

print(frq)

max_frq = 0
for i in frq:
        if frq[i] > max_frq:
                max_frq= frq[i]
print("max FRQ", max_frq)
max_friquen = []
for f in frq:
        if frq[f] == max_frq:
                max_friquen.append(f)
print(max_friquen)

max_friquen.sort()

print(max_friquen[0])
print(min(max_friquen))