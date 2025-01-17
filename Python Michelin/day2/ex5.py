
# date de la care pleci
data_inceput = 2000
data_sfarsit = 2025
# rezultat 2010, 2011...2015 dar unul sub celalalt
ani = []
#version 1
for an in range(data_inceput, data_sfarsit + 1):
    if an % 4 == 0:
        print(an)
# print("Anii specifici:", ani)

# adugare an bisect
print ()
print ("Verdsion 2")
if data_inceput%4 ==0:
    primulBisesc=data_inceput//4 * 4 +4
else :
    pass
for an in range(data_inceput, data_sfarsit + 1):
    if an % 4 == 0:
        print(an)

